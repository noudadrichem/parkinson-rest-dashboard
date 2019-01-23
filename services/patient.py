from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
sys.path.append("..")

patient = Blueprint('patient', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@patient.route('/patient')
def index():
    command = 'SELECT * FROM patient'
    cur.execute(command)
    patient = cur.fetchall()

    return jsonify({
        'message': 'Alle metingen',
        'success': True,
        'patients': patient
    })


@patient.route('/patient/add', methods=['POST'])
def addPatient():
  print(request.json)

  command = '''
    INSERT INTO patient (
      "fullname",
      "leeftijd",
      "initialdoses",
      "bodymass"
    )
    VALUES ('{}',{},'{}',{})
    '''.format(
      request.json['fullName'],
      request.json['leeftijd'],
      request.json['initialDoses'],
      request.json['bodyMass']
    )

  print(command)
  cur.execute(command)
  connection.commit()

  return jsonify({
    'message': 'succesfully added patient'
  })

