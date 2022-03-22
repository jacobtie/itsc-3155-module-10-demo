from flask import Flask, render_template

from models import Book, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc123@localhost:3306/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/books')
def get_all_books():
    all_books = Book.query.all()
    return render_template('all_books.html', books=all_books)
