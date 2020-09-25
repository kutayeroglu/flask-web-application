from flask import render_template, flash, redirect, url_for 
from flask_login import current_user, login_user
from application import app 
from application.forms import LoginForm
from application.models import User

@app.route('/')
@app.route('/index')
def index():
    random_user = {'username' : 'kutay '}
    groupx_credentials = [
        {
            'user_cred' : { 'username' : 'yorgox'},
            'last_login' : '12-12-2019'
        }, 
        
        {
            'user_cred' : { 'username' : 'calisanabasari'},
            'last_login' : '12-12-2007'
        }
    ]
    return render_template('index.html', title='Home', user=random_user, credentials = groupx_credentials )
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    beta_login_form = LoginForm()  
    if beta_login_form.validate_on_submit():
        userx = User.query.filter_by(username=beta_login_form.username.data).first()
        if userx is None or not userx.check_password(beta_login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(userx, remember = beta_login_form.remember_me.data)
        return redirect(url_for('index'))      
    return render_template('login.html', title = 'Sign In', form=beta_login_form)
    