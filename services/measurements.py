from flask import Blueprint, jsonify, request, Response
import psycopg2.extras
import sys

from db import connection
from tijdje import date_time_milliseconds
from actions import fetchFromDatabse
sys.path.append("..")

measurements = Blueprint('measurements', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@measurements.route('/measurements')
def index():
  return jsonify({
    'message': 'Alle metingen',
    'success': True,
    'measurements': fetchFromDatabse('trillingen')
  })

@measurements.route('/measurements/add', methods=['POST'])
def post():
  if request.method == 'POST':
    command = '''
      INSERT INTO trillingen (
        "aantaltrillingen",
        "patientid",
        "created"
      ) VALUES ({},{},'{}')
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
