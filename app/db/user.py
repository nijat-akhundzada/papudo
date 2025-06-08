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


def create(fullname: str, email: str, password: str):
    query = f'''
        INSERT INTO User (fullname, email, password)
        VALUES ('{fullname}', '{email}', '{password}')
    '''
    cursor.execute(query)
    connection.commit()


def update(user_id, is_active):

    query = f'''
        UPDATE User
        SET is_active = {is_active}
        WHERE id = {user_id}
    '''

    cursor.execute(query)
    connection.commit()
