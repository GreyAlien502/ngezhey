import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
dictfile = open(os.path.join(__location__, 'ngenglecian'),'r');
dictionary = json.load(dictfile)
dictfile.close()

def translate(word):
	for entry in dictionary:
		if entry['original'] == word:
			return entry
	print('ERROR: '+word+' not found')

def search(string, mode="start", to='eng'):
	matches = []
	if mode == "start":
		match = lambda x,y: y[0].startswith(x)
	elif mode == "exact":
		match = lambda x,y: x==y[0]
	elif mode == "contains":
		match = lambda x,y: x in (' '.join(y))

	if to=='eng':
		for entry in dictionary:
			if match(string,[entry['original']]):
				matches.append(entry)
	if to=='nge':
		for entry in dictionary:
			matchingTranslations = []
			for translation in entry['translations']:
				if match(string,[translation['english'],' '.join(translation['notes'])]):
					matchingTranslations.append(translation)
			nuvoentry = entry.copy()
			nuvoentry['translations'] = matchingTranslations
			if nuvoentry['translations']!=[]:
				matches.append(nuvoentry)
	return matches
