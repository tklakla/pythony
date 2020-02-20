from flask import render_template
from hello_world import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/omnie')
def about():
    return render_template('about.html')

@app.route('/kontakt')
def contact():
    return render_template('contact.html')

@app.context_processor
def inject_variables():
    return dict(
        user = {'name': 'Alicja'}
        )