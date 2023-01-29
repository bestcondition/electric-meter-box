import sqlite3
from datetime import datetime

import config


def get_conn():
    return sqlite3.connect(config.SQLITE_FILE)


def create_table():
    with get_conn() as conn:
        conn.execute('''
        CREATE TABLE if not exists balance 
        (date text, balance text)
        ''')
        conn.commit()


create_table()


def insert_balance(balance):
    with get_conn() as conn:
        conn.execute(
            'insert into balance values (?,?)',
            (datetime.now(), float(balance))
        )
        conn.commit()


def get_all_data():
    with get_conn() as conn:
        def type_map(_record):
            _datetime, balance = _record
            new_datetime = datetime.fromisoformat(_datetime)
            new_balance = float(balance)
            return new_datetime, new_balance
        return list(map(type_map, conn.execute('select * from balance')))


if __name__ == '__main__':
    print(get_all_data())
