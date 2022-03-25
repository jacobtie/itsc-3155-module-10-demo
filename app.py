from flask import Flask, render_template

from blueprints.book_blueprint import router as book_router
from models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:abc123@localhost:3306/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


app.register_blueprint(book_router)
