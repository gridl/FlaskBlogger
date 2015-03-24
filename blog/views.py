from flask import render_template

from blog import app
from database import session
from models import Post

@app.route("/")
def posts():
    posts = session.query(Post)
    posts = posts.order_by(Post.datetime.desc())
    posts = posts.all()
    return render_template("posts.html",
        posts=posts
    )
    
@app.route("/login", methods=["GET"])
def login_get():
	return render_template("login.html")