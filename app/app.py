from flask import Flask, render_template

app = Flask(__name__)

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
