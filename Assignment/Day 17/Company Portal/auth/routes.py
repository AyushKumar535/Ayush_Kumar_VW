from flask import render_template, request, redirect, make_response, url_for
from . import auth_bp

# Dummy users
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "employee": {"password": "emp123", "role": "employee"},
    "hr": {"password": "hr123", "role": "hr"},
}

@auth_bp.route("/", methods=["GET", "POST"])
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember")  # Checkbox

        user = users.get(username)

        if user and user["password"] == password:
            response = make_response(
                redirect(url_for(f"{user['role']}.dashboard"))
            )

            if remember:
                max_age = 7 * 24 * 60 * 60  # 7 days
                response.set_cookie("username", username, max_age=max_age)
                response.set_cookie("user_role", user["role"], max_age=max_age)
            else:
                response.set_cookie("username", username)
                response.set_cookie("user_role", user["role"])

            return response

        return render_template("login.html", error="Invalid Credentials")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    response = make_response(redirect(url_for("auth.login")))
    response.delete_cookie("username")
    response.delete_cookie("user_role")
    return response