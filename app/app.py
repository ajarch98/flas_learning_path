from flask import Flask, render_template
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Advait'}
    posts = [
        {
            'author': {'username':'John'},
            'body': 'Beautiful day in Portland!!'
        },
        {
            'author':{'username':'Susan'},
            'body':'The Avengers movie was amazing!!'
        }
    ]
    return render_template("index.html", title = "Hello to Microblog", user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html", title = "Sign In", form = form)
