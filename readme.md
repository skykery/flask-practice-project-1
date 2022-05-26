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
7. Populate the `load_data`  method from `DBService` class to insert in your database quotes from the `data.csv` file. You can read the file line by line or using the [DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader). Also, you can check the inserted data using a [MySQL client](https://ubiq.co/database-blog/top-5-mysql-gui-tools-free-paid/), or by using the `get_quotes` method you have written earlier.
8. Create a new route to edit the quote. You can use the same template `add.html`, just switch its logic using logic conditions `if`.
9. In the `add` view, after the form is submitted, insert the data using the `insert_quote` method you made earlier. Optionally, after a quote is submitted, redirect the user to the edit form/view. You can use the primaryKey(ID) from DB to form the URL (returned from `insert_quote`). 
10. List all the existing quotes on the main page (the root route `/`). Here you can use the `get_quotes` method made earlier. You can add the edit feature as a button on each quote using its ID to form the link. Make the url dynamic using something like `/edit/{id}`.

**Extra**

11. Drop you current DB scheme and make 2 tables, `author` and `quote`. Don't forget to add a one-to-many relation between the tables [Check the 1-M example](https://www.tech-recipes.com/database/one-to-one-one-to-many-table-relationships-in-sql-server/), to let an author have more than one quote linked to him.
12. Make a method `get_or_create_author` which searches in the `author` table for a provided name and returns the ID if exists. Otherwise, will create an author and will return the new ID.
13. Make a new method that inserts one quote and use the method `get_or_create_author` to get an ID for the author. Use the author's ID to add the quote. In this way, you'll link quotes with the same author to a single author. 
14. Load the CSV data by using the recently created methods. Now you'll have authors with multiple quotes linked. A real one-to-many relationship. 
15. Now you can list quotes by author using the `JOIN` statement. Change the following query accordingly to your case: 
```commandline
SELECT   *
FROM        Parent P
INNER JOIN  Child  C
    ON      C.ParentId = P.ParentId
```
The above query will join data from both tables, in our case `author` and `quote` ([SQL Joins](https://www.w3schools.com/sql/sql_join.asp)). An extra `WHERE` clause at the end will help you filter by a specific ID.
16. Make a new route and view to list all the authors with an `href` URL to something like `/author/{id}/quotes`.
17. Create a method for the route mentioned before `/author/{id}/quotes` which will return a page with the author's quotes. Use the SQL JOIN query presented above.

### AUTH

As an intro, the simplest way to do that is by using a decorator. Before executing the route method, the decorator will check if the user is authenticated.
Flask's documentation provides an example for [auth decorator](https://flask.palletsprojects.com/en/2.1.x/patterns/viewdecorators/).

In our case, we will check the user authentication by having the flag `logged_in` to `True` in his [session](https://flask.palletsprojects.com/en/2.1.x/api/#flask.session).
1. Copy the provided decorator to the `app.py` file and change its `if` condition to check if the flag `logged_in` is True in the session dict. Example `session["logged_in"] is True`. FYI make sure the key exists first.
2. Make a new route for login that accepts `GET` and `POST` requests. Handle the POST request by checking over some dummy data if the submitted data form match, and if it does, set the flag `logged_in` to `True` in the session and redirect the user somewhere. Otherwise, return an error. On the GET request, return the `login.html` template. You can add an extra argument for possible errors and render it in template if is not None.
3. Make a new route for logout action that will remove the `logged_in` key, or set a False value to it. This way, the auth decorator will not let the user access protected routes anymore.
4. Use the session to store everything you want related to the user (e.g. name) and access it from templates. You can add a simple HTML menu, where the Login button will be present if the user is not logged in. When he will be logged in, the login button will be replaced by a logout one and his username will be displayed in the same menu.

### TODO
- [x] fix typo
- [x] Add edit view for a quote listed in the main page using the same `add.html` template also, make the url dynamic using something like `/edit/{id}`.
- [x] db relationship (2 tables)
- [x] auth
- logging (directly to a separated db table)
- bigger dataset to load (multithreading)
