from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
import os

from config import DevConfig, ProdConfig

app = Flask(__name__)
env = os.getenv("FLASK_ENV", "development")
app.config.from_object(ProdConfig if env == "production" else DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Swagger
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Telemetry Cloud API",
        "description": "Industrial Machine Telemetry System API",
        "version": "1.1"
    },
    "basePath": "/api/telemetry/v1"
})

# Import & Register Blueprints
from routes.sensor_data import sensor_bp
from routes.heartbeat import heartbeat_bp
from routes.registration import registration_bp
from routes.config import config_bp
from routes.health import health_bp

app.register_blueprint(sensor_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(heartbeat_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(registration_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(config_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(health_bp, url_prefix="/api/telemetry/v1")

if __name__ == "__main__":
    app.run(debug=True)
swagger.template['definitions'] = {
    "SensorData": {
        "type": "object",
        "properties": {
            "message_type": {"type": "string"},
            "timestamp_utc": {"type": "string", "format": "date-time"},
            "node_id": {"type": "string"},
            "gateway_id": {"type": "string"},
            "sample_rate_hz": {"type": "integer"},
            "batch_size": {"type": "integer"},
            "sequence_start": {"type": "integer"},
            "raw_data": {"type": "array", "items": {"type": "object"}},
            "processed_data": {"type": "object"},
            "node_status": {"type": "object"}
        },
        "required": ["timestamp_utc", "node_id"]
    },
    "HeartbeatData": {
        "type": "object",
        "properties": {
            "message_type": {"type": "string"},
            "timestamp_utc": {"type": "string"},
            "node_id": {"type": "string"},
            "system_status": {"type": "object"},
            "power_status": {"type": "object"},
            "communication": {"type": "object"},
            "sensor_health": {"type": "object"},
            "data_quality": {"type": "object"}
        },
        "required": ["timestamp_utc", "node_id"]
    },
    "NodeRegistration": {
        "type": "object",
        "properties": {
            "message_type": {"type": "string"},
            "timestamp_utc": {"type": "string"},
            "node_id": {"type": "string"},
            "mac_address": {"type": "string"},
            "serial_number": {"type": "string"},
            "firmware_version": {"type": "string"},
            "hardware_version": {"type": "string"},
            "capabilities": {"type": "object"}
        },
        "required": ["node_id", "mac_address", "serial_number"]
    }
}
