from flask import Flask
import json

app = Flask(__name__)

@app.route('/add')
def add():
    data= requests.get("http://c1:6000/calculate)
    return json.dumps(data)

if __name__=="__main__":
	app.run(host="0.0.0.0",port=6000)



