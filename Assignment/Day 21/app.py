from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Employee
from decorators import role_required

app = Flask(__name__)
app.secret_key = "secret"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Ayush1kumar%40@localhost/company_vw"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username,password=password).first()

        if user:
            session["user_id"] = user.id
            session["role"] = user.role
            return redirect("/employees")

        return "Invalid Login"

    return render_template("login.html")


# VIEW ALL EMPLOYEES (Admin & Manager)
@app.route("/employees")
@role_required(["admin","manager"])
def employees():

    emp = Employee.query.all()

    return render_template("employees.html", emp=emp)


# CREATE EMPLOYEE (ADMIN)
@app.route("/employee/add", methods=["GET","POST"])
@role_required(["admin"])
def add_employee():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        department = request.form["department"]
        manager_id = request.form["manager_id"]

        emp = Employee(
            name=name,
            email=email,
            department=department,
            manager_id=manager_id
        )

        db.session.add(emp)
        db.session.commit()

        return redirect("/employees")

    return render_template("add_employee.html")


# VIEW PROFILE
@app.route("/employee/<int:id>")
def profile(id):

    emp = Employee.query.get(id)

    if session["role"] == "employee" and session["user_id"] != id:
        return "Access Denied"

    return render_template("profile.html", emp=emp)


# EDIT EMPLOYEE
@app.route("/employee/<int:id>/edit", methods=["GET","POST"])
def edit_employee(id):

    emp = Employee.query.get(id)
    role = session["role"]

    if role == "employee" and session["user_id"] != id:
        return "Access Denied"

    if role == "manager" and emp.manager_id != session["user_id"]:
        return "Access Denied"

    if request.method == "POST":

        emp.name = request.form["name"]
        emp.department = request.form["department"]

        db.session.commit()

        return redirect("/employees")

    return render_template("edit_employee.html", emp=emp)


# DELETE EMPLOYEE (ADMIN ONLY)
@app.route("/employee/<int:id>/delete")
@role_required(["admin"])
def delete_employee(id):

    emp = Employee.query.get(id)

    db.session.delete(emp)
    db.session.commit()

    return redirect("/employees")


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)