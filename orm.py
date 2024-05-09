from peewee import *

db = SqliteDatabase('library.db')

class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    name = CharField(unique=True)

class Book(BaseModel):
    title = CharField()
    author = ForeignKeyField(Author, backref='books')
    genre = CharField()
    available = BooleanField(default=True)

db.connect()
db.create_tables([Author, Book])
