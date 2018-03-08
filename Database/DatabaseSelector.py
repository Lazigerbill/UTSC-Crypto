def get_wl(cursor, connection):
    # insert row into WL
    cursor.execute("""SELECT * FROM WLCONTENTS""")
    connection.commit()
    return
