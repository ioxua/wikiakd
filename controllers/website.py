from flask import Blueprint, render_template

website_controller = Blueprint('website_controller', __name__)

@website_controller.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('website/index.pug')

@website_controller.route('/index2', methods=['GET', 'POST'])
def index2():
	return render_template('website/index2.pug')

@website_controller.route('/index3', methods=['GET', 'POST'])
def index3():
	return render_template('website/index3.pug')

@website_controller.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('website/login.pug')
