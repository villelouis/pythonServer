import flask
import req 
from flask import Flask, session, redirect, url_for, escape, request, render_template
import json
import os
from req import sessionM, auth, sms, get_data, logout
from flask import g

app = Flask(__name__)
# f = sessionM('10.42.0.1:5000')
f = sessionM('192.168.43.233:5000')
@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':
               
        username = request.form['username']
        password = request.form['password']

        session['user']=username
        if auth(f, username, password):
            return redirect(url_for('sms_view'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    
@app.route("/sms",methods=['POST','GET'])
def sms_view():
    if request.method == 'POST':
       
        sms_s = request.form['sms']
        if sms(f, sms_s):
            return redirect(url_for('main_window')) #изменения
        else:
            return redirect(url_for('sms_view'))
    else: 
        return render_template('sms.html') #изменения

@app.route("/main")
def main_window():    
    data = get_data(f,session['user'])
    # return data
    return render_template('index.html',user = session['user'], money = data['account'])

@app.route("/logout")
def logout_view():
    if logout(f):
        return redirect(url_for('login'))
    return "Something Wrong (Client SIDE)"

app.secret_key = os.urandom(24)
app.run(debug = True,port = 3000,use_reloader=False)

