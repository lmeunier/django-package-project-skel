django-package-project-skel
===========================

A Django skeleton project to ease packaging with distribute.

Features
--------

- the Django project is packagable with distribute
- replace `manage.py` with `myproject_admin`
- read configuration from an external file

Install
-------

Clone this repository:
    
    $ mkdir -p myproject/src.git/
    $ git clone https://github.com/lmeunier/django-package-project-skel.git myproject/src.git/
    
Create a new virtualenv:

    $ virtualenv myproject/env/
    
Install the skeleton project in the virtualenv:

    $ . ./myproject/env/bin/activate/
    (env) $ cd myproject/src/git/
    (env) src.git $ python setup.py develop
    
The skeleton project is now installed in the virtualenv. You can use the `myproject_admin` instead of the classis `manage.py`. The `myproject` folder is a regular Django project. You can use it like any other Django project.

Create a package
----------------

Like any other project with a `setup.py` script:

    (env) src.git $ python setup.py sdist
    
This will create a new tarball in the `dist/` folder. You can install the tarball with `pip install myproject-0.1.0.tar.gz`.

manage.py
---------

The `manage.py` script is not available when installed with `pip install`, but you can use the new `myproject_admin` script installed in the `PATH`.

    (env) $ myproject_admin syncdb
    (env) $ myproject_admin runserver
    etc.

Contact
-------

You have a question? Feel free to contact me at laurent@detalima.net.

License
-------

WTFPL : http://www.wtfpl.net/
