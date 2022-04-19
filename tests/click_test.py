import os

from click.testing import CliRunner

from app import create_log_folder, create_database

runner = CliRunner()


def test_create_log_folder():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    logdir = os.path.join(root, '../app/logs')
    # make a directory if it doesn't exist
    assert os.path.exists(logdir) == True

def test_error_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    errorlog = os.path.join(root, '../app/logs/errors.log')
    logfile = os.path.exists(errorlog)
    assert logfile == True

def test_flask_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    flasklog = os.path.join(root, '../app/logs/flask.log')
    logfile = os.path.exists(flasklog)
    assert logfile == True

def test_myapp_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    myapplog = os.path.join(root, '../app/logs/myapp.log')
    logfile = os.path.exists(myapplog)
    assert logfile == True

def test_request_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    requestlog = os.path.join(root, '../app/logs/request.log')
    logfile = os.path.exists(requestlog)
    assert logfile == True

def test_sqlalchemy_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    sqlalchemylog = os.path.join(root, '../app/logs/sqlalchemy.log')
    logfile = os.path.exists(sqlalchemylog)
    assert logfile == True

def test_werkzeug_log_file():
    root = os.path.dirname(os.path.abspath(__file__))
    werkzeuglog = os.path.join(root, '../app/logs/werkzeug.log')
    logfile = os.path.exists(werkzeuglog)
    assert logfile == True


def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    # set the name of the apps log folder to logs
    dbdir = os.path.join(root, '../database')
    # make a directory if it doesn't exist
    assert os.path.exists(dbdir) == True