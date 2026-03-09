from flask import Blueprint, request, jsonify
from app import db
from app.models import Order

main = Blueprint('main', __name__)

# Add order
@main.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    order = Order(
        product_name=data['product_name'],
        quantity=data['quantity'],
        price=data['price']
    )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully', 'order_id': order.id}), 201

# Get all orders
@main.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    output = [{
        'id': o.id,
        'product_name': o.product_name,
        'quantity': o.quantity,
        'price': o.price,
        'revenue': o.revenue
    } for o in orders]
    return jsonify(output)

# Total revenue
@main.route('/orders/total_revenue', methods=['GET'])
def total_revenue():
    total = sum(o.revenue for o in Order.query.all())
    return jsonify({'total_revenue': total})

# Orders with revenue > 2000
@main.route('/orders/high_revenue', methods=['GET'])
def high_revenue():
    orders = [o for o in Order.query.all() if o.revenue > 2000]
    output = [{
        'id': o.id,
        'product_name': o.product_name,
        'quantity': o.quantity,
        'price': o.price,
        'revenue': o.revenue
    } for o in orders]
    return jsonify(output)