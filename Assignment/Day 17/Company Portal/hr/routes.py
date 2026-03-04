from flask import render_template, request, redirect, url_for
from . import hr_bp

@hr_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if not role or role != "hr":
        return redirect(url_for("auth.login"))

    username = request.cookies.get("username")
    return render_template("dashboard.html", username=username, role="HR")