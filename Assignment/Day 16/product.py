from flask import Flask, render_template, request
from collections import namedtuple

# Initialize Flask app
app = Flask(__name__)

# Create a namedtuple to represent a Product
Product = namedtuple('Product', ['id', 'name', 'category', 'price', 'available'])

# Example list of products (this can be fetched from a database in a real-world scenario)
products = [
    Product(id=1, name="Product A", category="Electronics", price=100, available=True),
    Product(id=2, name="Product B", category="Electronics", price=50, available=False),
    Product(id=3, name="Product C", category="Clothing", price=25, available=True),
    Product(id=4, name="Product D", category="Clothing", price=80, available=True),
    Product(id=5, name="Product E", category="Electronics", price=200, available=True),
]

@app.route('/products')
def products_page():
    # Get query parameters
    category = request.args.get('category')
    available = request.args.get('available')
    sort_by = request.args.get('sort')

    filtered_products = products

    # Filter by Category
    if category:
        filtered_products = [p for p in filtered_products if p.category.lower() == category.lower()]

    # Filter by Availability
    if available is not None:  # Ensure availability is not None
        available = available.lower() == 'true'
        filtered_products = [p for p in filtered_products if p.available == available]

    # Sort by Price
    if sort_by == 'low_to_high':
        filtered_products = sorted(filtered_products, key=lambda p: p.price)
    elif sort_by == 'high_to_low':
        filtered_products = sorted(filtered_products, key=lambda p: p.price, reverse=True)

    # Count the number of products displayed after filtering
    total_count = len(filtered_products)

    # If no products match the filters, show a proper message
    if total_count == 0:
        no_results = True
    else:
        no_results = False

    return render_template(
        'products.html', 
        products=filtered_products, 
        total_count=total_count, 
        no_results=no_results,
        category=category,
        available=available,
        sort_by=sort_by
    )

if __name__ == '__main__':
    app.run(debug=True)