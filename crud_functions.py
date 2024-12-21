import sqlite3


def initiate_db():
    connection = sqlite3.connect("prod_base.db")
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY, 
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    for i in range(1,5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i, f"Продукт {i}", f"Описание {i}", f" {i * 100}"))
    connection.commit()
    connection.close()


def get_all_products(id, title, description):
    connection = sqlite3.connect("prod_base.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
    connection.commit()
    prod = cursor.fetchall()
    id, title, description, price = prod[0]
    return f"Название: {title} | Описание: {description} | Цена: {price}"
    connection.close()