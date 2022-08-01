from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sobre")
def sobre():
    return "<h1> Portal de vendas de coisas novas e usadas</h1>"

@app.route("/sobre/privacidade")
def privacidade():
    return "<h4> Privacidade nao existe neste site</h4>"

@app.route("/user/<username>")
def username(username):
    cok = make_response("<h2>cookie criado</h2>")
    cok.set_cookie('username', username)
    return cok

@app.route("/user2/")
@app.route("/user2/<username>")
def username2(username=None):
    cokusername = request.cookies.get('username')
    print(cokusername)
    return render_template('user.html',username=username, cokusername=cokusername)