from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from Database import DatabaseDriver, DatabaseInserter, DatabaseSelector, DatabaseDeleter
from static.Forms.forms import WatchListForm, WatchListContentsForm, StockForm
from testapi import lastDict, volumeDict, percentchangeDict, getUrl
import os


# launching the app
app = Flask(__name__)
# connecting to MYSQL server
mysql = MySQL()
# loading keys from config file
# use heroku config if in production
is_prod = os.environ.get('IS_HEROKU', None)
if not is_prod:
    app.config.from_pyfile('instance/config_file.pyc', silent=True)
    mysql.init_app(app)
    # creating or connecting database
    conn = mysql.connect()
    cursor = conn.cursor()
    database_connected = DatabaseDriver.create_database(cursor, conn)
else:
    app = os.environ.get('FLASK_APP')
    mysql.init_app(app)
    # creating or connecting database
    conn = mysql.connect()
    cursor = conn.cursor()
    database_connected = DatabaseDriver.use_heroku_database(cursor, conn)
if database_connected is not None:
    DatabaseDriver.initialize_database(cursor, conn)
    print("Success")
else:
    print("Failure")


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
    return render_template('index.html', form=form)


@app.route('/<wlName>', methods=['GET', 'POST'])
def handle_data(wlName):
    # check if user tries to enter name that does not exist in url
    if len(DatabaseSelector.get_wl(cursor, conn, wlName)) == 0:
        return redirect(url_for('submit'))

    # get user watchlist and if wlId is valid return view of watchlist
    data = DatabaseSelector.get_wl(cursor, conn, wlName)
    form = WatchListContentsForm()
    if form.validate_on_submit():
        wlid = request.form['WlId']
        check = DatabaseSelector.get_wl_for_user(cursor, conn, wlName, wlid)
        if len(check) == 0:
            return redirect(url_for('handle_data', wlName=wlName))
        return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlid))
    return render_template('showwatchlist.html', form=form, data=data, wlName=wlName)


@app.route('/<wlName>/<wlId>', methods=['GET', 'POST'])
def show_watchlist(wlName, wlId):
    data = DatabaseSelector.get_user_stock_data(cursor, conn, wlName, wlId)
    if data == 0:
        return redirect(url_for('handle_data', wlName=wlName))
    form = StockForm()
    if form.validate_on_submit():
        ticker = request.form['Ticker']
        # check if user has stock in watchlist
        man = DatabaseSelector.get_stock_from_wl(cursor, conn, wlId, ticker)
        if len(man) != 0:
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        # check if stock exists in database, if not add
        if len(DatabaseSelector.get_stock(cursor, conn, ticker)) == 0:
            DatabaseInserter.insert_new_stock(cursor, conn, ticker)
            DatabaseInserter. insert_new_wlcontents(cursor, conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        # add to user watchlist
        else:
            DatabaseInserter. insert_new_wlcontents(cursor, conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))

    # initialize 3 dictionaries for fields from API
    pcDict = percentchangeDict()
    volDict = volumeDict()
    priceDict = lastDict()

    # loop through watchlist and add fields to dict and send dict to html
    for row in data:
        pcDict[row[2]] = getUrl(row[2]).get('PercentChangeFromPreviousClose')
        volDict[row[2]] = getUrl(row[2]).get('Volume')
        priceDict[row[2]] = getUrl(row[2]).get('Last')
    keys = list(volDict.keys())
    return render_template('contents.html', form=form, percentagechangeDict=pcDict,
                           volumeDict=volDict, lastDict=priceDict, keys=keys, wlName=wlName, wlId=wlId)


@app.route('/delete_row/<wlName>/<wlId>/<ticker>', methods=['GET', 'POST'])
def delete_row(wlName, wlId, ticker):
    if request.method == 'POST':
        # delete row from table
        DatabaseDeleter.delete_stock_from_wl(cursor, conn, wlId, ticker)
    return redirect(url_for('show_watchlist', wlId=wlId, wlName=wlName))


@app.route('/new_watchlist/<wlName>', methods=['GET', 'POST'])
def new_watchlist(wlName):
    if request.method == 'POST':
        # create a new watchlist for user
        DatabaseInserter.insert_new_wl(cursor, conn, wlName)
    return redirect(url_for('handle_data', wlName=wlName))


if __name__ == '__main__':
    app.run()
