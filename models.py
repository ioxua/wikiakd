from server import db

# Creating models here. This is wrong on SO many levels

class Article(db.Model):
	title = db.Column(db.String(80), nullable=False)
	content_path = db.Column(db.String(100), unique=True, nullable=False)

db.create_all()