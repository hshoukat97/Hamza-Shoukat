from flask import Flask, render_template
app = Flask(__name__)

@app.route('/team4')
def index():
    return render_template('index.html', title='Home')

@app.route('/team4/screener_instance')
def test():
    return render_template('screener_instance.html', title='Screener Instance')

if __name__ == '__main__':
    app.run(debug=True)