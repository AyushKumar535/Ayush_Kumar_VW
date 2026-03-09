from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Event, Registration

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/events", methods=["POST"])
def create_event():

    data = request.json

    event = Event(
        name=data["name"],
        total_seats=data["total_seats"],
        available_seats=data["total_seats"]
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created"})


@app.route("/events",methods=["GET"])
def get_events():

    events = Event.query.all()

    result = []

    for e in events:
        result.append({
            "id": e.id,
            "name": e.name,
            "total_seats": e.total_seats,
            "available_seats": e.available_seats
        })

    return jsonify(result)

@app.route("/register/<int:event_id>", methods=["POST"])
def register_user(event_id):

    event = Event.query.get(event_id)

    if not event:
        return jsonify({"message":"Event not found"}),404

    if event.available_seats == 0:
        return jsonify({"message":"Event is full"}),400

    data = request.json

    reg = Registration(
        user_name=data["user_name"],
        event_id=event_id
    )

    event.available_seats -= 1

    db.session.add(reg)
    db.session.commit()

    return jsonify({"message":"Registration successful"})


@app.route("/events/full",methods=["GET"])
def full_events():

    events = Event.query.filter_by(available_seats=0).all()

    result = []

    for e in events:
        result.append({
            "id":e.id,
            "name":e.name
        })

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)