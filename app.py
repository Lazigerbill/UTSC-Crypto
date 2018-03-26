from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from Database import DatabaseDriver, DatabaseInserter, DatabaseSelector, DatabaseDeleter
from static.Forms.forms import WatchListForm, WatchListContentsForm, StockForm

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

# DatabaseInserter.insert_new_stock(cursor, conn, "AAPL")
# DatabaseInserter.insert_new_wl(cursor, conn, "Brady")
# DatabaseInserter.insert_new_wlcontents(cursor, conn, 1, "AAPL")


@app.route('/')
def start():
    return redirect(url_for('submit'))


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = WatchListForm()
    if form.validate_on_submit():
        wlname = request.form['WlName']
        if len(DatabaseSelector.get_wl(cursor, conn, wlname)) == 0:
            DatabaseInserter.insert_new_wl(cursor, conn, wlname)
        return redirect(url_for('handle_data', wlName=wlname))
    return render_template('showform.html', form=form)


@app.route('/<wlName>', methods=['GET', 'POST'])
def handle_data(wlName):
    data = DatabaseSelector.get_wl(cursor, conn, wlName)
    form = WatchListContentsForm()
    if form.validate_on_submit():
        wlid = request.form['WlId']
        return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlid))
    return render_template('showwatchlist.html', form=form, data=data, wlName=wlName)


@app.route('/<wlName>/<wlId>', methods=['GET', 'POST'])
def show_watchlist(wlName, wlId):
    data = DatabaseSelector.get_user_stock_data(cursor, conn, wlId)
    form = StockForm()
    if form.validate_on_submit() and form.data.get('Add'):
        ticker = request.form['Ticker']
        if len(DatabaseSelector.get_stock(cursor, conn, ticker)) == 0:
            DatabaseInserter.insert_new_stock(cursor, conn, ticker)
            DatabaseInserter. insert_new_wlcontents(cursor, conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        else:
            DatabaseInserter. insert_new_wlcontents(cursor, conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
    if form.validate_on_submit() and form.data.get('Delete'):
        ticker = request.form['Ticker']
        if len(DatabaseSelector.get_stock(cursor, conn, ticker)) == 0:
            # Should notify user, that stock does not exist in your watchlist!
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        else:
            DatabaseDeleter.delete_stock_from_wl(cursor, conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
    return render_template('contents.html', form=form, data=data, wlName=wlName, wlId=wlId)


if __name__ == '__main__':
    app.run()
