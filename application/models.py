from datetime import datetime 
from hashlib import md5 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import db, login_manager 

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    actions = db.relationship('Action', backref = 'actor', lazy = 'dynamic')
    last_seen = db.Column(db.String(128), index = True, default = datetime.now(tz=None).isoformat(timespec='seconds'))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    #d=identicon makes avatar different for users   
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()   
        return 'http://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest,size)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_text = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Action {}>'.format(self.random_text)
        
 
     

""""
class Action_document 


        {
            "type": "UserCreatedEvent",
            "document": {   
                "username": "yorogx",
                "email": "ismet@mail.com",
                "a": "b"
            },
            "prior": {
            },
            "sys": {
                "created_at": "2020-08-04T23:22:11.000Z",
                "created_by": "system"
            }
        }

        {
            "type": "UserUpdatedEvent",
            "document": {
                "username": "ismetacar",
                "email": "ismet@mail.com",
                "a": "b"
            },
            "prior": {
                "username": "yorogx",
                "email": "ismet@mail.com",
                "a": "b"
            },
            "sys": {
                "created_at": "2020-08-01T23:22:11.000Z",
                "created_by": "system"
            }
        }
"""


