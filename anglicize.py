import json
import parse

def english(word):
	dictfile = open('ngenglecian','r')
	dictionary = json.load(dictfile)
	dictfile.close()
	
	for entry in dictionary:
		if entry['original'] == word:
			return entry['translations'][0]['english']

def translate(phrase):
	if phrase['partOfSpeech'] == 'noun':
		head = ''
		tail = []
		for describer in phrase['describers']:
			if describer['head'] == 'xo':
				head = 'no '
			elif parse.partOf(describer['head']) == 'adverb':
				tail.append('existing'+translate(describer))
			elif describer['partOfSpeech'] in ['adjective','adverb']:
				tail.append(translate(describer))

	if phrase['partOfSpeech'] == 'adj':
		head = ''
		tail = ''
		for describer in phrase['describer']:
			if parse.partOf(describer['head']) == 'prep':
				tail = tail + translate(describer)
			else:
				head = head + translate(describer)
		return head +' '+ english(phrase['head'])+tail
	if phrase['partOfSpeech'] == 'adv':
		return english(phrase['head'])
	if phrase['partOfSpeech'] == 'prep':
		return english(phrase['head'])+' something'

translate([{'head': '0a0', 'describers': [{'head': 'ot', 'describers': [{'head': 'xox', 'describers': [{'head': 'ri9', 'describers': [{'head': '3o3', 'describers': [], 'part': 'adverboid'}, {'head': 'ot', 'describers': [{'head': 'joj', 'describers': [], 'part': 'noun'}], 'part': 'prep'}], 'part': 'adj'}], 'part': 'noun'}], 'part': 'prep'}, {'head': 'o', 'describers': [{'head': '3o3', 'describers': [], 'part': 'adverboid'}, {'head': 'ot', 'describers': [{'head': '0a0', 'describers': [{'head': 'ot', 'describers': [{'head': 'xox', 'describers': [{'head': 'iq', 'describers': [{'head': '3o3', 'describers': [], 'part': 'adverboid'}, {'head': 'ot', 'describers': [{'head': 'xox', 'describers': [{'head': 'ke0', 'describers': [{'head': '3o3', 'describers': [], 'part': 'adverboid'}], 'part': 'adj'}], 'part': 'noun'}], 'part': 'prep'}], 'part': 'adj'}, {'head': '0ub', 'describers': [{'head': '3o3', 'describers': [], 'part': 'adverboid'}], 'part': 'adj'}], 'part': 'noun'}], 'part': 'prep'}], 'part': 'noun'}], 'part': 'prep'}], 'part': 'adj'}], 'part': 'noun'}, {'head': '', 'describers': [], 'part': 'e:noun'}, {'head': 'ol', 'describers': [], 'part': 'endall'}])
