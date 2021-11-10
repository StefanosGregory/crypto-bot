from conn import create_connection


class Favorites:
    def __init__(self, coin_symbol, starter_price):
        self.coin_symbol = coin_symbol
        self.starter_price = starter_price

    def __repr__(self):
        return '<symbol: %r>' % self.coin_symbol


def insert_symbols(symbol, current_price):
    conn = create_connection()
    with conn:
        sql = ''' INSERT INTO symbols(symbol,current_price) VALUES(?,?) '''
        data_tuple = (symbol, current_price)
        cur = conn.cursor()
        cur.execute(sql, data_tuple)
        conn.commit()
    conn.close()


def select_favorites():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM favorites")

    rows = cur.fetchall()

    favorites = []

    for row in rows:
        favorites.append(Favorites(coin_symbol=row[1], starter_price=row[2]))

    return favorites


def select_all():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM symbols")

    rows = cur.fetchall()

    symbols = []

    for row in rows:
        symbols.append(Favorites(coin_symbol=row[1], starter_price=row[2]))

    return symbols
