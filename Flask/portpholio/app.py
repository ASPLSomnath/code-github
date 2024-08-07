# app.py new

from flask import Flask,render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('page.html')

# Routes
@app.route('/about')
@app.route('/try')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)
