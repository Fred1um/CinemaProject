import sqlite3 as sq
from tkntr import *

if __name__ == "__main__":
    with sq.connect('cinema.db') as db:
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

