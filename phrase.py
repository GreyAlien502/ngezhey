class phrase:
	def __init__(self,head,desc=None,zhozh=False):
		if desc == None:
			desc = []
		self.head = head
		self.part = head.part
		self.desc = desc
		self.zhozh = zhozh
	def __str__(self):
		return str(self.head)+' '+' '.join([str(describer) for describer in self.desc])
	def english(self):
		if self.part == 'n':
			head = ''
			tail = []
			if self.desc != []:
				for describer in desc:
					if describer.text == 'xo':
						head = 'no '
					elif describer.part == 'av':
						tail.append('existing'+describer.english())
					elif desc.part in ['aj','av']:
						tail.append(describer.english())
				return head + self.english()+' that is '+" and ".join(tail)
			else:
				return head
		if self.part == 'aj':
			head = ''
			tail = ''
			for describer in self.desc:
				if describer.part == 'pr':
					tail = tail + desc.english()
				else:
					head = head + desc.english()
			return head +' '+ desc.head.english()+tail
		if self.part == 'av':
			return english()
		if self.part == 'pr':
			head = ''
			tail = 'something'
			for describer in self.desc:
				if describer.part == 'noun':
					tail = translate(describer)
				elif describer['part'] == 'adv':
					head.append(translate(describer))
			return ", and ".join(head)+' '+english(phrase['head'])+' '+tail
		if phrase['part'] == 'adverboid':
			return english(phrase['head'])

