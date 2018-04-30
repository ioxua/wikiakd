from flask import Blueprint, render_template, request, abort
from model import Error, User
from views import LoginForm

common_controller = Blueprint('common_controller', __name__)

@common_controller.route('/profile', methods=['GET'])
def profile():
	return render_template('commons/index.pug')

@common_controller.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	print("novo metodo \o/")

	if form.is_submitted():
		print("Enviado!")
		
		if form.validate():
			print("Válido!")
			email 	= request.form['email']
			passwd 	= request.form['password']
			
			if email == 'admin@admin.admin' and passwd == 'admin':
				session['user'] = User('admin', 'admin', 'normal_user')
				return render_template('tests/todo.pug', message='Página interna da pourra toda!')
			else:
				return render_template('commons/login.pug', errors=[Error.defaultLoginError()], form=form)

		elif form.errors:
			print("Erros ao enviar D:")
			return render_template('commons/login.pug', errors=Error.reduceErrorDict(form.errors), form=form)
	
	print("Não enviado")
	return render_template('commons/login.pug', form=form)