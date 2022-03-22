from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# CREATE TABLE IF NOT EXISTS book (
# 	book_id INT AUTO_INCREMENT,
#     title VARCHAR(255) NOT NULL,
#     author VARCHAR(255) NOT NULL,
#     rating INT NOT NULL,
#     PRIMARY KEY (book_id)
# );


class Book(db.Model):

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Book({self.book_id}, {self.title}, {self.author}, {self.rating})'
