from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from Database import DatabaseDriver, DatabaseInserter, DatabaseSelector
from static.Forms.forms import TickerForm

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'equity123'
app.config['MYSQL_DATABASE_DB'] = 'sys'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()
database_connected = DatabaseDriver.create_database(cursor, conn)
if database_connected is not None:
    DatabaseDriver.initialize_database(cursor, conn)
    print("Success")
else:
    print("Failure")

DatabaseInserter.insert_new_stock(cursor, conn, "AAPL")
DatabaseInserter.insert_new_wl(cursor, conn, "Brady")
DatabaseInserter.insert_new_wlcontents(cursor, conn, 1, 1, "AAPL")


@app.route('/showform.html', methods=('GET', 'POST'))
def submit():
    form = TickerForm()
    if form.validate_on_submit():
        return redirect('/index.html')
    return render_template('showform.html', form=form)