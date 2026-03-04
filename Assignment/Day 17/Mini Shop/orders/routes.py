from flask import Blueprint, render_template, request, make_response, redirect

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route("/checkout")
def checkout():
    response = make_response(render_template("order_success.html"))
    response.delete_cookie("cart")
    return response