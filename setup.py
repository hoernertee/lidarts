# -*- coding: utf-8 -*-

"""Distutils setup.py file.

Used to create an installable package for deployment.
"""

from setuptools import find_packages, setup

setup(
    name='lidarts',
    version='0.6.0-8',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'alembic',
        'bcrypt',
        'bleach',
        'coverage',
        'Flask-BabelEx',
        'Flask-Login',
        'Flask-Mail',
        'Flask-Migrate',
        'Flask-Moment',
        'Flask-Security',
        'Flask-SocketIO',
        'Flask-SQLAlchemy',
        'Flask-Uploads',
        'Flask-WTF',
        'gevent',
        'gunicorn',
        'mypy',
        'numpy',
        'psycopg2-binary',
        'pytest',
        'python-dotenv',
        'redis',
        'wemake-python-styleguide',
    ],
)
