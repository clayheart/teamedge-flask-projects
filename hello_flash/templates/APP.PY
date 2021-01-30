from flask import flask, render_template 
from datetime import date


app = flask(__name__)

@app.route('/')
def show_nasa_pic():
	today = str(date.today())
	responce = request.get('')
	data= respond	



if __name__ =='__main__':
	app.run(debug = True, host='127.0.0.1')
