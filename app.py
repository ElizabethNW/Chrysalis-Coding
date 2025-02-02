import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/accessibility')
def accessibility():
    return render_template('accessibility.html')

@app.route('/wit')
def wit():
    return render_template('inspirationalwomenintechpage.html')

if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug=True
    )