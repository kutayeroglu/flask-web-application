import re 
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from application.models import User  

class LoginForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_verif = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        if not re.search(r"^(?=.{4,20}$)(?![_.])[a-zA-Z0-9._]+(?<![_.])$", username.data):
            raise ValidationError("Unallowed characters in username.")
            
    def validate_email(self, email):
        if not re.search(r'[\w\.-]+@[\w\.-]+', email.data):
            raise ValidationError("Email address not correct.")
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('There is an existing account with the specified mail address.')
        

class PasswordResetForm(FlaskForm):
    userinf = StringField('Enter username or email:', validators =[DataRequired()])
    submit = SubmitField('Change Password')
        
    def validate_userinf(self, userinf):  
        if userinf is not None:       
            if "@" in str(userinf):
                '''
                If there is a @ in the email, we know user is resetting by email. Because only "_" and "." are the allowed 
                special characters in usernames.
                '''
                SignupForm.validate_email(PasswordResetForm, userinf)
            else:
                SignupForm.validate_username(PasswordResetForm, userinf)
        else: 
            raise ValidationError("You can't leave this field empty.")


