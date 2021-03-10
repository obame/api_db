FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /home/app/app

RUN pip install --no-cache-dir fastapi
RUN pip install pymysql
RUN pip install mysqlclient


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app

CMD ["uvicorn", "main:app", "--reload"]
CMD ["uvicorn", "main:app", "--host 172.18.0.2"]