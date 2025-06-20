from db import connection

cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    fullname TEXT NOT NULL,
    email TEXT PRIMARY KEY,
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


def update(user_email, is_active):

    query = f'''
        UPDATE User
        SET is_active = {is_active}
        WHERE email = '{user_email}'
    '''

    cursor.execute(query)
    connection.commit()
