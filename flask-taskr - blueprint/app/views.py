#/app/views.py

from app import app, db
from flask import Blueprint, Flask,render_template, request, session,flash,redirect,url_for,g
from functools import wraps
from app.models import FTasks

#app=Flask(__name__)
#app.config.from_object('config')
#db=SQLAlchemy(app)

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (getattr(form, field).label.text,error), 'error')


def login_required(test):
	@wraps(test)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return test(*args,**kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('users.login'))
	return wrap

@app.errorhandler(500)
def internal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html'), 404

@app.route('/', defaults={'page': 'index'})
def index(page):
	return(redirect(url_for('users.login')))
