#-----------------------------------------------------------------------------#
# __init__.py										  						  #
# Honestly, I just follow the docs..                                          #
#-----------------------------------------------------------------------------#

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.DevConfig')

	db.init_app(app)
	migrate.init_app(app, db)

	from .routes import main
	app.register_blueprint(main)

	return app
