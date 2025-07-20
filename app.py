from flask import Flask
from flask import jsonify
from routes.sensor_data import sensor_bp
from routes.heartbeat import heartbeat_bp
from routes.registration import registration_bp
from routes.config import config_bp

app = Flask(__name__)

# Health check endpoints
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Server is running"}), 200


# Register blueprints
app.register_blueprint(sensor_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(heartbeat_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(registration_bp, url_prefix="/api/telemetry/v1")
app.register_blueprint(config_bp, url_prefix="/api/telemetry/v1")

if __name__ == "__main__":
    app.run(debug=True)
