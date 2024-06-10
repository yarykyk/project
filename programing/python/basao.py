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

cursor.execute('''
CREATE TABLE IF NOT EXISTS jar(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    balance REAL DEFAULT 0.0
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
)
''')


conn.commit()
conn.close()


def add_jar(user_id, username):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO jar (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()

def update_jar(user_id, amount):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    current_balance = get_jar(user_id)
    new_balance = current_balance + amount
    cursor.execute('UPDATE jar SET balance = ? WHERE user_id = ?', (new_balance, user_id))
    conn.commit()
    conn.close()

def get_jar(user_id):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM jar WHERE user_id = ?', (user_id,))
    balance = cursor.fetchone()[0]
    print(balance)
    conn.close()
    return balance



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
    cursor.execute('INSERT INTO transactions (user_id, amount) VALUES (?, ?)', (user_id, amount))
    conn.commit()
    conn.close()


def get_balance(user_id):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM wallet WHERE user_id = ?', (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def transactions(user_id):
    conn = sqlite3.connect('wallet.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions WHERE user_id = ?', (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    return transactions


