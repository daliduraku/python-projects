from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data_types/')
def data_types():
    return render_template('data_types.html')