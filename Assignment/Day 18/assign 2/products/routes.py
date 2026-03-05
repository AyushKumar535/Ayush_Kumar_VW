from flask import jsonify, request, session, make_response
from . import products_bp
import json

products = [
    {"id":1,"name":"Laptop","price":70000},
    {"id":2,"name":"Mouse","price":500},
    {"id":3,"name":"Keyboard","price":1200}
]

@products_bp.route("/", methods=["GET"])
def get_products():
    return jsonify(products)

@products_bp.route("/view/<int:id>", methods=["GET"])
def view_product(id):

    if "username" not in session:
        return jsonify({"error":"Login required"}),401

    product = next((p for p in products if p["id"] == id), None)

    if not product:
        return jsonify({"error":"Product not found"}),404

    # Get cookie
    recent = request.cookies.get("recent_products")

    if recent:
        recent_list = json.loads(recent)
    else:
        recent_list = []

    # Add new product
    if id not in recent_list:
        recent_list.append(id)

    # Keep max 5
    if len(recent_list) > 5:
        recent_list.pop(0)

    response = make_response(jsonify(product))

    response.set_cookie(
        "recent_products",
        json.dumps(recent_list)
    )

    return response

@products_bp.route("/recent", methods=["GET"])
def get_recent():

    recent = request.cookies.get("recent_products")

    if not recent:
        return jsonify([])

    recent_list = json.loads(recent)

    result = []

    for pid in recent_list:
        product = next((p for p in products if p["id"] == pid), None)
        if product:
            result.append({
                "id": product["id"],
                "name": product["name"]
            })

    return jsonify(result)