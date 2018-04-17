import os


class ProductionConfig:
    MYSQL_DATABASE_DB = os.environ['MYSQL_DATABASE_DB']
    MYSQL_DATABASE_HOST = os.environ['MYSQL_DATABASE_HOST']
    MYSQL_DATABASE_PASSWORD = os.environ['MYSQL_DATABASE_PASSWORD']
    MYSQL_DATABASE_USER = os.environ['MYSQL_DATABASE_USER']
    SECRET_KEY = os.environ['SECRET_KEY']
    WTF_CSRF_SECRET_KEY = os.environ['acsrfsecretkey']