zPyClub
=====
This is a forum project fork from [June](https://github.com/pythoncn/june).

Installation
-------------

Make sure you have python2.7, pip and virtualenv installed.

NodeJS is also required to compile static assets. After NodeJS is installed. You need to install::

    $ npm install -g stylus component uglify-js nib

Development
-----------

You should read the Contribution Guide first.

Start a development server::

    $ git checkout your_fork_of_june
    $ cd june
    $ virtualenv --distribute venv
    $ source venv/bin/activate
    (venv)$ pip install -r requirements.txt
    (venv)$ make static
    (venv)$ python manager.py createdb
    (venv)$ python manager.py runserver

It should be running at localhost:5000.
