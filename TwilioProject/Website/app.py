from flask import Flask, render_template,request, redirect,url_for
from flaskext.mysql import MySQL
from twilio.rest import TwilioRestClient
import string
import SimplifiedDES
import PlaintextProcessing
import KeyProcessing
import DESS
import Call
import ReturnCipher
import text
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Vfs@0001'
app.config['MYSQL_DATABASE_DB'] = 'Encryption'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/')
def hello_world():
    author = "Meha"
    name = "to the world of Encryption"
    return render_template('index.html', author=author, name=name)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showLogin')
def showLogin():
    return render_template('login.html')

@app.route('/Authenticate', methods = ['GET','POST'])
def Authenticate():
    if request.method =='POST':
        email = request.form['email']
        utaid=request.form['utaid']
        username=request.form['username']
        password=request.form['password']
        cursor = mysql.connect().cursor()
        print(email)
        cursor.execute("SELECT * from Users where email= '"+ email+"'")

        data = cursor.fetchone()
        if data is None:
            sql="insert into Users (userId,username,email,password) Values ('%s','%s','%s','%s')"%(utaid,username,email,password)
            print(sql)
            conn=mysql.connect()
            cursor = conn.cursor()
            # cursor.execute('START TRANSACTION')
            cursor.execute(sql)
            print('correct')
            conn.commit()
            return redirect('/')
        else:
            print("User already present in the system. Please login")
            return redirect('/')
    else:
        print("Please send data with post method")
        return redirect('/')

@app.route('/Login',methods = ['GET','POST'])
def Login():
    if request.method =='POST':
        email=request.form['email']
        password=request.form['password']
        sql="SELECT * from Users where email='%s' and password='%s'"%(email,password)
        print(sql)
        conn=mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        if data is None:
            print("Invalid credentials. Please login again")
            Call.CallHelp("+16825524196","+16823074500")
            return redirect('/')
        else:
            return redirect('/Encrypt')
    else:
        print("The form method is not post")
        return redirect('/')
@app.route('/Encrypt',methods = ['GET','POST'])
def Encrypt():
    return render_template("Encrypt.html")
@app.route('/showSimplifiedDES')
def showSimplifiedDES():
    return render_template("DES.html")


@app.route('/DES', methods = ['GET','POST'])
def DES():
    if request.method =='POST':
        name=request.form['first_name']
        utaId=request.form['utaid']
        userInput=request.form['desEncrypt']
        print(name)
        print(utaId)
        print(userInput)
        print("encrypted text entered by the user is:"+userInput)

        ciphertext=DESS.Encipher(name,utaId)
        print("Cipher text generated is:"+ciphertext)
        if ciphertext==userInput:
            print("same")
            return render_template("DESCheck.html")
        else:
            print("Different")
            return redirect('/')
    else:
        print("THe form method is incorrect")
        return redirect('/')

@app.route('/DESOutput', methods = ['GET','POST'])
def  DESOutput():
    if request.method =='POST':
        pt=request.form['plaintext']
        ciphertext=ReturnCipher.Encipher(pt)
        print(ciphertext)
        text.TextMessage(pt)
        return render_template('DESOutput.html',ciphertext=ciphertext)
    else:
        print("Please use the post method to submit the form")
        return redirect('/')


if __name__ == '__main__':
    app.run()
