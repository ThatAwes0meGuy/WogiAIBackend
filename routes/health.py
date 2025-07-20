# routes/health.py
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "Telemetry Cloud API is up and running",
        "version": "1.1",
        "date": "2025-07-20"
    }), 200
