from psycopg2 import connect
from config import HOST, DATABASE ,USER ,PASSWORD

def connectToDatabase():
  print('****Connecting to database****')
  conn = connect(
    host=HOST,
    database=DATABASE,
    user=USER,
    password=PASSWORD
  )
  cur = conn.cursor()

  print('PostgreSQL database version:')
  cur.execute('SELECT version()')

  retrievedData = cur.fetchall()
  print(retrievedData)

  cur.close()

  return conn

connection = connectToDatabase()

