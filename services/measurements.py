from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
from tijdje import date_time_milliseconds

sys.path.append("..")

measurements = Blueprint('measurements', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@measurements.route('/measurements')
def index():
    command = 'SELECT * FROM trillingen'
    cur.execute(command)
    measurements = cur.fetchall()

    return jsonify({
        'message': 'Alle metingen',
        'success': True,
        'measurements': measurements
    })


@measurements.route('/measurements/add', methods=['POST'])
def post():
  if request.method == 'POST':
    print(request.json)

    command = '''
        INSERT INTO trillingen (
          "aantaltrillingen",
          "patientid",
          "created"
        )
        VALUES ({},{},{})
        '''.format(
          request.json['aantaltrillingen'],
          request.json['patientid'],
          date_time_milliseconds()
        )

    cur.execute(command)
    connection.commit()

    return jsonify({
        'message': 'Succesfully posted measurement',
        'success': True,
    })
