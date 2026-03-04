from flask import Flask
from auth import auth_bp
from admin import admin_bp
from employee import employee_bp
from hr import hr_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(employee_bp, url_prefix="/employee")
app.register_blueprint(hr_bp, url_prefix="/hr")

if __name__ == "__main__":
    app.run(debug=True)