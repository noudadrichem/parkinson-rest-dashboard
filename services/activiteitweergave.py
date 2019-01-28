from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
from tijdje import date_time_milliseconds

sys.path.append("..")

activities = Blueprint('activity', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@activities.route('/activities')
def index():
    command = 'SELECT * FROM activity'
    cur.execute(command)
    activities = cur.fetchall()

    return jsonify({
        'message': 'Alle metingen',
        'success': True,
        'activities': activities
    })


@activities.route('/activities/add', methods=['POST'])
def post():
  if request.method == 'POST':
    command = "INSERT INTO activity (staje, patientid, created) VALUES ('{}', {}, '{}')".format(
      str(request.json['staje']).upper(),
      request.json['patientid'],
      date_time_milliseconds()
    )

    print(command)
    cur.execute(command)
    connection.commit()

    return jsonify({
      'message': 'Succesfully posted activity',
      'success': True,
    })



# {
#     aantaltrillingen: 10,
#     per: 'halfeminuut'
# }

# {
#     staje: True,
#     per: 'halfeminuut'
# }
