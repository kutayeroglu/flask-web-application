import os 

class Configure(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2x5lomn75'
