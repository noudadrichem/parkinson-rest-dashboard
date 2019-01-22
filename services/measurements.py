from flask import Blueprint, jsonify, request, Response
from db import connection
import sys
sys.path.append("..")

measurements = Blueprint('measurements', __name__)

cur = connection.cursor()


@measurements.route('/measurements')
def index():
  return jsonify({
    'message': 'All measurements',
    'success': True,
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
    cur.close()
    connection.commit()

    return jsonify({
      'message': 'Succesfully posted measurement',
      'success': True,
    })
