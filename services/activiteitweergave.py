from flask import Blueprint, jsonify, request, Response
import psycopg2.extras
import sys

from tijdje import date_time_milliseconds
from db import connection
from actions import fetchFromDatabse
sys.path.append("..")

activities = Blueprint('activity', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@activities.route('/activities')
def index():
  return jsonify({
    'message': 'Alle metingen',
    'success': True,
    'activities': fetchFromDatabse('activity')
  })

@activities.route('/activities/add', methods=['POST'])
def post():
  if request.method == 'POST':
    command = "INSERT INTO activity (staje, patientid, created) VALUES ('{}', {}, '{}')".format(
      str(request.json['staje']).upper(),
      request.json['patientid'],
      date_time_milliseconds()
    )

    cur.execute(command)
    connection.commit()

    return jsonify({
      'message': 'Succesfully posted activity',
      'success': True,
    })
