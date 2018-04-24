from flask import Flask, render_template, request, config
from sassutils.wsgi import SassMiddleware

from controllers import *

app = Flask(__name__, template_folder='views')

app.config.from_object('config')

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'static': ('sass/', 'css/', '/static/css')
})

app.register_blueprint(website_controller)
app.register_blueprint(video_controller)

# Error handling is made here because of
# http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.errorhandler
@app.errorhandler(404)
def not_found(error):
	return render_template('errors/404.pug'), 404

if __name__ == "__main__":
	app.run()
