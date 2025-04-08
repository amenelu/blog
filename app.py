from flask import Flask, request, jsonify
from models import db, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def index():
    return "Welcome to blog api"


# get all posts
@app.route("/posts", methodS="GET")
def get_posts():
    posts = Post.query.order_by(Post.created_at_desc()).all()
    return jsonify(
        [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author,
                "created": post.created_at,
            }
            for post in posts
        ]
    )


# create a new Post
@app.route("/posts", methods="POST")
def createpost():
    data = request.get_json()
    new_post = Post(title=data["title"], content=data["content"], author=data["author"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "post created!!", "post_id": new_post.id})


# get a single post
@app.route("/post/<int:id>", methods="GET")
def get_post(id):
    post = post.query.get_or_4o4(id)
    return jsonify(
        [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author,
                "created_at": post.created_at,
            }
        ]
    )
