from app import App

#imports below required for shell_context_processor
from app import db
from app.models import User, Post

@App.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}
