# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def register():
#     error = ""

#     if request.method == "POST":
#         email = request.form.get("email", "").strip()
#         password = request.form.get("password", "").strip()

#         # 1. Check blank fields
#         if not email or not password:
#             error = "Fields should not be blank"

#         # 2. Check email contains @
#         elif "@" not in email:
#             error = "Email should contain @ symbol"

#         # 3. Check password length
#         elif len(password) < 5 or len(password) > 8:
#             error = "Password must be between 5 and 8 characters"

#         else:
#             return "Form submitted successfully!"

#     return render_template("form.html", error=error)

# if __name__ == "__main__":
#     app.run(debug=True)



# ============================= Cookie ===============================================

from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("cookie_index.html")


@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form.get("username")
    cookie_name = f"user_{username}"

    visit_count = request.cookies.get(cookie_name)

    if visit_count:
        visit_count = int(visit_count) + 1
    else:
        visit_count = 1

    response = make_response(
        render_template("cookie_welcome.html", username=username, count=visit_count)
    )

    # Cookie valid for 30 days
    response.set_cookie(cookie_name, str(visit_count), max_age=60*60*24*30)

    return response


if __name__ == "__main__":
    app.run(debug=True)