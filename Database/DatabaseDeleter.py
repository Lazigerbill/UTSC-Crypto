from Database import DatabaseSelector


def delete_stock_from_wl(connection, watchlistid, ticker):
    cursor = connection.cursor()
    # if none does not exist
    deletion = ("""DELETE FROM WLContents WHERE WlId LIKE """ + str(watchlistid) + """ AND Ticker LIKE (%s) """)
    cursor.execute(deletion, ticker)
    connection.commit()
    return cursor.fetchall()