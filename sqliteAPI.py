from application import app, db
from application.models import User, Action 

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'user' : User, 'action': Action}
