from app import db

class Heartbeat(db.Model):
    __tablename__ = 'heartbeats'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(64), db.ForeignKey('nodes.node_id'), nullable=False)
    timestamp_utc = db.Column(db.DateTime)
    system_status = db.Column(db.JSON)
    power_status = db.Column(db.JSON)
    communication = db.Column(db.JSON)
    sensor_health = db.Column(db.JSON)
    data_quality = db.Column(db.JSON)
