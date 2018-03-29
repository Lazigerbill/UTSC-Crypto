Place file called "config.py" in this folder and add the following code filling in the required passwords and keys
where necessary:

from app import app
app.config.update(dict(
    SECRET_KEY="",
    WTF_CSRF_SECRET_KEY=""
))
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''