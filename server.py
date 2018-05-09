from flask import Flask, render_template, request, config

from sassutils.wsgi import SassMiddleware
from flask_session import Session
from flask_wtf.csrf import CSRFProtect

from controllers import *

app = Flask(__name__, template_folder='views')

app.config.from_object('config')

#CSRFProtect(app)  
Session(app)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'static': ('sass/', 'css/', '/static/css')
})

app.register_blueprint(common_controller)
app.register_blueprint(website_controller)
app.register_blueprint(video_controller)

# Error handling is made here because of
# http://flask.pocoo.org/docs/0.10/api/#flask.Blueprint.errorhandler
@app.errorhandler(404)
def not_found(error):
	return render_template('errors/404.pug'), 404

if __name__ == "__main__":
	app.run()
