from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
sys.path.append("..")

dokter = Blueprint('dokter', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@dokter.route('/dokter')
def index():
    command = 'SELECT * FROM dokter'
    cur.execute(command)
    dokter = cur.fetchall()

    return jsonify({
        'message': 'Alle metingen',
        'success': True,
        'dokters': dokter
    })


@dokter.route('/dokter/add', methods=['POST'])
def adddokter():
  print(request.json)

  command = '''
    INSERT INTO dokter (
      "fullname",
      "ziekenhuis"
    )
    VALUES ('{}','{}')
    '''.format(
      request.json['fullName'],
      request.json['ziekenhuis']
    )

  print(command)
  cur.execute(command)
  connection.commit()

  return jsonify({
    'message': 'succesfully added dokter'
  })

