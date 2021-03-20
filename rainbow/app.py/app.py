from flask import Flask, render_template,current_app as app

app = Flask(__name__)

 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/')
def index():
    return 'Welcome to Clays Rainbow project!'

@app.route('/')
def index():
    return 'red.html'


@app.route('/')
def index():
    return 'purple.html'

@app.route('/')
def index():
    return 'blue.html'

@app.route('/')
def index():
    return 'indigo.html'

@app.route('/')
def index():
    return 'green.html'

@app.route('/')
def index():
    return 'yellow.html'


@app.route('/')
def index():
    return 'orange.html'