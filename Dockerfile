# 
FROM reg.redrock.team/library/python:3.9

# 

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 
COPY . /code/app
#
WORKDIR /code/app
# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
