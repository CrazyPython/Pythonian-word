import pickle
class font(object):
	
class header(object):
	
class page(object):
	def __init__(self):
		self.content = []
	def add(self,what,par):
		self.content.append(what(par))
class document(object):
	def __init__(self,pages = 1):
		global page
		self.pages = []
		for i in range(pages):
			self.pages.append(page())
		
