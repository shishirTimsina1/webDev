from xml.dom.minidom import CharacterData
from flask import redirect, render_template, url_for, request, flash
from app import app, db, bcrypt
from app.models import User, Chat
from app.forms import RegistrationForm, LoginForm, ChatForm
from flask_login import login_user, current_user, logout_user



@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    form = ChatForm()
    chats = Chat.query.all()
    if form.validate_on_submit():
        chat = Chat(content = form.content.data, author=current_user)
        db.session.add(chat)
        db.session.commit()
        flash('Chat sent', 'success')
        return redirect (url_for('index'))
    return render_template('index.html', chats=chats, form=form)

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password= hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful', 'danger')
        
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


