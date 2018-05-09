class Error:
	def __init__(self, title='Error', message=None):
		self.title 		= title
		self.message 	= message

	@staticmethod
	def defaultLoginError():
		return Error('Acesso negado!', 'Login ou senha inválidos.')
	
	@staticmethod
	def reduceErrorDict(dict:{}):
		result = []
		for index, val in dict.items():
			if isinstance(val, list):
				temp = list(map(lambda it: Error(index, it), val))
				result = result + temp
			else:
				result.append(Error(index, val))
		return result