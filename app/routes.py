from flask import render_template, flash, url_for, redirect, request
from app import App, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@App.route('/')
@App.route('/index')
@login_required
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
    return render_template("index.html", title = "Hello to Microblog", posts = posts)

@App.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(index))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for_login)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title = "Sign In", form = form)

@App.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@App.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email= form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)
