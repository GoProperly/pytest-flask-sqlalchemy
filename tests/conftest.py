import pytest

pytest_plugins = ['pytester']


@pytest.fixture(scope='module')
def conftest():
    '''
    Load configuration file for the tests to a string, in order to run it in
    its own temporary directory.
    '''
    with open('tests/_conftest.py', 'r') as conf:
        conftest = conf.read()

    return conftest


@pytest.fixture(scope='module')
def testfile():
    '''
    Load a file with tests in it to a string, in order to run them in a temporary
    directory.
    '''
    with open('tests/_test_plugin.py', 'r') as tf:
        testfile = tf.read()

    return testfile
