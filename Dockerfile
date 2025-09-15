FROM python:3.11-slim
RUN  mkdir /app
WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt  /app/
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]