from flask import Flask, render_template
from flask_mysqldb import MySQL
import cred

# mysql connection using Python/Flask

app = Flask(__name__)
app.secret_key = cred.secret_key
app.config['MYSQL_HOST'] = cred.mysql_host
app.config['MYSQL_USER'] = cred.mysql_user
app.config['MYSQL_PASSWORD'] = cred.mysql_password
app.config['MYSQL_DB'] = cred.mysql_db
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('select id, firstname, lastname, phone, email from users order by id asc')
    result = cur.fetchall()
    return render_template('index.html', data=result)