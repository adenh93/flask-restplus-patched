import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'flask_restplus_patched/__init__.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-restplus-patched-aher93",
    version=__version__,
    url="https://github.com/aher93/flask-restplus-patched",

    author="Aden Herold",
    author_email="aden.herold1@gmail.com",

    description="Extends Flask-RESTplus so it can handle Marshmallow schemas and Webargs arguments.",
    long_description=open('README.rst').read(),

    packages=['flask_restplus_patched-aher93'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',

    install_requires=[
        'Flask', 'flask-restplus', 'marshmallow', 'flask-marshmallow',
        'webargs', 'apispec'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
