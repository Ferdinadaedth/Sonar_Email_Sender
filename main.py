from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from email_sender import sendmail
from sonar import getSonarqubeInfo

app = FastAPI()


@app.post("/webhook/event")
async def webhook(request: Request):
    # 获取请求体中的 JSON 数据
    data = await request.json()

    # 提取必要的信息
    username = data['pusher']['username']
    email_suffix = "@example.com"
    user_email = username + email_suffix
    ref = data['ref']
    branch = ref.split('/')[-1]
    project = data['repository']['name']  # 获取项目名
    print(project, branch, user_email)

    url = "https://example.redrock.team/"
    sonar_user="admin"
    sonar_pass="password"
    sonarqube_data = getSonarqubeInfo(branch=branch, component=project, url=url,username=sonar_user,password=sonar_pass)

    project_url = f"{url}dashboard?id={project}&branch={branch}"
    msg = create_email_content(project_url, user_email, project, branch, sonarqube_data)

    fromaddr = "sonarqube@example.com"
    smtpserver = "smtp.example.cn"
    subject = "代码质量检测"
    password = "password"
    sendmail(subject, msg, [user_email], fromaddr, smtpserver, password)

    return PlainTextResponse("Webhook received and processed.")


def create_email_content(project_url, user_email, project, branch, sonarqube_data):
    with open("email_template.html", "r", encoding="utf-8") as file:
        html_text = file.read()
    html_text = html_text.format(project_url=project_url,
                                 user_mail=user_email,
                                 project=project,
                                 branch=branch,
                                 lines=sonarqube_data["ncloc"],
                                 bugs=sonarqube_data["bugs"],
                                 vulnerabilities=sonarqube_data["vulnerabilities"],
                                 code_smells=sonarqube_data["code_smells"],
                                 ncloc_language_distribution=sonarqube_data["ncloc_language_distribution"],
                                 duplicated_lines_density=sonarqube_data["duplicated_lines_density"],
                                 reliability_rating=sonarqube_data["reliability_rating"],
                                 security_rating=sonarqube_data["security_rating"],
                                 comment_lines_density=sonarqube_data["comment_lines_density"],
                                 sqale_rating=sonarqube_data["sqale_rating"]
                                 )
    return html_text
