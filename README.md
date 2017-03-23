# Evonove website

[![Build Status](https://travis-ci.org/evonove/evonove.it.svg?branch=master)](https://travis-ci.org/evonove/evonove.it)

[evonove.it][1] website, made with [Wagtail][2]!


## Requirements

To run this project you need the Docker engine (>=1.12.1) and the docker-compose command (>=1.8.0) installed.

To install the Docker engine on your platform see:

    https://docs.docker.com/engine/getstarted/step_one/

To install docker-compose command:

    https://docs.docker.com/compose/install/


## Getting Started

To start the Evonove Website project run this command from the root folder:

    $ docker-compose up

Migration and a user are needed so run:

    $ docker-compose run django python django-website/manage.py migrate
    $ docker-compose run django python django-website/manage.py createsuperuser

Running migrations isn't enough because the home page requires some data.
If you dislike inserting data using the admin (or in general be a data insert operator),
you can launch the following commands that create the blog page linked to the
home page and a set of initial data for a fake company.

    $ docker-compose run django python django-website/manage.py create_pages
    $ docker-compose run django python django-website/manage.py load_test_data

Now visit [http://localhost:8000/](http://localhost:8000/) to see the application running.

Documentation is served at [http://localhost:9000](http://localhost:9000)
A frontend to the mailhog smtp service is served at: [http://localhost:8025](http://localhost:8025)

## Running the tests

To run the tests:

    $ docker-compose -f containers/test.yml up


## Frontend development

The frontend app uses Gulp and Wheelie as toolchain. To install them run this command from the `wheelie/` folder:

    $ yarn

To run the frontend app you need to launch Gulp tasks from the `wheelie/` folder with:

    $ gulp

To install the development dependencies run:

    $ yarn add -D [package]

To install the production dependencies run:

    $ yarn add [package]


When the frontend is ready to be deployed, launch the production build and
commit all files in the repository:

    $ gulp build --production
    $ git commit -m 'Process static files'

[1]: https://evonove.it/ "Evonove"
[2]: https://wagtail.io/ "Wagtail"
