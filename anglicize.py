import json
import sys

import parse
from dictionary import translate as english



def translate(phrase):
	print(parse.output(phrase))
	if phrase['part'] == 'noun':
		head = ''
		tail = []
		if phrase['describers'] != []:
			for describer in phrase['describers']:
				if describer['head'] == 'xo':
					head = 'no '
				elif parse.partOf(describer['head']) == 'adverb':
					tail.append('existing'+translate(describer))
				elif describer['part'] in ['adj','adv']:
					tail.append(translate(describer))
			return head + english(phrase['head'])+' that is '+" and ".join(tail)
		else:
			return head
	if phrase['part'] == 'adj':
		head = ''
		tail = ''
		for describer in phrase['describers']:
			if parse.partOf(describer['head']) == 'prep':
				tail = tail + translate(describer)
			else:
				head = head + translate(describer)
		return head +' '+ english(phrase['head'])+tail
	if phrase['part'] == 'adv':
		return english(phrase['head'])
	if phrase['part'] == 'prep':
		head = ''
		tail = 'something'
		for describer in phrase['describers']:
			if describer['part'] == 'noun':
				tail = translate(describer)
			elif describer['part'] == 'adv':
				head.append(translate(describer))
		return ", and ".join(head)+' '+english(phrase['head'])+' '+tail
	if phrase['part'] == 'adverboid':
		return english(phrase['head'])

sentence = parse.unparsed(' '.join(sys.argv[1:])+' ol')
parse.parse(sentence)
print('There is a '+translate(sentence[0]))
