from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # https://flask.palletsprojects.com/en/2.1.x/quickstart/#the-request-object
        print('You made it, almost!')
    return render_template('add.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9080)
