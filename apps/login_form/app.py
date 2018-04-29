from flask import Flask,flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login',methods=['POST'])
def login():
    if request.form['passwd']=="testing" and request.form['user']=="admin":
        session['logged_in']=True
        return index()
    else:
        flash("Please check the creds")
        return index()

@app.route('/logout')
def logout():
    session['logged_in']=False
    return index()



if __name__=="__main__":
    app.secret_key=os.urandom(10)
    app.run(port=80,debug=True)