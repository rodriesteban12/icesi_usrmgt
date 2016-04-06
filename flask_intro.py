from flask import Flask
import json
import commands
app = Flask(__name__)

@app.route("/")
def hello():

	r=commands.getoutput('ls /home |sort')
	b=r.split("\n")
	t=json.dumps(b)
	return t;

if __name__ =="__main__":
	app.run('0.0.0.0' ,debug=True)
