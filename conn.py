import sqlite3
from aifc import Error


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('DB/database.db')
    except Error as e:
        print(e)

    return conn
