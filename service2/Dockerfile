
FROM python:3.6.5-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY src /app/
ENV BASE_URL="http://c1:6000"
EXPOSE 5000
#CMD ["sleep","3600"]
CMD ["python","app.py"]
