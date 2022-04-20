"""This makes the test configuration setup"""
#pylint: disable=redefined-outer-name
import pytest

from app import logging_config


@pytest.fixture()
def application():
    """This makes the app"""

    application = logging_config()
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()