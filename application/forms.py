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
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_verif = PasswordField('Re-enter Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):        
        if not (re.search(r"(/^[A-Za-z0-9]+(?:[ _-][A-Za-z0-9]+)*$/')", username)):
            raise ValidationError("Allowed special characters are underscore and hyphen.")
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('That username is already taken.') 
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('There is an existing account with the specified mail address.')

class PasswordResetForm(FlaskForm):
    userinf = StringField('Enter your username or email:', validators =[DataRequired()])
    #reset_by shows what the user is using to reset their password. Its value is either 'username' or 'email'
    reset_by = ''
        
    def validate_reset_by(self, userinf):  
        if userinf is not Null:       
            if "@" in userinf:
                reset_by = 'email'
                SignupForm.validate_email(userinf)
            else:
                reset_by = 'username'
                SignupForm.validate_username(userinf)
    


