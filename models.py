class Article:
    def __init__(self, title, subtitle, authors, files, leaders):
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.files = files
        self.leaders = leaders

class File:
    def __init__(self, path, extension):
        self.path = path
        self.extension = extension

class Author:
    def __init__(self, name, user, articles):
        self.name = name
        self.user = user
        self.articles = articles

class Leader:
    def __init__(self, name, user):
        self.name = name
        self.user = user

class User:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha