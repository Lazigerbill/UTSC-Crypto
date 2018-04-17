
def create_database(cursor, connection):
    # create database
    cursor.execute("""CREATE DATABASE IF NOT EXISTS financelab""")
    connection.commit()
    # use database
    cursor.execute("""USE financelab""")
    connection.commit()
    return True


def use_heroku_database(cursor, connection):
    cursor.execute("""USE heroku_c7237869c2e3db0""")
    connection.commit()
    return True

def initialize_database(cursor, connection):
    # create WL table
    cursor.execute("""CREATE TABLE IF NOT EXISTS WL(
    WlId INT NOT NULL AUTO_INCREMENT,
    WlName TEXT,
    PRIMARY KEY (WlId))""")
    connection.commit()

    # create Stock table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Stock(
    StockId INT NOT NULL AUTO_INCREMENT,
    Ticker TEXT,
    PRIMARY KEY (StockId))""")
    connection.commit()

    # create WLContents table
    cursor.execute("""CREATE TABLE IF NOT EXISTS WLContents(
    WlId INT,
    StockId INT NOT NULL,
    Ticker TEXT, 
    FOREIGN KEY(WlId) REFERENCES WL(WlId),
    FOREIGN KEY(StockId) REFERENCES Stock(StockId))""")
    connection.commit()
    return
