from flask import Blueprint, jsonify, request, Response
from db import connection
import sys
sys.path.append("..")

measurements = Blueprint('measurements', __name__)

@measurements.route('/measurements')
def index():
  print('connection: ', connection)
  cur = connection.cursor()
  print('cursor: ', cur)

  cur.execute('')
  personen = cur.fetchall()
  print('personen: ',personen)

  return jsonify({
    'message': 'All measurements'
  })


@measurements.route('/measurements/add', methods=['POST'])
def post():
  if request.method == 'POST':
    cur.execute('''
      INSERT INTO measurements (tilt, created, userId)
      VALUES (value1, value2, value3)
    ''')


    return jsonify({
      'message': 'Succesfully posted measurement',
      'success': True,
      'tilt': request.json['tilt']
    })
  else:
    return json({
      'message': 'This type of request is not available on this route.'
    })
