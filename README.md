![](https://miro.medium.com/max/3000/1*25Le7KoMK_z6BIaM8x74RA.png)
# <p align="center">TDB (The Django Boilerplate) </p>

We <img src="https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg" width="25px" height="15px"> Django!
Django has been making our lives easier for so long, though it's a tedious task to initialize and setup a Django project everytime.

Hence, I've created this boilerplate for my future projects, it's using [Python 3.10](https://www.python.org/downloads/release/python-3106/) and [Django 4.1](https://docs.djangoproject.com/en/4.1/releases/4.1/), so it will be relevant for quite some time.

Things included in the boilerplate are as follow:
 - Docker & docker-compose files to kick-off development environment.
 - Commonly used Python packages bundled into Pipfile.lock
 - Pre-commit hooks integrated (run `pre-commit install` after installing all dependencies)
	 - Black
	 - iSort
	 - flake8
 - Ready to code folder structure of Django project with some base classes (i.e. BaseModel and BaseSerializer classes)
 - settings.py configured to read environment variables and jsonified configuration files, which is a better practice to manage sensitive data.

[Update - 03/05/2021]
 - `sample` an example Django app initialized to explain, how to leverage this boilerplate.

[Update - 20/08/2022]
 - Python bumped upto version `3.10`
 - Django and DRF bumped upto version `4.1` and `3.13.1` respectively
 - `QuerySet.values` monkey-patched
 - `uuid` PK added in BaseModel
 - black bumped upto version `22.6.0` 

---------------------------------------------------------------------------------
PS: *This boilerplate is still under development, hence pinned versions of python packages might change, kindly modify accordingly before use.*
-------------------------------------------------------
