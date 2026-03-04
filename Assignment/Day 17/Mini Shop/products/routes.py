from flask import Blueprint, render_template, request, redirect, make_response
import json

products_bp = Blueprint('products', __name__, url_prefix='/products')

PRODUCTS = {
    "laptop": 1000,
    "mouse": 50,
    "keyboard": 80,
    "headphones": 150,
    "monitor": 300
}

@products_bp.route("/")
def show_products():
    return render_template("products.html", products=PRODUCTS)

@products_bp.route("/add/<product>")
def add_to_cart(product):
    cart = request.cookies.get("cart")

    if cart:
        cart = json.loads(cart)
    else:
        cart = {}

    cart[product] = cart.get(product, 0) + 1

    response = make_response(redirect("/cart/"))
    response.set_cookie("cart", json.dumps(cart))

    return response