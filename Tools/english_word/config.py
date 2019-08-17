import os
from datetime import timedelta


client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

SECRET_KEY = os.urandom(24)
SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
PERMANENT_SESSION_LIFETIME = timedelta(days = 365)
GITHUB_CLIENT_ID = client_id
GITHUB_CLIENT_SECRET = client_secret
"""
SQLALCHEMY_DATABASE_URI = 'sqlite:///words.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_BINDS = {
    'wrongwords': 'sqlite:///wrongwords.sqlite3',
    "users": "sqlite:///users.sqlite3"
}
"""
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_BINDS = {
    'wrongwords': os.environ["HEROKU_POSTGRESQL_AMBER_URL"],
    "github-users": os.environ["HEROKU_POSTGRESQL_NAVY_URL"],
    "admin-users": os.environ["HEROKU_POSTGRESQL_ROSE_URL"]
}