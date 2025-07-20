from flask import request, jsonify
from functools import wraps

VALID_TOKENS = {"your_token_here"}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if token not in VALID_TOKENS:
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated
