from flask import Blueprint, render_template, request, abort

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
	if(request.method == 'GET'):
		return render_template('website-commons/login.pug')
	else:
		abort(404)
