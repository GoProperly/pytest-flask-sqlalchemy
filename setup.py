from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='properly-pytest-flask-sqlalchemy',
    author='Properly', # with Jean Cochrane as the author of the original package we forked this from
    author_email='info@properly.ca', # with jean@jeancochrane.com as the contact of the original package
    url='https://github.com/GoProperly/pytest-flask-sqlalchemy', # originally https://github.com/jeancochrane/pytest-flask-sqlalchemy
    description='A pytest plugin for preserving test isolation in Flask-SQlAlchemy using database transactions.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='MIT',
    version='1.2.1',
    packages=['pytest_flask_sqlalchemy'],
    install_requires=['pytest>=3.2.1',
                      'pytest-mock>=1.6.2',
                      'SQLAlchemy>=1.2.2',
                      'Flask-SQLAlchemy>=2.3',
                      'packaging>=14.1'],
    extras_require={'tests': ['pytest-postgresql>=2.4.0', 'psycopg2-binary', 'pytest>=6.0.1']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Pytest',
    ],

    # Make the package available to pytest
    entry_points={
        'pytest11': [
            'pytest-flask-sqlalchemy = pytest_flask_sqlalchemy.plugin',
        ]
    },
)
