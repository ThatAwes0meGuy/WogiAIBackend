from flask import Blueprint, request, jsonify
from auth import token_required

sensor_bp = Blueprint("sensor", __name__)

@sensor_bp.route("/data/sensor", methods=["POST"])
@token_required
def upload_sensor_data():
    data = request.json
    # TODO: Validate and process data
    return jsonify({"message": "Sensor data received"}), 200
