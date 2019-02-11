from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

MYSQL_DATABASE_USER = 'PMadziak'
MYSQL_DATABASE_PASSWORD = 'test3'
MYSQL_DATABASE_DB = 'pc_screener'

@app.route('/team4')
def index():
    return render_template('index.html', title='Home')

@app.route('/team4/screener_instance')
def test():
    return render_template('screener_instance.html', title='Screener Instance')

if __name__ == '__main__':
    app.run(debug=True)