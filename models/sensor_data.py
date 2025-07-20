from app import db

class SensorData(db.Model):
    __tablename__ = 'sensor_data'
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(64), db.ForeignKey('nodes.node_id'), nullable=False)
    gateway_id = db.Column(db.String(64))
    timestamp_utc = db.Column(db.DateTime)
    sample_rate_hz = db.Column(db.Integer)
    batch_size = db.Column(db.Integer)
    sequence_start = db.Column(db.BigInteger)
    raw_data = db.Column(db.JSON)
    processed_data = db.Column(db.JSON)
    node_status = db.Column(db.JSON)
