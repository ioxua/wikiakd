from flask import Blueprint, render_template, request, abort, session
from model import Error, User
from views import LoginForm
from models import *

website_controller = Blueprint('website_controller', __name__)

mini_lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam iaculis, lorem nec vehicula luctus, felis felis rutrum mi, non efficitur arcu eros sed mauris. Fusce nec lacus lectus. Etiam mattis leo non dui pretium tempor. Vestibulum porttitor facilisis leo, eget commodo est vehicula eu."

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam iaculis, lorem nec vehicula luctus, felis felis rutrum mi, non efficitur arcu eros sed mauris. Fusce nec lacus lectus. Etiam mattis leo non dui pretium tempor. Vestibulum porttitor facilisis leo, eget commodo est vehicula eu. Mauris luctus pellentesque dui, sit amet dapibus quam tincidunt et. Nulla sagittis et nibh non elementum. Nullam nec hendrerit nunc, hendrerit lacinia neque. Quisque nec iaculis orci, eu aliquam risus. Mauris et mi a augue dapibus molestie. Nullam a sagittis odio, sit amet pulvinar elit. Praesent nec maximus nibh. Curabitur a neque magna."

blocks = [
	ArticleBlock(title="Introdução", paragraphs=[mini_lorem]),
	ArticleBlock(title="Desenvolvimento", paragraphs=[mini_lorem, lorem, lorem]),
	ArticleBlock(title="Conclusão", paragraphs=[lorem, mini_lorem]),
	ArticleBlock(title="Referências", paragraphs=[lorem]),
]
db_articles = [
	Article(1, title="Análise semiótica da falácia dos políticos envolvidos diariamente com a congruência de ideias neo-apologistas", subtitle="Uma análise baseada nos estudos de João Almeida et al", blocks=blocks),
	Article(2, title="Os efeitos da procrastinação na auto-estima", subtitle="Uma discussão baseada em fatos", blocks=blocks),
]

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

@website_controller.route('/article/<id>', methods=['GET'])
def read_article(id):
	article = find_by_id(id)
	if article is not None:
		return render_template('website/article.pug', article=article)
	return render_template('errors/404.pug')

@website_controller.route('/articles', methods=['GET'])
def article_list():
	query = request.args.get('q')
	if query is None:
		query = ""
		query_results = db_articles
	else:
		query_results = filter(search_function(query), db_articles)
		query_results = list(query_results)
	return render_template(
		'website/search.pug', 
		q=query, 
		query_results=query_results, 
		result_quantity=len(query_results)
	)

# Please kill me.
def find_by_id(id):
	res = filter(lambda a: a.id == int(id), db_articles)
	return next(iter(res), None)
	
def search_function(query):
	def res(article):
		if query is not None:
			query_upper = query.upper()
			return article.contains(query_upper)
		return True
	return res

@website_controller.route('/newArticle', methods=['GET'])
def add_article():
	return render_template('website/addArticle.pug')
