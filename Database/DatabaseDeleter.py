from Database import DatabaseSelector


def delete_stock_from_wl(cursor, connection, watchlistid, ticker):
    # if none does not exist
    deletion = ("""DELETE FROM WLContents WHERE WlId LIKE """ + str(watchlistid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(deletion, ticker)
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
