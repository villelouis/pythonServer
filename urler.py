# from flask import Flask, session, redirect, url_for, escape, request
# import os
# # from models import User
# from database import db_session

# # from runapp import app


# # import runapp
# from runapp import app
# ===================================================================================



# from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
# from flask.ext.login import login_user , logout_user , current_user , login_required
 
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     username = request.form['username']
#     password = request.form['password']
#     registered_user = User.query.filter_by(username=username,password=password).first()
#     if registered_user is None:
#         flash('Username or Password is invalid' , 'error')
#         return redirect(url_for('login'))
#     login_user(registered_user)
#     flash('Logged in successfully')
#     return redirect(request.args.get('next') or url_for('index'))

# ====================================================================================

# print('Hello from URLER')

# app.run(ssl_context=context,threaded=True,debug = True, use_reloader=False)
