from flask import Blueprint, request, jsonify
from auth import token_required
from models.node import Node
from app import db
from datetime import datetime

registration_bp = Blueprint("register", __name__)

@registration_bp.route("/register/node", methods=["POST"])
@swag_from({
    "tags": ["Node Registration"],
    "summary": "Register a new node",
    "parameters": [
        {
            "name": "Authorization",
            "in": "header",
            "type": "string",
            "required": True
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {"$ref": "#/definitions/NodeRegistration"}
        }
    ],
    "responses": {
        201: {"description": "Node registered and config returned"}
    }
})
@token_required
def register_node():
    data = request.json
    node = Node(
        node_id=data["node_id"],
        mac_address=data["mac_address"],
        serial_number=data["serial_number"],
        firmware_version=data["firmware_version"],
        hardware_version=data["hardware_version"],
        capabilities=data["capabilities"],
        registered_at=datetime.utcnow()
    )
    db.session.add(node)
    db.session.commit()

    return jsonify({
        "status": "registered",
        "node_id": node.node_id,
        "config": {
            "sample_rate_hz": 8000,
            "transmission_interval_sec": 5,
            "heartbeat_interval_sec": 30
        }
    }), 201
