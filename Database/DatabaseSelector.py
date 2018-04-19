def get_wl(connection, name):
    # select WL if it exists
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM WL WHERE WlName LIKE (%s) """, name)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results


def get_wl_for_user(connection, wlname, wlid):
    cursor = connection.cursor()
    selection = ("""SELECT * FROM WL WHERE WlId LIKE """ + str(wlid) + """ AND WlName LIKE (%s) """)
    cursor.execute(selection, wlname)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results


def get_user_stock_data(connection, wlname, watchlistid):
    cursor = connection.cursor()
    # check if watchlistid is not a number
    if not str(watchlistid).isnumeric():
        cursor.close()
        return 0
    # if user does not have a watchlist with that id return 0
    if len(get_wl_for_user(connection, wlname, watchlistid)) == 0:
        cursor.close()
        return 0
    else:
        cursor.execute("""SELECT * FROM WLContents WHERE WlId LIKE (%s) """, watchlistid)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()
        return results


def delete_stock_from_wl(connection, watchlistid, ticker):
    cursor = connection.cursor()
    # if none does not exist
    deletion = ("""DELETE FROM WLContents WHERE WlId LIKE """ + str(watchlistid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(deletion, ticker)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results

def get_stock(connection, ticker):
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM Stock WHERE Ticker LIKE (%s) """, ticker)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results


def get_stock_id(connection, ticker):
    cursor = connection.cursor()
    cursor.execute("""SELECT StockId FROM Stock WHERE Ticker LIKE (%s) """, ticker)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results


def get_stock_from_wl(connection, wlid, ticker):
    cursor = connection.cursor()
    selection = ("""SELECT * FROM WLContents WHERE WlId LIKE """ + str(wlid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(selection, ticker)
    connection.commit()
    results = cursor.fetchall()
    cursor.close()
    return results
