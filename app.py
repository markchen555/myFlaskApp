from flask import Flask, render_template, flash, redirect, url_for, session, request, logging 
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps


app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
# If your MySQL database has password then enter it below if not leave it
# app.config['MYSQL_PASSWORD'] = '5555'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Init MYSQL
mysql = MySQL(app)


Articles = Articles()

# Home route
@app.route('/')
def index():
  return render_template('home.html')

# About route
@app.route('/about')
def about():
  return render_template('about.html')

# Articles route
@app.route('/articles')
def articles():
  return render_template('articles.html', articles = Articles)

# Single article routes
@app.route('/article/<string:id>/')
def article(id):
  return render_template('article.html', id = id)

# Register form class
class RegisterForm(Form):
  name = StringField('Name', [validators.Length(min=1, max=50)])
  username = StringField('Username', [validators.Length(min=4, max=25)])
  email = StringField('Email', [validators.Length(min=6, max=50)])
  password = PasswordField('Password', [
    validators.DataRequired(),
    validators.EqualTo('confirm', message='Passwords do not match')
  ])
  confirm = PasswordField('Confirm Password')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegisterForm(request.form)
  if request.method == 'POST' and form.validate():
    name = form.name.data
    email = form.email.data
    username = form.username.data
    password = sha256_crypt.encrypt(str(form.password.data))

    # create cursor
    cur = mysql.connection.cursor()

    # execute query
    cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

    # commit to DB
    mysql.connection.commit()

    # close connection
    cur.close()

    # show alert messages
    flash('You are now registered and ready to log in', 'success')

    return redirect(url_for('login'))
  return render_template('register.html', form=form)

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Get Form Fields
    username = request.form['username']
    passwrod_candidate = request.form['password']

    # Create cursor
    cur = mysql.connect.cursor()

    # Get user by username
    result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

    if result > 0:
      # Get stored hash
      data = cur.fetchone()
      password = data['password']

      # Compare Passwords
      if sha256_crypt.verify(passwrod_candidate, password):
        # Passed
        session['logged_in'] = True
        session['username'] = username

        flash('You are now logged in', 'success')
        return redirect(url_for('dashboard'))
      else:
        error = 'Invalid Login'
        return render_template('login.html', error=error)
      # Close connection
      cur.close()
    else:
      # If no existing User
      error = 'Username not found'
      return render_template('login.html', error=error)
    
  return render_template('login.html')

# Check if User login
def is_logged_in(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else :
      flash('Unauthorized, Please login', 'danger')
      return redirect(url_for('login'))
  return wrap

# Logout route
@app.route('/logout')
def logout():
  session.clear()
  flash('You are now logged out', 'sucess')
  return redirect(url_for('login'))

# Dashboard route
@app.route('/dashboard')
@is_logged_in
def dashboard():
  return render_template('dashboard.html')

# basic server
if __name__ == '__main__':
  app.secret_key='secret123'
  app.run(debug=True)

