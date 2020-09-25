from flask import Flask   
from config import Configure   
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configure)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

from application import routes, models 