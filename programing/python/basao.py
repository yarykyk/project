import sqlite3

conn = sqlite3.connect('wallet.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS wallet (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance REAL DEFAULT 0.0
)
''')


conn.commit()
conn.close()



def add_user(user_id, username):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wallet (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()


def update_balance(user_id, amount):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE wallet SET balance = balance + ? WHERE user_id = ?', (amount, user_id))
    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM wallet WHERE user_id = ?', (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance


