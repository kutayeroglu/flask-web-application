from datetime import datetime 
from application import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    actions = db.relationship('Action', backref = 'actor', lazy = 'dynamic')
    
class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    random_text = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Action {}>'.format(self.random_text)