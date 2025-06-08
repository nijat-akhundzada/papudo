from db import connection

cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    is_active INTEGER DEFAULT TRUE NOT NULL
)
''')


def create(fullname, email, password):
    query = f'''
        INSERT INTO User (fullname, email, password)
        VALUES ('{fullname}', '{email}', '{password}')
    '''
    cursor.execute(query)
    connection.commit()
