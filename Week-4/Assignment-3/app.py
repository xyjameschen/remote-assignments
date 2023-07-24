import json
from flask import (Flask, render_template, redirect, 
                   url_for, request, make_response,
                   flash)
import pymysql
import pymysql.cursors

host = 'localhost' # host: URL of db, localhost is for local computer
user = 'root'
password = 'xinyou81229chen'

app = Flask(__name__)
app.secret_key = 'my_secret_key'

"""connect to mysql and create a new db"""
connection = pymysql.connect(
    host = host,
    user = user,
    passwd = password,
)

with connection.cursor() as my_cursor:
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS assignment")

"""reconnect to the new db (assignment)"""
connection = pymysql.connect(
    host = host,
    user = user,
    passwd = password,
    db = 'assignment' 
)

"""create the user table"""
try:
    with connection.cursor() as my_cursor:
        my_cursor.execute("""
                        CREATE TABLE `user` (
                        `id` INTEGER AUTO_INCREMENT PRIMARY KEY, 
                        `email` varchar(255) COLLATE utf8_bin NOT NULL, 
                        `password` varchar(255) COLLATE utf8_bin NOT NULL)
                        """
                        )
except Exception as e:
    print(f'Error: {e}')

my_cursor = connection.cursor()

"""try to write a recode to test"""
# recode = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
# my_cursor.execute(recode, ('webmaster@python.org', 'very-secret'))
# connection.commit()

"""Flask"""

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
        connection.commit()

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
    connection.close()
