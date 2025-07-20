from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from auth import token_required
from models.heartbeat import Heartbeat

heartbeat_bp = Blueprint("heartbeat", __name__)

@heartbeat_bp.route("/data/heartbeat", methods=["POST"])
@swag_from({
    "tags": ["Heartbeat"],
    "summary": "Upload heartbeat data",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "default": "Bearer your_token_here"
        },
        {
            "name": "body",
            "in": "body",
            "schema": {"$ref": "#/definitions/HeartbeatData"},
            "required": True
        }
    ],
    "responses": {
        201: {"description": "Heartbeat stored"}
    }
})
@token_required
def upload_heartbeat():
    try:
        data = request.get_json()

        heartbeat = Heartbeat(
            node_id=data["node_id"],
            timestamp_utc=datetime.fromisoformat(data["timestamp_utc"].replace("Z", "+00:00")),
            system_status=data.get("system_status"),
            power_status=data.get("power_status"),
            communication=data.get("communication"),
            sensor_health=data.get("sensor_health"),
            data_quality=data.get("data_quality")
        )
        db.session.add(heartbeat)
        db.session.commit()

        return jsonify({"message": "Heartbeat stored"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@heartbeat_bp.route("/data/heartbeat/<string:node_id>", methods=["GET"])
@swag_from({
    "tags": ["Heartbeat"],
    "summary": "Get heartbeat data by node",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True
        },
        {
            "name": "node_id",
            "in": "path",
            "type": "string",
            "required": True
        }
    ],
    "responses": {
        200: {"description": "List of heartbeat entries"}
    }
})
@token_required
def get_heartbeat(node_id):
    results = Heartbeat.query.filter_by(node_id=node_id).order_by(Heartbeat.timestamp_utc.desc()).all()
    data = [
        {
            "timestamp_utc": r.timestamp_utc.isoformat(),
            "system_status": r.system_status,
            "power_status": r.power_status,
            "communication": r.communication,
            "sensor_health": r.sensor_health,
            "data_quality": r.data_quality
        } for r in results
    ]
    return jsonify(data), 200