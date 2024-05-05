from peewee import *

db = SqliteDatabase('library.db')

class Author(Model):
    name = CharField()

    class Meta:
        database = db

class Book(Model):
    title = CharField()
    author = ForeignKeyField(Author, backref='books')
    genre = CharField()
    available = BooleanField(default=True)

    class Meta:
        database = db

db.connect()
db.create_tables([Author, Book])
