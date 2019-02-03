from flask import Flask, render_template
app = Flask(__name__)

@app.route('/team4')
def index():
    return render_template('index.html', title='Home')

@app.route('/team4/form')
def test():
    return render_template('form.html', title='Form')

if __name__ == '__main__':
    app.run(debug=True)