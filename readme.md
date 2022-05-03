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
7. On the method for route `/add`, after you are loading the form data, return a redirect to the `/show` route and pass the required kwargs [example](https://flask.palletsprojects.com/en/2.1.x/quickstart/#rendering-templates).

### Database
Work in progress...