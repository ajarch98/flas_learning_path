import os

class Config(object):
    """Contains configuration variables for Flask app"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you-will-never-guess"
