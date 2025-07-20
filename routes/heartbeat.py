from flask import Blueprint, request, jsonify
from auth import token_required

heartbeat_bp = Blueprint("heartbeat", __name__)

@heartbeat_bp.route("/data/heartbeat", methods=["POST"])
@token_required
def heartbeat():
    data = request.json
    # TODO: Log or validate heartbeat
    return jsonify({"message": "Heartbeat received"}), 200
