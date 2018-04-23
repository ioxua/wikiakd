from flask import Blueprint, render_template, request, abort

website_controller = Blueprint('website_controller', __name__)

@website_controller.route('/index', methods=['GET'])
def index():
	return render_template('website/index.pug')

@website_controller.route('/index2', methods=['GET'])
def index2():
	return render_template('website/index2.pug')

@website_controller.route('/login', methods=['GET', 'POST'])
def login():
	if(request.method == 'GET'):
		return render_template('website/login.pug')
	else:
		abort(404)
