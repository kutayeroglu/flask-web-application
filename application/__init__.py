from flask import Flask   
from config import Configure   
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 


app = Flask(__name__)
app.config.from_object(Configure)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from application import routes, models 