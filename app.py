from flask import Flask, render_template
from data import Articles


app = Flask(__name__)

Articles = Articles()

# home route
@app.route('/')
def index():
  return render_template('home.html')

# about route
@app.route('/about')
def about():
  return render_template('about.html')

# articles route
@app.route('/articles')
def articles():
  return render_template('articles.html', articles = Articles)

# eatch article routes
@app.route('/article/<string:id>/')
def article(id):
  return render_template('article.html', id = id)

if __name__ == '__main__':
  app.run(debug=True)

