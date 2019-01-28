from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/test')
def test():
    return render_template('test.html', title='Test')

if __name__ == '__main__':
    app.run(debug=True)