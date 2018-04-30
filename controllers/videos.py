from flask import Blueprint, render_template

video_controller = Blueprint('video_controller', __name__)

@video_controller.route('/videos/index', methods=['GET'])
def index():
	return render_template('videos/index.pug')
