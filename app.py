from flask import Flask, render_template, g, request, redirect, url_for, flash
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user , logout_user , current_user , login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

MYSQL_DATABASE_USER = 'Mlukina'
MYSQL_DATABASE_PASSWORD = 'test1234'
MYSQL_DATABASE_DB = 'pc_screener'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_PORT = 3306

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = MYSQL_DATABASE_USER
app.config['MYSQL_DATABASE_PASSWORD'] = MYSQL_DATABASE_PASSWORD
app.config['MYSQL_DATABASE_DB'] = MYSQL_DATABASE_DB
app.config['MYSQL_DATABASE_HOST'] = MYSQL_DATABASE_HOST
app.config['SECRET_KEY'] = 'r<ÄX¨:izÃrT×r@Æ65Bø-bf}"ë*¼Þ¡ÁýÙñëÃöKxGfT·7])f£mÕ`ëßW°=Ðs.s{üë¿¦'
mysql.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

#login_manager.login_view = 'login'

'''
class User(object):
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def set_password(self , password):
        #self.password = generate_password_hash(password)
        self.password = password

    def check_password(self , password):
        return self.password == password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
'''

@app.before_request
def dbConnect():
    g.db_conn = mysql.connect()

@app.teardown_request
def logTeardown(exception=None):
    g.db_conn.close()

@app.route('/team4')
def index():
    # Needs to be modified at some point to only return instances recorded by the assessor
    if request.method == "GET":
        return render_template('index.html', title='Home', screener_instance=
        screener_instance)

@app.route('/team4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', title="Login")
    '''
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        registered_user = lookup_user(username, password)

        if registered_user is None:
            flash('Username or Password is invalid', 'error')
            return redirect(url_for('login'))
        else:
            login_user(registered_user)
            flash('Logged in successfully')
            next_url = request.args.get('next')
            return redirect(next_url or url_for('home'))
        '''
@app.route('/team4/dashboard')
def dashboard():
    # Needs to be modified at some point to only return instances recorded by the assessor and perform a join
    if request.method == "GET":
        cursor = g.db_conn.cursor()
        cursor.execute(' \
            SELECT p.id, p.first_name, p.last_name, s.sex, p.time_recorded \
            FROM patient AS p \
            JOIN sex AS s \
                ON s.id = p.sex_id \
            ORDER BY time_recorded DESC LIMIT 5;')
        screener_instance = [dict(id=row[0], first_name=row[1], last_name= row[2], sex=row[3], time_recorded=row[4])
            for row in cursor.fetchall()]
        cursor.close()

    return render_template('dashboard.html', title='Dashboard', screener_instance=screener_instance)       

@app.route('/team4/identification_information', methods=['GET', 'POST'])
def identification_information():
    if request.method == 'GET':
        return render_template('identification_information.html', title="Identification Information")
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        sex = request.form['sex']
        primary_langauge_code = request.form['primary_language_code']

        cursor = g.db_conn.cursor()
        cursor.execute(' \
            INSERT INTO patient(first_name, last_name, sex_id, primary_language_code) \
            VALUES (%s, %s, %s, %s)', 
            (first_name, last_name, sex, primary_langauge_code))

        g.db_conn.commit()
        cursor.close()

        return redirect(url_for('screener_instance'))

@app.route('/team4/screener_instance', methods=['GET', 'POST'])
def screener_instance():
    if request.method == 'GET':
        return render_template('screener_instance.html', title="Screener Instance")
    
    elif request.method == 'POST':
        return redirect(url_for('screener_instance'))
    
if __name__ == '__main__':
    app.run(host='localhost', port='5004', debug=True)