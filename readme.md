The purpose of this project is to be used as a starting skeleton for a Flask project.
Also, a list of exercises will let you understand how a simple web app works.

## Setting up the local environment
Create a new venv if you do not have one in the root of project `python3 -m venv venv` and activate it using `source venv/bin/activate`.

Another way of creating a virtualenv is to use the IDE and do it interactively.

Install all the packages from the `requirements.txt` file:
```commandline
pip install -r requirements.txt
```
And you are ready to run the skeleton project with `python app.py`

Now, take a quick look on the [Quickstart](https://flask.palletsprojects.com/en/2.1.x/quickstart/) page.

## Exercises
The following exercises will lead to a simple quotes manager application where you can create a quote, delete or view the dataset.

###  Flask basics

1. Change the method `hello` (app.py) for the root endpoint to render the existing index.html file in the `templates` directory. You'll have to use the render_template method presented in [here](https://flask.palletsprojects.com/en/2.1.x/quickstart/?highlight=render_template#rendering-templates). 
2. Read about [base layouts](https://flask.palletsprojects.com/en/2.1.x/tutorial/templates/#the-base-layout) and migrate the existing `index.html` to a base template `base.html` which will contain the HTML standard structure with two `{% block something %}{% endblock %}` for title and content. Also, use the learning block style to migrate the index.html to the new format extended from your `base.html`.
3. Create a new route `/contact` in `app.py` and return a dummy contact page template. As a bonus, you can add hyperlink in your `index.html` for your `/contact` route.
4. In the templates directory, you'll find a `add.html` file which contains an HTML form. Complete the `add` method found in `app.py` to get the submitted data from the form (author, quote) and print it in the console.
5. For the template files mentioned above `contact.html`, `add.html` and the future ones, adapt them to the new structure, using the base template.
6. Make a new route `/view` where its method accepts two arguments author and quote. In this one, render the `view.html` template passing the author and quote kwargs like in this [example](https://flask.palletsprojects.com/en/2.1.x/quickstart/#rendering-templates).
7. On the method for route `/add`, after you are loading the form data, return a redirect to the `/view` route and pass the required kwargs [example](https://flask.palletsprojects.com/en/2.1.x/quickstart/#rendering-templates).

### Database
_Work in progress..._

I added a mariadb docker service in the `docker-compose.yml` file. You can start the service with `docker-compose up -d`.

If you are not using docker-compose, and want to use the mariadb image directly with `docker`, do the following steps:
- create a volume for the mariadb container `docker volume create --name mariadb_data`
- create the mariadb container configured with its persistent volume and the exposed port `3306`
```commandline
docker run -d --name mariadb -p 3306:3306 -e ALLOW_EMPTY_PASSWORD=yes -e MARIADB_USER=user -e MARIADB_DATABASE=test -e MARIADB_PASSWORD=test --volume mariadb_data:/bitnami bitnami/mariadb:latest
```
You can see your new container by typing `docker ps`.

1. Populate the `get_connection` found at `services/db.py` to return a connection to your database using the `mysql.connector` - [examples](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html). Also, do not forget to use the right variables from `__init__`.
2. Populate the `close` and `commit` methods found in the `DBService` class.
3. In the `__main__` part of `services/db.py` execute a SQL query that creates a new table `famous_quotes` with author and quote as fields. Do not forget to use your `DBService` class.
4. Populate the `insert_quote` method from `DBService` class to connect to your database and insert a received quote with its author in the `famous_quotes` table. It can return its primary key (ID).
5. Populate the `get_quotes_by_author` method from `DBService` class to make a `SELECT` query and return all quotes with a received author.
6. Populate the `get_quotes`  method from `DBService` class to return all the quotes from `famous_quotes` table.
