from flask import Flask, render_template

app = Flask(__name__)


# Home Page
@app.route('/')
def index():
    return render_template('home.html', title='Home | Ratan Kumar')

# Project
@app.route('/projects')
def project():
    return render_template('project.html', title="Projects")

# About Us
@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

# About Us
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

if __name__ == '__main__':
    app.run(debug=True)