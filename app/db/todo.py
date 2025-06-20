from db import connection

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT DEFAULT "DUE" NOT NULL,
    user INTEGER NOT NULL,
    FOREIGN KEY (user) REFERENCES User(email) ON DELETE CASCADE
)
''')


def create(name: str, email: int):
    query = f'''
        INSERT INTO Todo (name, user)
        VALUES ('{name}', '{email}')
    '''
    cursor.execute(query)
    connection.commit()


def get_all(email: str):
    query = f'''
        SELECT * FROM Todo
        WHERE user='{email}'
    '''
    cursor.execute(query)
    data = [{'id': row[0], 'name': row[1], 'status': row[2]}
            for row in cursor.fetchall()]

    return data


def update(todo_id: int, email: int, status: str = None, name: str = None):

    if name and status:
        query = f'''
            UPDATE Todo
            SET name = '{name}',
                status = '{status}'
            WHERE id = {todo_id} AND user = '{email}'
        '''
    elif status:
        query = f'''
            UPDATE Todo
            SET status = '{status}'
            WHERE id = {todo_id} AND user = '{email}'
        '''
    else:
        query = f'''
            UPDATE Todo
            SET name = '{name}'
            WHERE id = {todo_id} AND user = '{email}'
        '''
    cursor.execute(query)
    connection.commit()
