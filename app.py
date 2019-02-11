from flask import Flask, render_template, g
from flaskext.mysql import MySQL

app = Flask(__name__)

MYSQL_DATABASE_USER = 'Pmadziak'
MYSQL_DATABASE_PASSWORD = 'test3'
MYSQL_DATABASE_DB = 'pc_screener'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_PORT = 3306

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
mysql.init_app(app)

@app.before_request
def dbConnect():
    g.db_conn = mysql.connect()

@app.teardown_request
def logTeardown(exception=None):
    g.db_conn.close()

@app.route('/team4')
def index():
    return render_template('index.html', title='Home')

@app.route('/team4/screener_instance', methods=['GET', 'POST'])
def test():
    return render_template('screener_instance.html', title='Screener Instance')


if __name__ == '__main__':
    app.run(debug=True)