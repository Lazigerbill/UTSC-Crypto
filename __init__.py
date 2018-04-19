from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from Database import DatabaseDriver, DatabaseInserter, DatabaseSelector, DatabaseDeleter
from static.Forms.forms import WatchListForm, StockForm
from xignite import lastDict, volumeDict, percentchangeDict, getUrl, getTime
import os


# launching the app
app = Flask(__name__)
# connecting to MYSQL server
mysql = MySQL()
is_prod = os.environ.get('IS_HEROKU', None)
# if not running production code, use local config keys from file and local db
if not is_prod:
    app.config.from_pyfile('instance/config_file.pyc', silent=True)
    mysql.init_app(app)
    # creating or connecting database
    conn = mysql.connect()
    database_connected = DatabaseDriver.create_database(conn)
# if running production code, use config codes from class anf connect to cleardb database
else:
    app.config.from_object('prodconfig.ProductionConfig')
    mysql.init_app(app)
    # creating or connecting database
    conn = mysql.connect()
    database_connected = DatabaseDriver.use_heroku_database(conn)
if database_connected is not None:
    DatabaseDriver.initialize_database(conn)
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
        conn = mysql.connect()
        # if user does not have a watchlist, create a new one
        if len(DatabaseSelector.get_wl(conn, wlname)) == 0:
            DatabaseInserter.insert_new_wl(conn, wlname)
        return redirect(url_for('handle_data', wlName=wlname))
    return render_template('index.html', form=form)


@app.route('/<wlName>', methods=['GET', 'POST'])
def handle_data(wlName):
    # check if user tries to enter name that does not exist in url
    data = DatabaseSelector.get_wl(conn, wlName)
    if len(data) == 0:
        return redirect(url_for('submit'))
    # return list of user watchlists
    return render_template('showwatchlist.html', data=data, wlName=wlName)


@app.route('/<wlName>/<wlId>', methods=['GET', 'POST'])
def show_watchlist(wlName, wlId):
    data = DatabaseSelector.get_user_stock_data(conn, wlName, wlId)
    if data == 0:
        return redirect(url_for('handle_data', wlName=wlName))
    form = StockForm()
    if form.validate_on_submit():
        ticker = request.form['Ticker']
        # check if user has stock in watchlist
        man = DatabaseSelector.get_stock_from_wl(conn, wlId, ticker)
        if len(man) != 0:
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        # check if stock exists in database, if not add
        if len(DatabaseSelector.get_stock(conn, ticker)) == 0:
            DatabaseInserter.insert_new_stock(conn, ticker)
            DatabaseInserter. insert_new_wlcontents(conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))
        # add to user watchlist
        else:
            DatabaseInserter. insert_new_wlcontents(conn, wlId, ticker)
            return redirect(url_for('show_watchlist', wlName=wlName, wlId=wlId))

    # initialize 3 dictionaries for fields from API
    pcDict = percentchangeDict()
    volDict = volumeDict()
    priceDict = lastDict()
    # loop through watchlist and add fields to dict and send dict to html
    for row in data:
        pcDict[row[2]] = getUrl(row[2]).get('PercentChangeFromPreviousClose')
        volDict[row[2]] = round(getUrl(row[2]).get('Volume'))
        priceDict[row[2]] = getUrl(row[2]).get('Last')
    keys = list(volDict.keys())
    time = getTime()
    return render_template('contents.html', form=form, percentagechangeDict=pcDict,
                           volumeDict=volDict, lastDict=priceDict, keys=keys, wlName=wlName, wlId=wlId, time=time)


@app.route('/delete_row/<wlName>/<wlId>/<ticker>', methods=['GET', 'POST'])
def delete_row(wlName, wlId, ticker):
    if request.method == 'POST':
        # delete row from table
        DatabaseDeleter.delete_stock_from_wl(conn, wlId, ticker)
    return redirect(url_for('show_watchlist', wlId=wlId, wlName=wlName))


@app.route('/new_watchlist/<wlName>', methods=['GET', 'POST'])
def new_watchlist(wlName):
    if request.method == 'POST':
        # create a new watchlist for user
        DatabaseInserter.insert_new_wl(conn, wlName)
    return redirect(url_for('handle_data', wlName=wlName))


if __name__ == '__main__':
    app.run()
