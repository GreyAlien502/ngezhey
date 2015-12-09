import json
import os

def translate(word):
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	dictfile = open(os.path.join(__location__, 'ngenglecian'),'r');
	dictionary = json.load(dictfile)
	dictfile.close()
	
	for entry in dictionary:
		if entry['original'] == word:
			return entry
	print('ERROR: '+word+' not found')
