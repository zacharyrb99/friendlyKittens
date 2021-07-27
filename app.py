from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'password'

# toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

@app.route('/care_for_kittens')
def kitten_care():
    return render_template('kitten_care.html')

@app.route('/adopt')
def adoptions():
    return render_template('adopt.html')

@app.route('/previous_adoptions')
def kittens():
    return render_template('previous_adoptions.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')