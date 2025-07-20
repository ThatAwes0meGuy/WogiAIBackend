from flasgger import Schema, fields

app.config['SWAGGER'] = {
    'title': 'Telemetry Cloud API',
    'uiversion': 3
}

swagger.template['definitions'] = {
    'SensorData': {
        'type': 'object',
        'properties': {
            'message_type': {'type': 'string'},
            'timestamp_utc': {'type': 'string', 'format': 'date-time'},
            'node_id': {'type': 'string'},
            'gateway_id': {'type': 'string'},
            'sample_rate_hz': {'type': 'integer'},
            'batch_size': {'type': 'integer'},
            'sequence_start': {'type': 'integer'},
            'raw_data': {'type': 'array', 'items': {'type': 'object'}},
            'processed_data': {'type': 'object'},
            'node_status': {'type': 'object'}
        },
        'required': ['timestamp_utc', 'node_id']
    }
}
