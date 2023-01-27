import sqlite3
from pathlib import Path
def init():
    DB_NAME = 'db.sqlite3'
    DB_PATH = Path(__file__).parent.parent
    global db, cur
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cur = db.cursor()

def create_tables():


    cur.execute(
        """CREATE TABLE IF NOT EXISTS products
        (product_id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT,
        price INTEGER,
        photo TEXT)"""
    )
    db.commit()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders
        (order_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        region TEXT,
        product_id INTEGER,
        FOREIGN KEY (product_id)
        REFERENCES products (product_id)
        ON DELETE CASCADE)"""
    )

    db.commit()


def populate_products():
    cur.execute("""INSERT INTO products (
        name,
        description,
        price,
        photo
    ) VALUES
    ('Цезарь', 'вкусный салат', 350, './media/zez.jpg'),
    ('Оливье', 'новогодний салат', 260, './media/olivie.jpg'),
    ('Коктейль Мимоза', 'Апельсиновый коктейль самое то для тебя :), сладкое как и ты', 500, './media/mimoza.jpg'),
    ('Голубая лагуна', 'Освежающий коктейль для отличного вечера', 450, './media/blue.jpg')
    """)
    db.commit()


def get_products():
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()
    # cyr = cur.execute("""SELECT * FROM products""")
    # return tuple(cyr)


def create_order(data):
    data = data.as_dict()
    cur.execute("""INSERT INTO orders (
        name,
        age,
        gender,
        region,
        product_id
    )VALUES (:name, :age, :gender, :region, :product_id)""",
                {'name': data['name'],
                 'age': data['age'],
                 'gender': data['gender'],
                 'region': data['region'],
                 'product_id': data['product_id']})
    db.commit()

init()
create_tables()
# populate_products()

