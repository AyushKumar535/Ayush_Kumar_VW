from flask import render_template, request, redirect, url_for
from . import employee_bp

@employee_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if not role or role != "employee":
        return redirect(url_for("auth.login"))

    username = request.cookies.get("username")
    return render_template("dashboard.html", username=username, role="Employee")