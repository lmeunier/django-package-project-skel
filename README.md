django-package-project-skel
===========================

A Django project template to ease packaging with distribute.

Features
--------

- the Django project is packagable with distribute
- replace `manage.py` with `myproject_manage`
- read configuration from an external file

Install
-------

Create a new virtualenv and install Django:

    $ mkdir myproject
    $ cd myproject/
    myproject/ $ virtualenv env
    myproject/ $ . ./env/bin/activate
    (env) myproject/ $ pip install django

Start a new Django project using this template:

    (env) myproject/ $ mkdir src
    (env) myproject/ $ cd src/
    (env) myproject/src/ $ django-admin.py startproject --template=https://github.com/lmeunier/django-package-project-skel/archive/django-1.6.zip myproject

Install your newly created Django project in your virtualenv:

    (env) myproject/src/ $ cd myproject/
    (env) myproject/src/myproject/ $ python setup.py develop

Test your installation:

    (env) myproject/src/myproject/ $ myproject_manage runserver

Go to http://127.0.0.1:8000. If you can see the welcome message `It worked!`, then your installation is ok.

The skeleton project is now installed in the virtualenv. You can use the `myproject_manage` command instead of the classic `manage.py`. The `myproject` folder is a regular Django project. You can use it like any other Django project.

Create a package
----------------

Like any other project with a `setup.py` script:

    (env) myproject/src/myproject/ $ python setup.py sdist

This command will create a new tarball in the `dist/` folder. You can install the tarball with `pip install myproject-0.1.0.tar.gz`.

manage.py
---------

The `manage.py` script is not available when installed with `pip install`, but you can use the new `myproject_manage` script installed in the `PATH`.

    (env) $ myproject_manage syncdb
    (env) $ myproject_manage runserver
    etc.

Contact
-------

You have a question? Feel free to contact me at laurent@detalima.net.

License
-------

WTFPL : http://www.wtfpl.net/
