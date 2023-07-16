import json
from flask import (Flask, render_template, redirect, 
                   url_for, request, make_response,
                   flash)

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, My Server!"

@app.route('/data')
def data():
    number = request.args.get('number')
    # request.args.get('number'): retrieves the value of the number query parameter
    # http://localhost:3000/data?number=100 will print 100, 100 is a str by default
    if number is None:
        return "Lack of Parameter"
    else:
        try:
            int(number)
        except ValueError:
            return "Wrong Parameter"
        else:
            results = 0
            for num in range(1, int(number)+1):
                results += num
            return str(results)


@app.route('/sum')
def sum():
    return render_template("sum.html")

@app.route('/myName')
def my_name():
    user_name = request.cookies.get('user_name')

    if user_name:
        return f"Hello, {user_name}!"
    else:
        return render_template("name_form.html")

@app.route('/trackName')
def track_name():
    user_name = request.args.get('name')

    if user_name:
        response = make_response(redirect(url_for('my_name')))
        response.set_cookie('user_name', user_name)
        return response
    else:
        return "Invalid name."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)

