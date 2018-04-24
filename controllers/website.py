from flask import Blueprint, render_template, request, abort
from model import Error
from views import LoginForm

website_controller = Blueprint('website_controller', __name__)

@website_controller.route('/', methods=['GET'])
@website_controller.route('/index', methods=['GET'])
def index():
	return render_template('website/index.pug')


@website_controller.route('/indexTest', methods=['GET'])
def index2():
	return render_template('website/index-test.pug')


@website_controller.route('/me', methods=['GET'])
def me():
	return render_template('tests/todo.pug', next='http://localhost:5000/secret', message='Faça login primeiro D:')


@website_controller.route('/secret', methods=['GET'])
def secret():
	return render_template('tests/todo.pug', message='Se você tá vendo isso, você está logado!')

@website_controller.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	print("submitted: ", form.is_submitted())
	print("valid: ", form.validate())
	print("errors: ", form.errors)
	print(form.validate_on_submit())
	print(request.form['email'])
	if form.validate_on_submit():
		email 	= request.form['email']
		passwd 	= request.form['password']
		
		if email == 'admin@admin.admin' and passwd == 'admin':
			session['user'] = ('admin', 'admin', 'normal_user')
			return render_template('tests/todo.pug', message='Página interna da pourra toda!')
		else:
			return render_template('website-commons/login.pug', errors=[Error.defaultLoginError()], form=form)
	elif form.errors:
		return render_template('website-commons/login.pug', errors=Error.reduceErrorDict(form.errors), form=form)
	return render_template('website-commons/login.pug', form=form)