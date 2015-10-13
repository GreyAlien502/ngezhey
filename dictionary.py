import json

def translate(word):
	dictfile = open('ngenglecian','r')
	dictionary = json.load(dictfile)
	dictfile.close()
	
	for entry in dictionary:
		if entry['original'] == word:
			return entry
	print('ERROR: '+word+' not found')
