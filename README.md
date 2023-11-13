# The Ghibli Project

> APIs created using Django and Django REST framework to get a list of movies and people in them.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment notes on how to deploy the project on a live system.

### Prerequisites

This project is built with Python, Django, Redis and use sqlite so you will need to have these installed on your system and a working internet connection.

- Install python in your system from [here](https://www.python.org/downloads/)
- Install redis in your system from [here](https://redis.io/docs/get-started/data-store/)

### Installing

Follow the following steps to build and run docker image for Wire It Up:

- Step 1: Clone this repository and change directory to cms
```
  $ git clone <git_url> the_ghibli_project && cd the_ghibli_project
```

- Step 2: Make a virtual environment and activate it
  ```
  $ python -m venv venv
  $ source venv/bin/activate
  ```

- Step 3: Install all the python packages
  ```
  $ pip install -r dev-requirements.txt
  ```

- Step 4: Now make migrations and migrate the db.
  ```
  $ ./manage.py makemigrations
  $ ./manage.py migrate
  ```

- Step 5: Create superuser
  ```
  $ ./manage.py createsuperuser
  ```

- Step 6: Start the development server
  ```
  $ ./manage.py runserver
  ```

- Step 7: Now go to 127.0.0.1/admin to see the login screen and login using credentials for super user credential.
- Step 8: Now create an API key nd use it for subsequent requests.

### Coding Style

This project follows pep 8 guidelines for coding practices, you can read more about [pep8](http://pep8.org/) except line length of 120.

## Deployment

Detailed instructions for deploying Django project can be found [here](https://docs.djangoproject.com/en/2.0/howto/deployment/).

## Built With

* [Python](https://www.python.org/) - Programming Language.
* [Django](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines.
* [Django REST framework](https://www.django-rest-framework.org/) - The web framework for perfectionists with deadlines.

## Authors

* **Ratan Kulshreshtha**

## Acknowledgments

* Hat tip to anyone who's code was used
* Stack Overflow
* Coffee

