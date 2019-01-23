from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
sys.path.append("..")

measurements = Blueprint('measurements', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@measurements.route('/measurements')
def index():
    command = 'SELECT * FROM meting'
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
        INSERT INTO meting (
            "xposition",
            "yposition",
            "zposition",
            "xacceleration",
            "yacceleration",
            "zacceleration"
        )
        VALUES ({},{},{},{},{},{})
        '''.format(
            request.json["xPosition"],
            request.json["yPosition"],
            request.json["zPosition"],
            request.json["xAcceleration"],
            request.json["yAcceleration"],
            request.json["zAcceleration"]
            )

    cur.execute(command)
    connection.commit()

    return jsonify({
        'message': 'Succesfully posted measurement',
        'success': True,
    })
