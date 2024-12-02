#-----------------------------------------------------------------------------#
# routes.py										  							  #
# Some special magic going on here.                                           #
#-----------------------------------------------------------------------------#

from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

#--------------------------- Page Rendering ----------------------------------#

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/profile')
def profile():
	return render_template('profile.html')

@main.route('/oracle')
def oracle():
	return render_template('oracle.html')

#-----------------------------------------------------------------------------#

