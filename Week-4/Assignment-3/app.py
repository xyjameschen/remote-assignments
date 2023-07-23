import json
from flask import (Flask, render_template, redirect, 
                   url_for, request, make_response,
                   flash)
import mysql.connector


"""create db"""
mydb = mysql.connector.connect(
    # host: URL of db, localhost is for local computer
    host = 'localhost',
    # root
    user = 'root',
    # the root's (user) password
    passwd = 'xinyou81229chen',
    database = 'assignment'
)

my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE assignment")
# my_cursor.execute("CREATE TABLE user (user_id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255))")


"""Flask"""
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    message = request.args.get('message')
    return render_template('index.html', message=message)

@app.route('/member')
def member():
    return render_template('member.html')

@app.route('/signup', methods=['POST'])
def signup():
    email = request.form['email']
    password = request.form['password']

    try:
        sql_query = "SELECT * FROM user WHERE email = %s"
        my_cursor.execute(sql_query, (email,))
        existing = my_cursor.fetchone() # read the row of sql_query if match the condition, else return None

        if existing:
            flash("This email is already registered.")
            return redirect(url_for('index'))
        
        sqlStuff = "INSERT INTO user (email, password) VALUES (%s, %s)"
        my_cursor.execute(sqlStuff, (email, password))
        mydb.commit()

        return redirect(url_for('member'))
    
    except Exception as e:
        return f"error: {str(e)}"

@app.route('/signin', methods=['POST'])
def signin():
    email = request.form['email']
    password = request.form['password']

    try:
        sql_query = "SELECT * FROM user WHERE email = %s AND password = %s"
        my_cursor.execute(sql_query, (email, password))

        existing = my_cursor.fetchone()

        if existing:
            return redirect(url_for('member'))
        
        flash("Email and password do not match.")
        return redirect(url_for('index'))
    
    except Exception as e:
        return f"error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
    my_cursor.close()
    mydb.close()
