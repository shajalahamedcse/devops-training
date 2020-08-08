
FROM python:3.6.5-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY src /app/
EXPOSE 6000
#CMD ["sleep","3600"]
CMD ["python","app.py"]
