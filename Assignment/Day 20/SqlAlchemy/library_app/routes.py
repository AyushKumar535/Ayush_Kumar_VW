from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Book

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@main_routes.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        copies = int(request.form['copies'])
        
        book = Book(title=title, author=author, copies=copies)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_book.html')

@main_routes.route('/borrow/<int:book_id>')
def borrow_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.copies > 0:
        book.copies -= 1
        db.session.commit()
    return redirect(url_for('main.index'))

@main_routes.route('/unavailable')
def unavailable_books():
    books = Book.query.filter_by(copies=0).all()
    return render_template('unavailable_books.html', books=books)