from flask import Blueprint, jsonify, request, Response
from db import connection
import psycopg2.extras
import sys
sys.path.append("..")

activities = Blueprint('activity', __name__)
cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

@activities.route('/activities')
def index():
    return jsonify({
        'message': 'Sta of lig je?',
        'success': True,
    })


@activities.route('/activities/add', methods=['POST'])
def post():
  if request.method == 'POST':
    print('*******************')
    print(request.json['staje'])
    print('*******************')

    value = ''
    if request.json['staje']:
        value = 't'
    else:
        value = 'f'

    command = 'INSERT INTO activity (staje) VALUES ({})'.format(value)

    print('*******************')
    print(value, command)
    print('*******************')
    # cur.execute(command)
    # connection.commit()

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
