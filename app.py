from flask import Flask, render_template, g, request, redirect, url_for, flash, jsonify
from flaskext.mysql import MySQL
from flask_login import LoginManager, login_user , logout_user , current_user , login_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

MYSQL_DATABASE_USER = 'mlukina'
MYSQL_DATABASE_PASSWORD = 'test1234'
MYSQL_DATABASE_DB = 'pc_screener_4'
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
    # Try modifying at some point to only return instances recorded by the assessor logged in?
    if request.method == "GET":
        cursor = g.db_conn.cursor()

        cursor.execute(' \
            SELECT p.id, p.first_name, p.last_name, s.sex, p.last_updated \
            FROM patient AS p \
            JOIN sex AS s \
                ON s.id = p.sex_id \
            ORDER BY last_updated DESC LIMIT 5;')
        recent_patients = [dict(id=row[0], first_name=row[1], last_name= row[2], sex=row[3], last_updated=row[4])
            for row in cursor.fetchall()]
        
        cursor.execute(' \
            SELECT p.id, p.first_name, p.last_name, s.assessor, s.assessment_urgency_score, s.assessment_required, \
                s.date_time_completed \
            FROM patient AS p \
            JOIN screener_instance AS s \
                ON p.id = s.patient_id \
            ORDER BY date_time_completed DESC LIMIT 5;')
        recent_screeners = [dict(id=row[0], first_name=row[1], last_name= row[2], assessor=row[3], 
            assessment_urgency_score=row[4], assessment_required=row[5], date_time_completed=row[6])
            for row in cursor.fetchall()]
        
        cursor.execute(' \
            SELECT p.id, p.first_name, p.last_name, s.assessor, s.assessment_urgency_score, s.assessment_required, \
                s.date_time_completed \
            FROM patient AS p \
            JOIN screener_instance AS s \
                ON p.id = s.patient_id \
            WHERE s.assessment_urgency_score >= 3 \
            ORDER BY s.assessment_urgency_score DESC, date_time_completed ASC;')
        required_cha_assessment = [dict(id=row[0], first_name=row[1], last_name= row[2], assessor=row[3], 
            assessment_urgency_score=row[4], date_time_completed=row[5])
            for row in cursor.fetchall()]

        cursor.close()

    return render_template('dashboard.html', title='Dashboard', required_cha_assessment=required_cha_assessment,
        recent_patients=recent_patients, recent_screeners=recent_screeners)

@app.route('/team4/identification_information', methods=['GET', 'POST'])
def identification_information():
    if request.method == 'GET':
        return render_template('identification_information.html', title="Identification Information")
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        middle_initial = request.form['middle_initial']
        last_name = request.form['last_name']
        jr_sr = request.form['jr_sr']
        sex = request.form['sex']
        dob = request.form['dob']
        health_card_number = request.form['health_card_number']
        province_or_territory_issued = request.form['province_or_territory_issued']
        case_record_number = request.form['case_record_number']
        province_or_territory = request.form['province_or_territory']
        postal_code = request.form['postal_code']
        facility_or_agency_id = request.form['facility_or_agency_id']
        primary_langauge_code = request.form['primary_language_code']
        interpreter_need = request.form['interpreter_need']
        reasons_for_referral = request.form['reasons_for_referral']

        cursor = g.db_conn.cursor()
        cursor.execute(' \
            INSERT INTO patient(first_name, middle_initial, last_name, jr_sr, sex_id, dob, health_card_number, \
                province_or_territory_issued, case_record_number, province_or_territory, postal_code, \
                facility_or_agency_id, primary_language_code, interpreter_need, reasons_for_referral) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            (first_name, middle_initial, last_name, jr_sr, sex, dob, health_card_number, province_or_territory_issued,
                case_record_number, province_or_territory, postal_code, facility_or_agency_id, primary_langauge_code, 
                interpreter_need, reasons_for_referral))

        g.db_conn.commit()
        cursor.close()

        flash('Form successfully submitted!')
        return redirect(url_for('screener_instance'))

@app.route('/team4/screener_instance', methods=['GET', 'POST'])
def screener_instance():
    if request.method == 'GET':
        return render_template('screener_instance.html', title="Screener Instance")
    
    elif request.method == 'POST':
        patient_id = request.form['patient_id']
        cognitive_skills = request.form['cognitive_skills']
        bathing = request.form['bathing']
        personal_hygiene = request.form['personal_hygiene']
        dressing_lower_body = request.form['dressing_lower_body']
        locomotion = request.form['locomotion']
        dyspnea = request.form['dyspnea']
        self_reported_health = request.form['self_reported_health']
        instability_of_conditions_a = request.form['instability_of_conditions_a']
        instability_of_conditions_b = request.form['instability_of_conditions_b']
        self_reported_mood = request.form['self_reported_mood']
        informal_helper_status_a = request.form['informal_helper_status_a']
        informal_helper_status_b = request.form['informal_helper_status_b']

        assessment_urgency_score = request.form['assessment_urgency_score']
        assessment_required = request.form['assessment_required']
        assessor = request.form['assessor']

        cursor = g.db_conn.cursor()
        cursor.execute(' \
            INSERT INTO screener_instance(patient_id, assessor, cognitive_skills, bathing, personal_hygiene, \
            dressing_lower_body, locomotion, dyspnea, self_reported_health, instability_of_conditions_a, \
            instability_of_conditions_b, self_reported_mood, informal_helper_status_a, informal_helper_status_b, \
            assessment_urgency_score, assessment_required) \
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (patient_id, assessor, cognitive_skills, bathing, personal_hygiene, dressing_lower_body, locomotion, 
                dyspnea, self_reported_health, instability_of_conditions_a, instability_of_conditions_b, 
                self_reported_mood, informal_helper_status_a, informal_helper_status_b, assessment_urgency_score, 
                assessment_required))

        g.db_conn.commit()
        cursor.close()

        flash('Form successfully submitted!')
        return redirect(url_for('screener_instance'))
    
if __name__ == '__main__':
    app.run(host='localhost', port='5004', debug=True)