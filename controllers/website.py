from flask import Blueprint, render_template, request, abort, session
from model import Error, User
from views import LoginForm
from models import Article
#from 

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

@website_controller.route('/about', methods=['GET'])
def about():
	return render_template('website/about.pug')

@website_controller.route('/article', methods=['GET'])
def new_article():
	return render_template('website/article.pug')

@website_controller.route('/article/<id>', methods=['GET'])
def read_article(id):
	return render_template('tests/todo.pug', message='Leitura do artigo nº{}'.format(id))

@website_controller.route('/articles', methods=['GET'])
def article_list():
	query = request.args.get('q')
	return render_template('website/search.pug', q=query)

@website_controller.route('/test', methods=['GET'])
def test():
	art = Article(title='TITULO DAORA', content_path='C:/path/to/sla')
	art.save()