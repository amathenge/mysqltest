# MySQL database functions.

from flask_mysqldb import MySQL
from app import app
import cred

app.secret_key = cred.secret_key
app.config['MYSQL_HOST'] = cred.mysql_host
app.config['MYSQL_USER'] = cred.mysql_user
app.config['MYSQL_PASSWORD'] = cred.mysql_password
app.config['MYSQL_DB'] = cred.mysql_db
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


# notes:
# requires installation of pkg-config (via sudo apt)
# requires installation of default-libmysqlclient-dev (via sudo-apt)
# requires installation of flask-mysqldb (via pip)
