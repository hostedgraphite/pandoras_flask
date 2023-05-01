#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [
    'prometheus_client==0.5.0',
    'uwsgi==2.0.18',
    'Flask==2.3.2',
]

setup(
    name='pandoras_flask',
    version='1.0.1',
    description='Flask app with Prometheus monitoring',
    long_description='Worked example of integrating Prometheus monitoring with a Flask app',
    url='https://github.com/metricfire/pandoras_flask',
    author='Metricfire',
    author_email='maintainer@metricfire.com',
    install_requires=requirements,
    packages=['pandoras_flask'],
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    keywords='flask prometheus example',
)
