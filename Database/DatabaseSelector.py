def get_wl(cursor, connection, name):
    # select WL if it exists
    cursor.execute("""SELECT * FROM WL WHERE WlName LIKE (%s) """, name)
    connection.commit()
    return cursor.fetchall()


def get_stock_data(cursor, connection):
    cursor.execute("""SELECT * FROM STOCK """)

