from psycopg2 import connect

def connectToDatabase():
  print('****Connecting to database****')
  conn = connect(
    host='postgres',
    database='parki',
    user='noud',
    password='test1234'
  )
  cur = conn.cursor()

  print('PostgreSQL database version:')
  cur.execute('SELECT version()')

  retrievedData = cur.fetchall()
  print(retrievedData)

  cur.close()

  return conn

connection = connectToDatabase()

