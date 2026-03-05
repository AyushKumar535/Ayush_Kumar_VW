from flask import request, session, jsonify
from . import auth_bp

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json
    username = data.get("username")

    session["username"] = username

    return jsonify({
        "message": "Login successful",
        "user": username
    })