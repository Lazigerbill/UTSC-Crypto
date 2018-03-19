from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from Database import DatabaseDriver, DatabaseInserter, DatabaseSelector
from static.Forms.forms import WatchListForm, WatchListContentsForm, AddStockForm

# launching the app
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# connecting to MYSQL server
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'financelab'
app.config['MYSQL_DATABASE_PASSWORD'] = 'equity123'
app.config['MYSQL_DATABASE_DB'] = 'sys'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

# creating or connecting database
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
DatabaseInserter.insert_new_wlcontents(cursor, conn, 1, "AAPL")
DatabaseInserter.insert_new_stock(cursor, conn, "Bad")
var = DatabaseSelector.get_stock_id(cursor, conn, "Bad")


@app.route('/', methods=('GET', 'POST'))
def submit():
    form = WatchListForm()
    if form.validate_on_submit():
        wlname = request.form['WlName']
        data = DatabaseSelector.get_wl(cursor, conn, wlname)
        if len(DatabaseSelector.get_wl(cursor, conn, wlname)) == 0:
            DatabaseInserter.insert_new_wl(cursor, conn, wlname)
        form1 = WatchListContentsForm()
        return render_template('showwatchlist.html', data=data, form1=form1)
    return render_template('showform.html', form=form)


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/showwatchlist.html', methods=('GET', 'POST'))
def showwatchlist():
    form = WatchListContentsForm()
    if form.validate_on_submit():
        wlid = request.form['WlId']
        data = DatabaseSelector.get_user_stock_data(cursor, conn, wlid)
        form2 = AddStockForm
        return render_template('contents.html', data=data, form2=form2)


@app.route('/contents.html', methods=('GET', 'POST'))
def contents():
    data = DatabaseSelector.get_user_stock_data(cursor, conn, wlid)
    form = AddStockForm()
    if form.validate_on_submit():
        Ticker = request.form['Ticker']
        if len(DatabaseSelector.get_stock(cursor, conn, Ticker)) == 0:
            DatabaseInserter.insert_new_stock(cursor, conn, Ticker)
            DatabaseInserter. insert_new_wlcontents(cursor, conn, wlId, Ticker)
            return render_template('contents.html', data=data, form=form)
        else:
            DatabaseInserter. insert_new_wlcontents(cursor, connection, wlId, Ticker)
            return render_template('contents.html', data=data, form=form)
    return render_template('contents.html', data=data, form=form)

"""@app.route(/contents.html', methods=('GET', 'POST'))
def contents_add_stock(wlid):
    form = AddStockForm()
    if form.validate_on_submit():
        Ticker = request.form['Ticker']
        data = DatabaseSelector.get_user_stock_data(cursor, conn, wlid)
        if len(DatabaseSelector.get_stock(cursor, conn, Ticker)) == 0:
            DatabaseInserter.insert_new_stock(cursor, connection, Ticker)
            DatabaseInserter. insert_new_wlcontents(cursor, connection, wlId, Ticker)
             return render_template again
        else:
            DatabaseInserter. insert_new_wlcontents(cursor, connection, wlId, Ticker)
            return render_template
        """

if __name__ == '__main__':
    app.run()
