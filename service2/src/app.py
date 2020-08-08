from flask import Flask
import json
import requests
import os
app = Flask(__name__)
C1_URL= os.getenv('BASE_URL','http://172.17.0.2:6000')
@app.route('/add')
def add():
    try:
    	data= requests.get(C1_URL+'/calculate')
    except Exception as e:
        print(e)
    print(data.json())
    return data.json()

@app.route('/')
def index():
    data={"data":200}
    return json.dumps(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")



