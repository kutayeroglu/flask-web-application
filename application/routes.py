from flask import render_template, flash, redirect 
from application import app 
from application.forms import LoginForm


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
    beta_login_form = LoginForm()  
    if beta_login_form.validate_on_submit():
        flash("Data requested for {}, remember me status = {}".format(
            beta_login_form.username.data, beta_login_form.remember_me.data ))
        return redirect('/index')      
    return render_template('login.html', title = 'Sign In', form=beta_login_form)
    