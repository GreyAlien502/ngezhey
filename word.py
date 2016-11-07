import dictionary

class word:
	def __init__(self,text):
		self.text = text
	def __str__(self):
		return self.text

class rootword(word):
	def __init__(self,text):
		self.text = text
		info = dictionary.translate(text)
		self.part = info['partOfSpeech']
		self.translations = info['translations']
	def english(self):
		return self.translations[0]['english']

class loanword(word):
	def __init__(self,text):
		self.text = text.upper()
		self.part = 'n'

	def english(self):
		return text.capitalize()
	
class compoundword(word):
	def __init__(self,roots):
		self.roots = roots
	def __str__(self):
		return '-'.join([str(root) for root in self.roots])
	

#class sandwhich:
