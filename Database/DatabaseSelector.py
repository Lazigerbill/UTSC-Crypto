def get_wl(cursor, connection, name):
    # select WL if it exists
    cursor.execute("""SELECT * FROM WL WHERE WlName LIKE (%s) """, name)
    connection.commit()
    return cursor.fetchall()


def get_user_stock_data(cursor, connection, watchlistid):
    cursor.execute("""SELECT * FROM WLContents WHERE WlId LIKE (%s) """, watchlistid)
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
