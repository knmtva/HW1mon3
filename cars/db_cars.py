import sqlite3
from pathlib import Path

def init1():
    DB_NAME = 'd.sqlite3'
    DB_PATH = Path(__file__).parent.parent
    global db
    global cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()

def create_tables1():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dictionary (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price TEXT,
        description TEXT,
        link TEXT UNIQUE
    )
    """)
    db.commit()


def populate_cars(spisok):
    for item in spisok:
        cur.execute("""
        INSERT OR IGNORE INTO dictionary (name, price, description, link)
        VALUES (?, ?, ?, ?)
        """, (item['name'], item["price"], item["description"], item["link"]))


    db.commit()


def get_data():
    cur.execute(
        '''
        SELECT * FROM dictionary
        '''
    )
    return cur.fetchall()
