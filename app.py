from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

from services.measurements import measurements
from services.activiteitweergave import activities
from services.patient import patient
from services.dokter import dokter

app = Flask(__name__)
CORS(app)
app.register_blueprint(measurements)
app.register_blueprint(activities)
app.register_blueprint(patient)
app.register_blueprint(dokter)

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
  app.run(debug=True)
