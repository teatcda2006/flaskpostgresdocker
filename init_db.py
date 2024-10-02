import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(
    host="db",
    database=os.environ['DB_POSTGRES'],
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            'name varchar (150) NOT NULL);'
            )

cur.execute('INSERT INTO users (name) VALUES (%s), (%s), (%s)', ('Tom1', 'Tom2', 'Tom3'))

cur.execute('SELECT * FROM users')
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()
