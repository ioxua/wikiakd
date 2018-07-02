class Article:
    def __init__(self, title, subtitle, authors, content, leaders):
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.content = content
        self.leaders = leaders

class Author:
	def __init__(self, name, user, articles):
		self.name = name
		self.articles = articles
		self.user = user

class Leader:
    def __init__(self, name, user):
        self.name = name
        self.user = user

class User:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha
