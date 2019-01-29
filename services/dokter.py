from flask import Blueprint, jsonify, request, Response
import psycopg2.extras
import sys

from db import connection
from actions import fetchFromDatabse
sys.path.append("..")

dokter = Blueprint('dokter', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@dokter.route('/dokter')
def index():
  return jsonify({
    'message': 'Alle doktoren',
    'success': True,
    'dokters': fetchFromDatabse('dokter')
  })

@dokter.route('/dokter/add', methods=['POST'])
def adddokter():
  if request.method == 'POST':
    command = '''
      INSERT INTO dokter (
        "fullname",
        "ziekenhuis"
      ) VALUES ('{}','{}')
      '''.format(
        request.json['fullName'],
        request.json['ziekenhuis']
      )

    cur.execute(command)
    connection.commit()

    return jsonify({
      'message': 'succesfully added dokter'
    })
