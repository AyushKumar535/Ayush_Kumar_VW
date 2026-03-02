from flask import Flask, render_template

app = Flask(__name__)

# Data of students
students = [
    {"name": "John", "marks": 30},
    {"name": "Amit", "marks": 70},
    {"name": "Ayush", "marks": 91},
]

@app.route('/')
def index():
    # Pass the list of students to the template
    return render_template('stud_form.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)