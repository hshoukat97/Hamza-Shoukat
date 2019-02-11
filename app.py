# Landing page can contain something like the 5 most recent screener instances?

from flask import Flask, render_template, g, request, redirect, url_for
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
    # Needs to be modified to only return the top five most recent additions
    if request.method == "GET":
        cursor = g.db_conn.cursor()
        cursor.execute('SELECT id, first_name, last_name FROM screener_instance')
        screener_instance = [dict(id=row[0], first_name=row[1], last_name=
            row[2]) for row in cursor.fetchall()]
        cursor.close()

    return render_template('index.html', title='Home', screener_instance=
        screener_instance)

@app.route('/team4/screener_instance', methods=['GET', 'POST'])
def screener_instance():
    if request.method == 'GET':
        return render_template('screener_instance.html')
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        cursor = g.db_conn.cursor()
        cursor.execute('INSERT INTO screener_instance(first_name, last_name) VALUES (%s, %s)', 
            (first_name, last_name))

        g.db_conn.commit()
        cursor.close()

        return redirect(url_for('screener_instance'))
    
if __name__ == '__main__':
    app.run(host='localhost', port='5004', debug=True)