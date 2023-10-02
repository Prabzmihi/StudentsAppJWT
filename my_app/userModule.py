from flask import request
from my_app import app
from .userModel import User
import jwt


@app.route("/users/login", methods=["POST"])
def login():
    try:
        data = request.json
        if not data:
            return {
                "message": "Please provide user details",
                "data": None,
                "error": "Bad request",
            }, 400
        # validate input
        # is_validated = validate_email_and_password(data.get('email'), data.get('password'))
        is_validated = True
        if is_validated is not True:
            return dict(message="Invalid data", data=None, error=is_validated), 400
        user = User().login(data["username"], data["password"])
        if user:
            try:
                # token should expire after 24 hrs
                user["token"] = jwt.encode(
                    {"username": user["Username"], "role": user["UserRole"]},
                    app.config["SECRET_KEY"],
                    algorithm="HS256",
                )
                return {"message": "Successfully fetched auth token", "data": user}
            except Exception as e:
                return {"error": "Something went wrong", "message": str(e)}, 500
        return {
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized",
        }, 404
    except Exception as e:
        return {"message": "Something went wrong!", "error": str(e), "data": None}, 500
