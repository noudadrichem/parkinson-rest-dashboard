from flask import Blueprint, jsonify, request, Response
import psycopg2.extras
import sys

from db import connection
from tijdje import date_time_milliseconds
from actions import fetchFromDatabse
sys.path.append("..")

dampening = Blueprint('dampening', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@dampening.route('/dampening')
def index():
  return jsonify({
    'message': 'Alle metingen',
    'success': True,
    'dampening': fetchFromDatabse('dampening')
  })


@dampening.route('/dampening/add', methods=['POST'])
def post():
  if request.method == 'POST':
    command = '''
      INSERT INTO dampening (
        "luchtvochtigheid",
        "patientid",
        "created"
      ) VALUES ({},{},'{}')
      '''.format(
        request.json['luchtvochtigheid'],
        request.json['patientid'],
        date_time_milliseconds()
      )

    cur.execute(command)
    connection.commit()

    return jsonify({
      'message': 'Succesfully posted dampening',
      'success': True,
    })
