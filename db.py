from flask import Flask, jsonify, request
from psycopg2 import connect
from createTestData import commands

app = Flask(__name__)

def connectToDatabase():
  print('Connecting to database')
  conn = connect(
    host='localhost',
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

def initDatabaseTables():
  cur = connection.cursor()
  for command in commands:
    cur.execute(
      command
    )

  cur.close()
  connection.commit()

  print('Succesfully created tables.')

# Use this function to initialize the database tables.
# initDatabaseTables()
