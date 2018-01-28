# How To Install

## Basic Software Requirements

### Packages


#### Bare Minimum

- Python 3.6
- [MongoDB](https://www.mongodb.com/) as the back-end
- Optional: [Gunicorn](http://gunicorn.org/). Recommended for running
  the microservices.

#### Suggested Packages

These packages [should] have no bearing on how well the application performs,
but they're pretty useful.

- [Nginx](https://www.nginx.com/), or anther web service (for getting static packages)
- [Virtualenv](https://pypi.python.org/pypi/virtualenv), for Python.
- Highly recommended for making virtualenv easier: [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

### Operating System

The initial development has been done on **Ubuntu 17.10**. No other operating
systems have been tested.

## Installing

First of all, install Python and MongoDB. **Ensure you're using Python 3.6**.

Next, clone the reposity https://github.com/src-r-r/1Base.git.

    $ git clone --recursive https://github.com/src-r-r/1Base.git
    $ cd 1Base

The submodules should already be checked out. If not, update them.

    $ git submodule init
    $ git submodule --sync

Install the requirements. If you're using a virtualenv, ensure you've activated
the environment.

    $ pip install -r requirements.txt

Install each package in *development* mode. Since these are git submodules it
should be pretty easy:

    $ git submodule foreach python setup.py develop

## Starting the microservices

As a rule of thumb, the service you're developing the most should be run with
Python. The service that's running in the background should be run with
gunicorn.

This statement will make sense once you see what's going on.

Go to the microservice you wish to work on.

    $ cd onebase_api/

The Flask app is defined in `onebase_api/__init__.py`. This means that to run
the flask app, simply type:

    $ FLASK_APP=onebase_api python -m flask run

And you're off to the races!

Note that 1Base has a few other environment variables that are useful for
setting:

    $ export ONEBASE_MODE='development' # Makes 1Base run in "development" mode
    $ export ONEBASE_PERSIST_USER='admin@example.com' # Fakes a user session for
    $                                                 # development; only works
    $                                                 # when ONEBASE_MODE='development'

On first run of the appliction, the application will ask you to set an
administrator password. So far the admin email address is `admin@example.com`.
Set the password and remember it (if you forget it, you can always reset it
with a Python script)

If you get an error message about "config.yaml" not being found, have a look
at <a href="#configfile">the configfile section</a> below.

If everything checks out you should have the `onebase_api` running on your
system. Notice that the application is running on port `5000`. This is why
you need gunicorn for the other microservices: to run on a seperate port.

Now let's say you want to run the `onebase_web` microservice.

    $ cd $ONEBASE_ROOT/onebase_web
    $ gunicorn -w 4 -b 127.0.0.1:5002

The same environment variables as above apply here, too (in fact,
`ONEBASE_PERSIST_USER` was designed for the web microservice). Now you can
navigate to `http://localhost:5002` in your browser.

### Configuration File <a name="configfile" />

The application will also check for a configuration file. The configuration
file is a YAML file in your home directory under
`$HOME/.share/onebase/config.yaml`. If it's not there and 1Base complains
about not finding it create it. Here's a simple example to get you
started:

    mode: development
    server:
    onebase_web:
        development:
            host: localhost
            port: 5000
            base_url: http://localhost:5000
    onebase_api:
        development:
            host: localhost
            port: 5002
            base_url: http://localhost:5002
    database:
        development:
            name: onebase
        test:
            dialect: mongodb
            host: 127.0.0.1
            port: 27017
    collection:
        development: onebase_dev
    email:
        development:
            smtp:
                host: << EMAIL HOST >>
                username: << EMAIL LOGIN >>
                port: 587
                password: << EMAIL PASSWORD >>
    static:
        development: http://localhost/~my_user/static/1base

Notice how `development` is used throughout. Each *setting* is on the first
level. The 2nd level contains the *mode*. In this case the only mode so far is
development.
