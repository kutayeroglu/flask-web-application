from application import app, db
from application.models import User, Action 

#: @app.shell_context_processor
#: def make_shell_context():
#:     return {'db' : db, 'user' : User, 'action': Action}
#:

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)