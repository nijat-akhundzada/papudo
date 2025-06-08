from db import connection

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT DEFAULT "DUE" NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE
)
''')


def create(name: str, user_id: int):
    query = f'''
        INSERT INTO Todo (name, user_id)
        VALUES ('{name}', '{user_id}')
    '''
    cursor.execute(query)
    connection.commit()


def update(todo_id: int, user_id: int, status: str = None, name: str = None):

    if name and status:
        query = f'''
            UPDATE Todo
            SET name = '{name}',
                status = '{status}'
            WHERE id = {todo_id} AND user_id = {user_id}
        '''
    elif status:
        query = f'''
            UPDATE Todo
            SET status = '{status}'
            WHERE id = {todo_id} AND user_id = {user_id}
        '''
    else:
        query = f'''
            UPDATE Todo
            SET name = '{name}'
            WHERE id = {todo_id} AND user_id = {user_id}
        '''
    cursor.execute(query)
    connection.commit()
