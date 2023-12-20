from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_name = ""
    return render_template(
        'home.html.jinja',
        user_name = user_name
                      
        )
    

@app.route('/ping')
def ping():
    return '<h6>pong</h6>'

@app.route('/hello/<name>')
def hello(name):
    return f'<h2>hello {name}</h2>'
