
def create_database(connection):
    cursor = connection.cursor()
    # create local database
    cursor.execute("""CREATE DATABASE IF NOT EXISTS financelab""")
    connection.commit()
    # use local database
    cursor.execute("""USE financelab""")
    connection.commit()
    cursor.close()
    return True


def use_heroku_database(connection):
    # specify we are using the clearDB
    cursor = connection.cursor()
    cursor.execute("""USE heroku_c7237869c2e3db0""")
    connection.commit()
    cursor.close()
    return True


def initialize_database(connection):
    cursor = connection.cursor()
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
    cursor.close()
    return
