from db import connection
import psycopg2.extras

cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def fetchFromDatabse(tableName):
  command = 'SELECT * FROM {}'.format(tableName)
  cursor.execute(command)
  resolved = cursor.fetchall()

  return resolved
