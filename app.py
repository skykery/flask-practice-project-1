from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # https://flask.palletsprojects.com/en/2.1.x/quickstart/#the-request-object
        print(f'''{request.form['author']}: "{request.form['quote']}"''')
        return redirect(url_for('view',
                                author=request.form['author'],
                                quote=request.form['quote']))
    return render_template('add.html')


@app.route('/view/', methods=['GET'])
@app.route('/view/<author>/<quote>', methods=['GET'])
def view(author=None, quote=None):
    return render_template('view.html',
                           author=author,
                           quote=quote)


@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9080)
