from flask import request, redirect,flash
from flask import Flask, render_template, request,url_for
from flask import g
import sqlite3
app = Flask(__name__)
conn = sqlite3.connect("emails.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE email_addresses ( email TEXT );")

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')

@app.route('/emails.html')
def emails():
    email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
    return render_template('emails.html', email_addresses=email_addresses)
