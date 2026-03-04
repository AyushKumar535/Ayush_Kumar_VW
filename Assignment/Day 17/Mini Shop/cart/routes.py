from flask import Blueprint, render_template, request, redirect, make_response
import json

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

PRODUCTS = {
    "laptop": 1000,
    "mouse": 50,
    "keyboard": 80,
    "headphones": 150,
    "monitor": 300
}

@cart_bp.route("/")
def view_cart():
    cart = request.cookies.get("cart")

    if not cart:
        return render_template("cart.html", empty=True)

    cart = json.loads(cart)

    total = 0
    items = []

    for product, qty in cart.items():
        price = PRODUCTS.get(product, 0)
        subtotal = price * qty
        total += subtotal

        items.append({
            "name": product,
            "price": price,
            "qty": qty,
            "subtotal": subtotal
        })

    return render_template("cart.html", items=items, total=total)

@cart_bp.route("/update/<product>/<action>")
def update_cart(product, action):
    cart = request.cookies.get("cart")

    if not cart:
        return redirect("/cart/")

    cart = json.loads(cart)

    if action == "increase":
        cart[product] += 1
    elif action == "decrease":
        cart[product] -= 1
        if cart[product] <= 0:
            del cart[product]

    response = make_response(redirect("/cart/"))
    response.set_cookie("cart", json.dumps(cart))

    return response

@cart_bp.route("/clear")
def clear_cart():
    response = make_response(redirect("/cart/"))
    response.delete_cookie("cart")
    return response