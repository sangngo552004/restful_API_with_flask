from sqlalchemy import func
from .extension import db

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    birth_date = db.Column(db.Date)
    gender = db.Column(db.String(10))
    class_name = db.Column(db.String(10))

    def __init__(self, name, birth_date, gender, class_name):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.class_name = class_name

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    page_count = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
      
    def __init__(self, name, page_count, author_id, category_id):
        self.name = name
        self.page_count = page_count
        self.author_id = author_id
        self.category_id = category_id

class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    borrow_date = db.Column(db.Date, default=func.now())
    return_date = db.Column(db.Date)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))

    def __init__(self, return_date, student_id, book_id):
        self.return_date = return_date
        self.student_id = student_id
        self.book_id = book_id

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique = True, nullable = False)

    def __init__(self, name):
        self.name = name

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique = True, nullable = False)

    def __init__(self, name):
        self.name = name 
