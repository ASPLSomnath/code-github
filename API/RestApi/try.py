# app.py

from flask import Flask, render_template_string,render_template

app = Flask(__name__)



# Routes
@app.route('/')
@app.route('/try')
def about():
    return render_template('page.html', content='''
    {% block content %}
    <header>
        <h1>About Me</h1>
        <p>Hello! I am Somnath Chakraborty, a passionate Software Developer. Welcome to my personal webpage.</p>
    </header>
    {% endblock %}
    ''')

@app.route('/projects')
def projects():
    return render_template('page.html', content='''
    {% block content %}
    <section>
        <h2>Projects</h2>
        <p>Here are some of the projects I have worked on:</p>
        <ul>
            <li><strong>Project 1:</strong> Description of project 1.</li>
            <li><strong>Project 2:</strong> Description of project 2.</li>
            <li><strong>Project 3:</strong> Description of project 3.</li>
        </ul>
    </section>
    {% endblock %}
    ''')

@app.route('/skills')
def skills():
    return render_template('page.html', content='''
    {% block content %}
    <section>
        <h2>Skills</h2>
        <p>Here are some of my skills:</p>
        <ul>
            <li>Programming Languages: Python, JavaScript, C++</li>
            <li>Frameworks: Flask, Django, React</li>
            <li>Databases: MySQL, PostgreSQL</li>
        </ul>
    </section>
    {% endblock %}
    ''')

@app.route('/contact')
def contact():
    return render_template('page.html', content='''
    {% block content %}
    <section>
        <h2>Contact</h2>
        <p>You can contact me at:</p>
        <p>Email: somnath@example.com</p>
        <p>Phone: +1234567890</p>
    </section>
    {% endblock %}
    ''')

@app.route('/blog')
def blog():
    return render_template('page.html', content='''
    {% block content %}
    <section>
        <h2>Blog</h2>
        <p>Welcome to my blog! Here you will find my latest posts.</p>
        <ul>
            <li><strong>Post 1:</strong> Summary of post 1.</li>
            <li><strong>Post 2:</strong> Summary of post 2.</li>
            <li><strong>Post 3:</strong> Summary of post 3.</li>
        </ul>
    </section>
    {% endblock %}
    ''')

if __name__ == '__main__':
    app.run(debug=True)
