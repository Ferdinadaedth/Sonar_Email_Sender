# Sonar email sender
## 功能
用于在CI自动化sonarqube代码检查后，自动将代码检测报告通过邮件发送给puhser

## 使用方法

### webhook配置

需要在仓库里配置webhook地址，本项目部署后webhook地址为`[你的部署地址]/webhook/event`，可自定义哪些分支做了哪些操作时触发请求

### 邮件发送逻辑

本项目使用gitea，用户邮件暂时未配置，所以通过从请求信息中的用户名加上邮箱后缀组合的方式发送给pusher
，如果配置了用户邮件那么可直接从data['pusher']['email']中拿到邮件数据

### 参数配置


| 参数                 | 解释           |
| -------------------- | -------------- |
| EMAIL_ADDR           | 邮件服务器地址 |
| EMAIL_SERVER_PASS    | 邮件发送地址   |
| EMAIL_SERVER         | 邮件服务器密码 |
| SONAR_PASS sonarqube | 服务端登录密码 |
| SONAR_URL sonarqube  | 服务端地址     |
| SONAR_USER sonarqube | 服务端登录用户 |


### 部署

#### docker

```angular2html
docker run -d -p 8000:80\
  -e EMAIL_ADDR=sonarqube@example.com \
  -e EMAIL_SERVER=smtp.feishu.cn \
  -e EMAIL_SERVER_PASS=password \
  -e SONAR_PASS=password \
  -e SONAR_URL=https://sonarqube.example.com \
  -e SONAR_USER=user \
  sonar_email_sender:1.5
```
#### k8s

配置好deploy目录下的yaml文件后，apply deploy/目录下的所有文件即可