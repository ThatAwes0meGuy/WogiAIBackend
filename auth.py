from flask import request, jsonify
from functools import wraps

VALID_TOKENS = {"your_token_here"}  # Replace with actual token or DB lookup

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].replace("Bearer ", "")
        if not token or token not in VALID_TOKENS:
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated