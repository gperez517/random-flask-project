from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello there, just adding this to avoid a 401 error"

@app.route('/me')
def aboutMe():
    return render_template('about_me.html.j2')
