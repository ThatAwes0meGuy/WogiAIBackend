from flask import Blueprint, request, jsonify
from auth import token_required

registration_bp = Blueprint("register", __name__)

@registration_bp.route("/register/node", methods=["POST"])
@token_required
def register_node():
    data = request.json
    # TODO: Save node info
    return jsonify({
        "status": "registered",
        "node_id": data["node_id"],
        "config": {
            "sample_rate_hz": 8000,
            "transmission_interval_sec": 5,
            "heartbeat_interval_sec": 30
        },
        "endpoints": {
            "data_upload": "https://client-api.com/api/telemetry/v1/data/sensor",
            "config_check": "https://client-api.com/api/telemetry/v1/config/node"
        }
    }), 201
