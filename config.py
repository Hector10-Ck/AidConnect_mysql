import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    # MySQL connection (user provided: root:12345 on localhost)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://root:12345@localhost/aidconnect_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
