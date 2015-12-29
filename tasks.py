from invoke import task
import pytest, logging.config

import settings as app_settings

@task()
def clean():
    '''Clean build directory.'''
    print 'Cleaning build directory...'

@task(clean, help={'name': "Name of the person to say hi to."})
def hi(name):
    print("Hi %s!" % name)

@task
def all():
    pytest.main()


@task(clean)
def unit():
    # initialize logging config
    logging.config.dictConfig(app_settings.LOGGING)
    # add -x to enable print
    #pytest.main(['-x','tests/unit'])
    pytest.main('tests/unit')
