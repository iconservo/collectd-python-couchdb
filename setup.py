
import os
from setuptools import setup


def pkg_dir(path):
    return os.path.join(os.path.dirname(__file__), path)


with open(pkg_dir('VERSION'), 'r') as f:
    version = f.read().strip()

setup(
    name='couchdb-collectd-plugin',
    version=version,
    py_modules=['couchdb'],
    install_requires=['requests','collectd'],
    author='Avishai Ish-Shalom',
    url='https://github.com/avishai-ish-shalom/collectd-python-couchdb',
    description='Collectd plugin to query stats from couchdb',
    classifiers=[
        'Programming Language :: Python',
    ]
    )
