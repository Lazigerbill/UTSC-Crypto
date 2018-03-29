def get_wl(cursor, connection, name):
    # select WL if it exists
    cursor.execute("""SELECT * FROM WL WHERE WlName LIKE (%s) """, name)
    connection.commit()
    return cursor.fetchall()


def get_wl_for_user(cursor, connection, wlname, wlid):
    selection = ("""SELECT * FROM WL WHERE WlId LIKE """ + str(wlid) + """ AND WlName LIKE (%s) """)
    cursor.execute(selection, wlname)
    connection.commit()
    return cursor.fetchall()


def get_user_stock_data(cursor, connection, wlname, watchlistid):
    # if user does not have a watchlist with that id return 0
    if len(get_wl_for_user(cursor, connection, wlname, watchlistid)) == 0:
        return 0
    else:
        cursor.execute("""SELECT * FROM WLContents WHERE WlId LIKE (%s) """, watchlistid)
        connection.commit()
        return cursor.fetchall()


def delete_stock_from_wl(cursor, connection, watchlistid, ticker):
    # if none does not exist
    deletion = ("""DELETE FROM WLContents WHERE WlId LIKE """ + str(watchlistid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(deletion, ticker)
    connection.commit()
    return cursor.fetchall()

def get_stock(cursor, connection, ticker):
    cursor.execute("""SELECT * FROM Stock WHERE Ticker LIKE (%s) """, ticker)
    connection.commit()
    return cursor.fetchall()


def get_stock_id(cursor, connection, ticker):
    cursor.execute("""SELECT StockId FROM Stock WHERE Ticker LIKE (%s) """, ticker)
    connection.commit()
    return cursor.fetchall()


def get_stock_from_wl(cursor, connection, wlid, ticker):
    selection = ("""SELECT * FROM WLContents WHERE WlId LIKE """ + str(wlid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(selection, ticker)
    connection.commit()
    return cursor.fetchall()