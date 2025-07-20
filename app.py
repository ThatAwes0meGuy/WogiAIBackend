from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from config import DevConfig, ProdConfig

app = Flask(__name__)
env = os.getenv("FLASK_ENV", "development")
app.config.from_object(ProdConfig if env == "production" else DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
