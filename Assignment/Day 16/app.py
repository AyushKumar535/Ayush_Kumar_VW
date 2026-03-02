# from flask import Flask
# app = Flask(__name__)

# @app.route('/add/<int:num1>/<int:num2>')

# def add(num1,num2):
#     result = num1+num2
#     return f"The addition of {num1} and {num2} is {result}"

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def home():
    names = ["arun","ayush","rahul"]
    return render_template("index.html",names=names)

if __name__ == '__main__':
    app.run(debug=True)