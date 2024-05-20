import sqlite3

def create_table():
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wallet(
    number TEXT)
    ''')
    conn.commit()
    conn.close()

def conect():
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    wallet = cursor.fetchall()
    conn.close()
    return wallet

def balance(number):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wallet (number) VALUES (?)', (number))
    conn.commit()
    conn.close()