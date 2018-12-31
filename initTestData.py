import psycopg2
from index import connection

def create_tables():
  commands = [
    """
      CREATE TABLE vendors (
        vendor_id SERIAL PRIMARY KEY,
        vendor_name VARCHAR(255) NOT NULL
      )
    """,
    """
      CREATE TABLE parts (
        part_id SERIAL PRIMARY KEY,
        part_name VARCHAR(255) NOT NULL
      )
    """
  ]

  cur = connection.cursor()
  for command in commands:
    print('Succesfully executed\n: {}'.format(command))
    cur.execute(command)
  cur.close()
  connection.commit()


create_tables()
