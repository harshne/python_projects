from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint


app = Flask(__name__)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    return "My app"
@app.route("/hello/<string:name>")
def first(name):
    states=["texas","oklahoma","new york","maine"]
    rand = randint(0,len(states)-1)
    state=states[rand]
    print (state)
    return render_template("data.html",name = name,state = state)

if __name__=="__main__":
    app.run(port=80) 