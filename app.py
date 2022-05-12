from flask import Flask, render_template, request, redirect, url_for
from services.db import DBService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    db_serv = DBService()
    db_serv.get_connection()
    print(db_serv.get_quotes())
    return render_template('index.html', quotes=db_serv.get_quotes())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # https://flask.palletsprojects.com/en/2.1.x/quickstart/#the-request-object
        print(f'''{request.form['author']}: "{request.form['quote']}"''')
        db_serv = DBService()
        db_serv.get_connection()
        db_serv.insert_quote(request.form['author'], request.form['quote'])
        return redirect(url_for('view',
                                author=request.form['author'],
                                quote=request.form['quote']))
    return render_template('add.html')


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
