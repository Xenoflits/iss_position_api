from flask import Blueprint, jsonify
from app.controllers import ISScontroller

main = Blueprint('main',__name__)

@main.route('/iss-position', methods=['GET'])
def get_iss_position():
    position = ISScontroller.fetch_iss_position()
    return jsonify(position)