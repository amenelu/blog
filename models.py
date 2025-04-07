from flask_alchemy import sqlalchemy

db = sqlalchemy()


class Post(db.Model):
    id = db.column(db.intiger, primarykey=True)
    title = db.column(db.string(100), nullabe=False)
    content = db.column(db.text, nullable=False)
    author = db.column(db.string, nullable=False)
    created_a = db.column(db.DateTime, default=db.func.current_timestamp())
