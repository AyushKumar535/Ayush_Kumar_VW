from flask import render_template, request, redirect, url_for
from . import admin_bp

@admin_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if not role or role != "admin":
        return redirect(url_for("auth.login"))

    username = request.cookies.get("username")
    return render_template("dashboard.html", username=username, role="Admin")