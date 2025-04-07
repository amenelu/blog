from flask import Flask, request, jsonify
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY__DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODEIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    return "Welcome to blog api"


@app.route("/posts", methodS="GET")
def getposts():
    posts = Post.query.order_by(Post.created_at_desc()).all()
    return jsonify([{"id"}])
