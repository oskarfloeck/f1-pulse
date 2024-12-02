#-----------------------------------------------------------------------------#
# config.py										  							  #
# Flask configuration file, with preferences for environment etc.             #																			  #
# Note: This file relies on a .env file that stores the secret key			  #
# and the SQLACH_DATABASE_URI.						                          #
#-----------------------------------------------------------------------------#

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

#-----------------------------------------------------------------------------#

class Config:
	"""Base config."""
	SECRET_KEY = environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = environ.get('SQLACH_DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
	FLASK_ENV = 'production'
	DEBUG = False
	TESTING = False

class DevConfig(Config):
	FLASK_ENV = 'development'
	DEBUG = True
	TESTING = True