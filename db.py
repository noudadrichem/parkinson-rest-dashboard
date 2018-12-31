from flask import Flask, jsonify, request
app = Flask(__name__)

from psycopg2 import connect


def connectToDatabase():
  print('Connecting to database')
  conn = connect(
    host='localhost',
    database='parki',
    user='postgres',
    password='postgres'
  )
  cur = conn.cursor()

  print('PostgreSQL database version:')
  cur.execute('SELECT version()')

  db_version = cur.fetchone()
  print(db_version)

  cur.close()

  return conn


connection = connectToDatabase()

# @app.route('/')
# def index():
#   return 'nah'


# @app.route('/api')
# def returnTasks():
#   return jsonify(tasks)

# @app.route('/api/post', methods=['POST'])
# def create_task():
#   if not request.json or not 'title' in request.json:
#       abort(400)
#   task = {
#       'id': tasks[-1]['id'] + 1,
#       'title': request.json['title'],
#       'description': request.json.get('description', '),
#       'done': False
#   }

#   print(task)
#   tasks.append(task)
#   return jsonify({'task': task}), 201

