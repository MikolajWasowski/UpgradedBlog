from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def get_about():
    return render_template("about.html",)

@app.route("/contact")
def get_contact():
    return render_template("contact.html",)

@app.route("/blog/<blog_id>")
def get_blog(blog_id):
    return render_template("post.html", posts=all_posts[int(blog_id)])

if __name__ == "__main__":
    app.run(debug=True)
