from flask import Blueprint

measurements = Blueprint('measurements', __name__)

@measurements.route('/measurements')
def index():
  return 'Hello yes'
