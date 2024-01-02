from flask import Flask, render_template , request
app = Flask(__name__)

todo = ['Pass all my classes for the year', 'Graduate Highschool']

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form['new_todo']
        todo.append(new_todo)
    
    
    return render_template( 
        'todo.html.jinja', todos= todo
                      
        )
