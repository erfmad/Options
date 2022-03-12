import sqlite3

connection = sqlite3.connect('app.db')

cursor = connection.cursor()

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS stock (
        id INTIGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL);
    );



    CREATE TABLE IF NOT EXISTS stock_price (
        id intiger primary key,
        stock_id intiger,
        date not null,
        open not null,
        high not null,
        low not null,
        close not null,
        adjusted_close not null,
        volume not null,
        foreign key (stock_id) references stock (id)
    );
""")

connection.commit()
