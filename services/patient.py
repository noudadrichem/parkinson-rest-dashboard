from flask import Blueprint, jsonify, request, Response
import sys
import psycopg2.extras

from db import connection
from actions import fetchFromDatabse
sys.path.append("..")

patient = Blueprint('patient', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@patient.route('/patient')
def index():
  return jsonify({
    'message': 'Alle metingen',
    'success': True,
    'patients': fetchFromDatabse('patient')
  })


@patient.route('/patient/add', methods=['POST'])
def addPatient():
  if request.method == 'POST':
    command = '''
      INSERT INTO patient (
        "fullname",
        "leeftijd",
        "initialdoses",
        "bodymass"
      ) VALUES ('{}',{},'{}',{})
      '''.format(
        request.json['fullName'],
        request.json['leeftijd'],
        request.json['initialDoses'],
        request.json['bodyMass']
      )

    cur.execute(command)
    connection.commit()

    return jsonify({
      'message': 'succesfully added patient'
    })

