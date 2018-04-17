from Database import DatabaseSelector


def insert_new_wl(connection, name):
    cursor = connection.cursor()
    # insert row into WL
    cursor.execute("""INSERT INTO WL (WlName) VALUES (%s)""", name)
    connection.commit()
    cursor.close()
    return


def insert_new_stock(connection, ticker):
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO Stock (Ticker) VALUES (%s)""", ticker)
    connection.commit()
    cursor.close()
    return

# WHERE NOT EXISTS (SELECT Ticker FROM Stock  WHERE Ticker LIKE (%s)),


def insert_new_wlcontents(connection, wlId, ticker):
    cursor = connection.cursor()
    stockId = DatabaseSelector.get_stock_id(connection, ticker)
    insertion = ("INSERT INTO WLContents (wlId, stockId, Ticker) "
                 "VALUES (%s, %s, %s)")
    data = (wlId, stockId[0], ticker)
    cursor.execute(insertion, data)
    connection.commit()
    cursor.close()
    return


