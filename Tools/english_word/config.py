import os
from datetime import timedelta


SECRET_KEY = os.urandom(24)
SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
PERMANENT_SESSION_LIFETIME = timedelta(days = 365)
SQLALCHEMY_DATABASE_URI = 'sqlite:///words.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_BINDS = {
    'wrongwords': 'sqlite:///wrongwords.sqlite3'
}