from flask import Blueprint, jsonify
from app.controllers import ISScontroller,Sunrisecontroller

main = Blueprint('main',__name__)

@main.route('/iss-position', methods=['GET'])
def get_iss_position():
    position = ISScontroller.fetch_iss_position()
    return jsonify(position)

@main.route('/sunrise', methods=['GET'])
def get_sunrise():
    sunrise = Sunrisecontroller.fetch_sunrise()
    return jsonify(sunrise)