from flask import Flask, request, jsonify
from config import Config
from models import db, Task
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

CORS(app)


# CREATE TASK
@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    title = data.get("title")
    priority = data.get("priority")

    if not title or not priority:
        return jsonify({"error": "Title and priority required"}), 400

    task = Task(
        title=title,
        priority=priority,
        completed=False
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"})


# VIEW TASKS + FILTER
@app.route("/tasks", methods=["GET"])
def get_tasks():

    priority = request.args.get("priority")
    completed = request.args.get("completed")

    query = Task.query

    if priority:
        query = query.filter(Task.priority == priority)

    if completed is not None:
        query = query.filter(Task.completed == (completed.lower() == "true"))

    tasks = query.order_by(Task.created_at.desc()).all()

    result = []

    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "completed": t.completed,
            "created_at": t.created_at
        })

    return jsonify(result)


# TOGGLE TASK STATUS
@app.route("/tasks/<int:id>/toggle", methods=["PUT"])
def toggle_task(id):

    task = Task.query.get_or_404(id)

    task.completed = not task.completed

    db.session.commit()

    return jsonify({"message": "Task updated"})


# DELETE TASK
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":
    app.run(debug=True)