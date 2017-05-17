from flask import request, redirect,flash
from flask import Flask, render_template, request,url_for
from flaskext.mysql import MySQL
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Vfs@0001'
app.config['MYSQL_DATABASE_DB'] = 'Encryption'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn=mysql.connect()
cursor=conn.cursor()
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    flash(_name)
    flash(_email)
    print("The email id of the user is:"+_email)
    return redirect(url_for('result'))

if __name__ == '__main__':
    app.run()
