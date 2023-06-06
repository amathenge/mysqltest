from flask import Flask, render_template

# mysql connection using Python/Flask

# the main Flask app object. Needs to be imported before database.py which configures
# the MySQL items in the Flask object.
app = Flask(__name__)

# database needs app to be imported - there may be a circular thing going on here since database
# also imports app - but just the object above.

import database
mysql = database.mysql

@app.template_filter('nl2br')
def nl2br(item):
    if isinstance(item, str):
        return item.replace('\n','<br>')
    return item

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('select id, firstname, lastname, phone, email from users order by id asc')
    result = cur.fetchall()
    return render_template('index.html', data=result)

@app.route('/notes')
def notes():
    cur = mysql.connection.cursor()
    cur.execute('select id, firstname, lastname, notes from users order by id asc')
    result = cur.fetchall()
    return render_template('notes.html', data=result)

@app.route('/logout')
def logout():
    return 'Still Building Logout'