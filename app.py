from flask import Flask, render_template, request, redirect, url_for, session
from models import User
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SECRET_KEY'] = os.urandom(24) 
# Set up MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['itmowadhw2']
users_collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.find_by_username(username)
        if user and check_password_hash(user.password, password):  
            session['username'] = username
            return redirect(url_for('profile', username=username))
        else:
            return 'Invalid username or password'
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.find_by_username(username) is None:
            users_collection.insert_one({'username': username, 'password': password})
            return redirect(url_for('index'))
        else:
            return 'Username already exists'
    return render_template('register.html')

@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
    if 'username' not in session or session['username'] != username:
        return redirect(url_for('index'))
    if request.method == 'POST':
        new_password = generate_password_hash(request.form['new_password'])
        users_collection.update_one({'username': username}, {'$set': {'password': new_password}})
        return 'Password updated successfully'
    return render_template('profile.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
