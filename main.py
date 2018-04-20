from flask import Flask, render_template, request
from sassutils.wsgi import SassMiddleware
from config import Env

app = Flask(__name__, template_folder='views')

app.debug = Env['debug']

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'static': ('sass/', 'css/', '/static/css')
})


@app.route('/', methods=['GET', 'POST'])
@app.route('/<name>', methods=['GET', 'POST'])
def hello(name=None):
	if(request.method == 'GET'):
		return render_template('website/index.pug', name=name)

	elif(request.method == 'POST'):
		return render_template('website/hello.pug', name="Você mandou um POST \o/")

@app.errorhandler(404)
def not_found(error):
	return render_template('errors/404.pug'), 404


if __name__ == "__main__":
	app.run()
