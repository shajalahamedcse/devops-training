from flask import Flask
import json

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    return json.dumps({'data':8})

if __name__=="__main__":
	app.run(host="0.0.0.0",port=6000)



