from flask import Blueprint, jsonify
from auth import token_required
from flasgger import swag_from

config_bp = Blueprint("config", __name__)

@config_bp.route("/config/node/<string:node_id>", methods=["GET"])
@swag_from({
    "tags": ["Config"],
    "summary": "Get node configuration",
    "parameters": [
        {"name": "Authorization", "in": "header", "type": "string", "required": True},
        {"name": "node_id", "in": "path", "type": "string", "required": True}
    ],
    "responses": {
        200: {"description": "Node configuration JSON"}
    }
})
@token_required
def get_node_config(node_id):
    return jsonify({
        "config_version": "v2.1",
        "sampling": {
            "sample_rate_hz": 16000,
            "batch_size": 512,
            "window_size": 8192,
            "overlap_percent": 50
        },
        "processing": {
            "calculate_rms": True,
            "calculate_peak": True,
            "calculate_statistics": True,
            "fft_enabled": True,
            "frequency_bands": True
        },
        "transmission": {
            "interval_sec": 2,
            "compression_enabled": True,
            "retry_attempts": 3
        },
        "filters": {
            "anti_alias": True,
            "highpass_hz": 2.0,
            "lowpass_hz": 8000.0,
            "notch_50hz": True,
            "notch_60hz": True
        }
    }), 200

@config_bp.route("/config/wifi/<string:node_id>", methods=["GET"])
@swag_from({
    "tags": ["Config"],
    "summary": "Get WiFi configuration for node",
    "parameters": [
        {"name": "Authorization", "in": "header", "type": "string", "required": True},
        {"name": "node_id", "in": "path", "type": "string", "required": True}
    ],
    "responses": {
        200: {"description": "WiFi configuration JSON"}
    }
})
@token_required
def get_wifi_config(node_id):
    return jsonify({
        "config_version": "v1.3",
        "primary_network": {
            "ssid": "FACTORY_WIFI_2024",
            "password": "Secure@Factory2024!",
            "security": "WPA2_PSK"
        },
        "backup_networks": [
            {
                "ssid": "FACTORY_BACKUP",
                "password": "Backup@2024!",
                "priority": 2
            }
        ]
    }), 200
