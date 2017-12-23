from flask import Flask
from models import User
from database import db_session
import ssl
import os
from sms import send_sms
import random
import string
import hashlib
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# ==============================================================
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    # default_limits=["15 per day", "3 per hour"]
)
# ==============================================================
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


print(User.query.all())
print(User.query.filter(User.username == "villelouis").first())
print(User.query.filter(User.username == "alexander").first())
print(User.query.filter(User.username == "asdd").first())

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')

# host='0.0.0.0'

app.secret_key = os.urandom(24)


from flask import Flask,session, request, flash, jsonify,url_for, redirect, render_template, abort ,g,session
from flask_login import login_user , logout_user , current_user , login_required

from flask_login import LoginManager
login_manager = LoginManager()
import hashlib, binascii
login_manager.init_app(app)

def to_hash(string):
    string = string.encode()
    dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
    dk = binascii.hexlify(dk)
    return dk

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id)).first()

@limiter.limit("100/day;12/hour;6/minute")
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        registered_user = User.query.filter(User.username == username).first()
        if (registered_user is None):
            flash('Username or Password is invalid' , 'error')
            # return redirect(url_for('login'))
            return "False"
        # print("Смотри " + registered_user.password + "и" + password)           
        if (registered_user.password != to_hash(password) ):
            flash('Username or Password is invalid' , 'error')
            # return redirect(url_for('login'))
            return "False" 

       
        
        sms_n = (''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(6)))
        #TEEEEEEEEEEEEEEST
        # sms_n = "A"
        #TEEEEEEEEEEEEEEST
        print("СЕКРЕТНАЯ СМС ", sms_n)
        session[sms_n]=registered_user.username
        registered_user.sms = sms_n
        # Отправка СМС. Включить:
        send_sms(registered_user.phone,str(sms_n))
        # 
        db_session.commit()
        print(str(registered_user)+'Это зарегистрированный пользователь')
        # return redirect(url_for('sms_shield',username = registered_user.username))
        return "True"

@app.route('/sms_shield?<username>')
def sms_shield(username):
    if request.method == 'GET':
        print('66 Я тут, я получил',username)   
        return render_template('sms.html',username=username)

@limiter.limit("100/day;10/hour;3/minute")
@app.route('/sms_detected',methods=['POST'])
def sms_detected():
    sms = request.form['sms']
    try:
        print(session[sms])
        user = User.query.filter(User.username == session[sms]).first()
        if user is not None:
            user.sms = ""
            login_user(user)
            db_session.commit()
            return "True"
        else:
            raise KeyError('non-alphanumeric character in input')
    except KeyError :
        flash('Введены ошибочные данные. Попробуйте ещё раз')
        # return render_template('sms.html')
        return "False"

@app.route('/index/<username>')
@login_required
def index(username):
    user = User.query.filter(User.username == username).first()
    return jsonify(user = user.username,account = user.account)

@app.route('/i')
def i():
    return jsonify('hello!')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# app.run(ssl_context=context,threaded=True,debug = True, use_reloader=False,host='10.42.0.1')
app.run(ssl_context=context,threaded=True,debug = True, use_reloader=False,host='192.168.43.233')