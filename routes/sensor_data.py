from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from auth import token_required
from models.sensor_data import SensorData
from flasgger import swag_from

sensor_bp = Blueprint("sensor", __name__)

@sensor_bp.route("/data/sensor", methods=["POST"])
@swag_from({
    'tags': ['Sensor Data'],
    'description': 'Upload raw and processed sensor data',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': True,
            'default': 'Bearer your_token_here'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                '$ref': '#/definitions/SensorData'
            }
        }
    ],
    'responses': {
        201: {'description': 'Sensor data stored'},
        400: {'description': 'Invalid input'},
        401: {'description': 'Unauthorized'}
    }
})
@token_required
def upload_sensor_data():
    try:
        data = request.get_json()

        new_data = SensorData(
            node_id=data["node_id"],
            gateway_id=data.get("gateway_id"),
            timestamp_utc=datetime.fromisoformat(data["timestamp_utc"].replace("Z", "+00:00")),
            sample_rate_hz=data.get("sample_rate_hz"),
            batch_size=data.get("batch_size"),
            sequence_start=data.get("sequence_start"),
            raw_data=data.get("raw_data"),
            processed_data=data.get("processed_data"),
            node_status=data.get("node_status")
        )
        db.session.add(new_data)
        db.session.commit()

        return jsonify({"message": "Sensor data stored"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@sensor_bp.route("/data/sensor/<string:node_id>", methods=["GET"])
@swag_from({
    "tags": ["Sensor Data"],
    "summary": "Get all sensor data for a node",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True,
            "default": "Bearer your_token_here"
        },
        {
            "name": "node_id",
            "in": "path",
            "type": "string",
            "required": True
        }
    ],
    "responses": {
        200: {"description": "List of sensor data"}
    }
})
@token_required
def get_sensor_data(node_id):
    results = SensorData.query.filter_by(node_id=node_id).order_by(SensorData.timestamp_utc.desc()).all()
    data = [
        {
            "timestamp_utc": r.timestamp_utc.isoformat(),
            "sample_rate_hz": r.sample_rate_hz,
            "raw_data": r.raw_data,
            "processed_data": r.processed_data,
            "node_status": r.node_status
        } for r in results
    ]
    return jsonify(data), 200
