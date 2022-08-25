import sqlite3 as sq

db = sq.connect('cinema.db')
cur = db.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS customers(
            login TEXT, 
            customer_name TEXT, 
            surname TEXT, 
            age TEXT, 
            email TEXT, 
            orders TEXT
            )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS halls(
            hall_name TEXT,
            economy TEXT,
            comfort TEXT,
            vip TEXT,
            cinemas TEXT
            )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS cinemas(
            film_name TEXT,
            sch_time TEXT,
            hall TEXT
            )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS workers(
            worker_name TEXT,
            surname TEXT,
            login TEXT,
            password TEXT,
            title TEXT
            )
            """)

db.commit()
