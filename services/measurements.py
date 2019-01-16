from flask import Blueprint, jsonify
from db import connection
import sys
sys.path.append("..")

measurements = Blueprint('measurements', __name__)

@measurements.route('/measurements')
def index():
  print('connection: ', connection)
  cur = connection.cursor()
  print('cursor: ', cur)

  cur.execute('SELECT * FROM groupproject')
  personen = cur.fetchall()
  print('personen: ',personen)

  return jsonify({
    'message': 'Moetje chris?',
    'personen': personen
  })


@measurements.route('/measurements/add', method='POST')
def post():
  return 'post'
