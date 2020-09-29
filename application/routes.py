from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse  
from flask_login import current_user, login_user, logout_user, login_required
from application import app, db
from application.forms import LoginForm, SignupForm
from application.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', credentials = groupx_credentials )
    
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
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)        
    return render_template('login.html', title = 'Sign In', form=beta_login_form)
    
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/signup', methods = ["POST", "GET"])
def signup(): 
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    beta_signup_form = SignupForm()
    if beta_signup_form.validate_on_submit():
        userx = User(username = beta_signup_form.username.data, email=beta_signup_form.email.data)
        userx.set_password(beta_signup_form.password.data)
        db.session.add(userx)
        db.session.commit()
        flash('Hooray! Your account is successfully created.')
        return redirect(url_for('login'))
    return render_template('signup.html', title = "Sign up", form = beta_signup_form)
    
    
@app.route('/<username>')
@login_required
def user(username):
    #Using first_or_404 to prevent crashes if the user is not found. 
    current_user = User.query.filter_by(username=username).first_or_404()
    actions = [
        {  'actor' : current_user, 'body' : 'random text #1 '  },
        {  'actor' : current_user, 'body' : 'random text #2' }
    ]
    return render_template('profile.html', current_user=current_user, actions=actions)
    


    