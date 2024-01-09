from flask import Flask, render_template , request, redirect
import pymysql 
import pymysql.cursors
from pprint import pprint as print 


app = Flask(__name__)

todo = ['Pass all my classes for the year', 'Graduate Highschool']


connect = pymysql.connect(
    database = 'lfrancois_todos',
    user = 'lfrancois',
    password = '231566837',
    host = '10.100.33.60',
    cursorclass=pymysql.cursors.DictCursor
)



@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        new_todo = request.form['new_todo']
        todo.append(new_todo)
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO `todos` (description) VALUES ('{new_todo}')")
        cursor.close()


    cursor = connect.cursor()
    cursor.execute("SELECT * FROM `todos`")
    results = cursor.fetchall()
    cursor.close()     

    return render_template( 
        'todo.html.jinja', 
        todos= results
        )

@app.route('/delete_todo/<int:todo_index>', methods =['POST'])
def todo_delete(todo_index):
    cursor = connect.cursor()
    
    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")

    cursor.close()
    connect.commit()



    return redirect('/')
