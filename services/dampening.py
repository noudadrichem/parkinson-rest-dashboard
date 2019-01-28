# /dampening/add
from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
from tijdje import date_time_milliseconds

sys.path.append("..")

dampening = Blueprint('dampening', __name__)

cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@dampening.route('/dampening')
def index():
    command = 'SELECT * FROM dampening'
    cur.execute(command)
    dampening = cur.fetchall()

    return jsonify({
        'message': 'Alle metingen',
        'success': True,
        'dampening': dampening
    })


@dampening.route('/dampening/add', methods=['POST'])
def post():
  if request.method == 'POST':
    print(request.json)

    command = '''
        INSERT INTO dampening (
          "luchtvochtigheid",
          "patientid",
          "created"
        )
        VALUES ({},{},'{}')
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
