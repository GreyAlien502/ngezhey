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
				for describer in self.desc:
					if describer.head.text == 'xo':
						head = 'no '
					elif describer.head.part == 'av':
						tail.append('existing'+describer.english())
					elif describer.head.part in ['aj','pr']:
						tail.append(describer.english())
				return head + self.head.english()+' that is '+" and ".join(tail)
			else:
				return head + self.head.english()
		if self.part == 'aj':
			head = ''
			tail = ''
			for describer in self.desc:
				if describer.head.part == 'pr':
					tail = tail + ' ' + describer.english()
				else:
					head = head + describer.english() + ' '
			return head + self.head.english() + tail
		if self.head.part == 'av':
			return \
				self.head.english() +' '+ \
				+ ' '.join([describer.english() for describer in self.desc])
		if self.head.part == 'pr':
			head = ''
			tail = 'something'
			for describer in self.desc:
				if describer.part == 'n':
					tail = describer.english()
				elif describer.part == 'av':
					head.append(translate(describer))
			return ", and ".join(head)+' '+self.head.english()+' '+tail
		if self.part == 'ab':
			return self.head.english()

