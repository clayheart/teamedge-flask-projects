from flask import Flask, render_template, request, redirect, url_for, request
app = Flask(__name__)

app = Flask(__name__)

@app.route('/success' , methods=['GET', 'POST'])
def success():
   message = request.form['message']
   return render_template("login.html", message = message)

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0' 

 