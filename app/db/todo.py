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


def create(name: str, status: str, user_id: int):
    query = f'''
        INSET INTO Todo (name, status, user_id)
        VALUES ('{name}', '{status}', '{user_id}')
    '''
    cursor.execute(query)
    connection.commit()
