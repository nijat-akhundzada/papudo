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
        INSERT INTO Todo (name, email)
        VALUES ('{name}', '{email}')
    '''
    cursor.execute(query)
    connection.commit()


def update(todo_id: int, email: int, status: str = None, name: str = None):

    if name and status:
        query = f'''
            UPDATE Todo
            SET name = '{name}',
                status = '{status}'
            WHERE id = {todo_id} AND email = {email}
        '''
    elif status:
        query = f'''
            UPDATE Todo
            SET status = '{status}'
            WHERE id = {todo_id} AND email = {email}
        '''
    else:
        query = f'''
            UPDATE Todo
            SET name = '{name}'
            WHERE id = {todo_id} AND email = {email}
        '''
    cursor.execute(query)
    connection.commit()
