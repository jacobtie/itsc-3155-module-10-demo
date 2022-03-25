from flask import Blueprint, abort, redirect, render_template, request
from models import Book, db

router = Blueprint('book_router', __name__, url_prefix='/books')


@router.get('')
def get_all_books():
    all_books = Book.query.all()
    return render_template('all_books.html', books=all_books)


@router.get('/<book_id>')
def get_single_book(book_id):
    # single_book = Book.query.get(book_id)
    # if not single_book:
    #     abort(404)
    single_book = Book.query.get_or_404(book_id)
    # single_book = Book.query.filter_by(book_id=book_id).first()
    return render_template('single_book.html', book=single_book)


@router.get('/new')
def get_new_book_form():
    return render_template('new_book_form.html')


@router.post('')
def create_book():
    title = request.form.get('title', '')
    author = request.form.get('author', '')
    rating = request.form.get('rating', 0, type=int)

    if title == '' or author == '' or rating < 1 or rating > 5:
        abort(400)

    new_book = Book(title=title, author=author, rating=rating)
    db.session.add(new_book)
    db.session.commit()

    return redirect(f'/books/{new_book.book_id}')


@router.get('/<book_id>/edit')
def get_edit_book_form(book_id):
    book_to_edit = Book.query.get_or_404(book_id)
    return render_template('edit_book_form.html', book=book_to_edit)


@router.post('/<book_id>')
def update_book(book_id):
    book_to_update = Book.query.get_or_404(book_id)
    author = request.form.get('author', '')
    rating = request.form.get('rating', 0, type=int)

    if author == '' or rating < 1 or rating > 5:
        abort(400)

    book_to_update.author = author
    book_to_update.rating = rating

    db.session.commit()

    return redirect(f'/books/{book_id}')


@router.post('/<book_id>/delete')
def delete_book(book_id):
    book_to_delete = Book.query.get_or_404(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/books')
