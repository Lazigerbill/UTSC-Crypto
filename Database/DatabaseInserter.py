
def insert_new_wl(cursor, connection, name):
    # insert row into WL
    cursor.execute("""INSERT INTO WL (WlName) VALUES (%s)""", (name))
    connection.commit()
    return


def insert_new_stock(cursor, connection, ticker):
    cursor.execute("""INSERT INTO Stock (Ticker) VALUES (%s)""", (ticker))
    connection.commit()
    return


def insert_new_wlcontents(cursor, connection, wlId, stockId, ticker):
    insertion = ("INSERT INTO WLContents (wlId, stockId, Ticker) "
                 "VALUES (%s, %s, %s)")
    data = (wlId, stockId, ticker)
    cursor.execute(insertion, data)
    connection.commit()
    return
