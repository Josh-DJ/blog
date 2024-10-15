from flask import Flask, render_template
import datetime
import requests
app = Flask(__name__)

@app.route("/")
def home():
    yr = datetime.datetime.now().year
    return render_template('index.html', year=yr)

@app.route("/guess/<name>")
def guess(name):
    result = requests.get(f"https://api.agify.io?name={name}").json()
    age = result['age']
    return render_template("guess.html", name=name, age=age)

@app.route("/blog")
def blog():
    blog_posts = requests.get("https://api.npoint.io/e51247ba3a1a98718dd9").json()
    return render_template("blog.html", posts=blog_posts)



if __name__ == "__main__":
    app.run(debug=True)