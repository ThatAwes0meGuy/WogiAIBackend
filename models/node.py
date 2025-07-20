from app import db

class Node(db.Model):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(64), unique=True, nullable=False)
    mac_address = db.Column(db.String(64))
    serial_number = db.Column(db.String(64))
    firmware_version = db.Column(db.String(32))
    hardware_version = db.Column(db.String(32))
    capabilities = db.Column(db.JSON)
    registered_at = db.Column(db.DateTime)

    sensor_data = db.relationship("SensorData", backref="node", lazy=True)
    heartbeats = db.relationship("Heartbeat", backref="node", lazy=True)
