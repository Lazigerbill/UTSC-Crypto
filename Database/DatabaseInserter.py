from Database import DatabaseSelector


def insert_new_wl(cursor, connection, name):
    # insert row into WL
    cursor.execute("""INSERT INTO WL (WlName) VALUES (%s)""", name)
    connection.commit()
    return


def insert_new_stock(cursor, connection, ticker):
    cursor.execute("""INSERT INTO Stock (Ticker) VALUES (%s)""", ticker)
    connection.commit()
    return

# WHERE NOT EXISTS (SELECT Ticker FROM Stock  WHERE Ticker LIKE (%s)),


def insert_new_wlcontents(cursor, connection, wlId, ticker):
    stockId = DatabaseSelector.get_stock_id(cursor, connection, ticker)
    insertion = ("INSERT INTO WLContents (wlId, stockId, Ticker) "
                 "VALUES (%s, %s, %s)")
    data = (wlId, stockId[0], ticker)
    cursor.execute(insertion, data)
    connection.commit()
    return


