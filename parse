#!/usr/bin/env python 
import json
import sys
'''
sentence(
	word(
		head:
		part:
		describers:(
			tail
			...
		)
	)
	...
)
'''

parts = [
 'noun','adj','adv','prep', 'adverboid']
desc = [
[False,False,False,True, False],
[True, False,False,False,False],
[True, True, True, True, False],
[True, True, True, True, False],
[True, True, True, True, False]
]
def partList(lecian):
	output = []
	for i in range(0,len(lecian)):
		if lecian[i]:
			output.append(parts[i])
	return output

def partOf(word):
	wordFile = open('ngenglecian','r')
	wordlecian = json.load(wordFile)
	wordFile.close()
	for wordlecian_item in wordlecian:
		if wordlecian_item['original'] == word:
			return convertPart(wordlecian_item['partOfSpeech'])
	print(word)

def convertPart(part):
	parts = 'n aj av pr ab dn ed'.split(' ')
	nuvoparts = 'noun adj adv prep adverboid ender endall'.split(' ')
	return nuvoparts[parts.index(part)]

def describes(head,tail):
	if (head == 'conj') or\
	   (tail == 'conj') or\
	   (head == 'ender')or\
	   (tail == 'ender'):
		return False
	if head[1] == ':':
		if head[0] == 'e':
			return False
	if tail[1] == ':':
		if tail[0] == 'e':
			return describes(head,tail[2:])

	head = parts.index(head)
	tail = parts.index(tail)
	return desc[tail][head]

def attempt(sentence,i):
	word = sentence[i]['part']
	if (i < len(sentence)-1) & (i >= 0):
		post = sentence[i+1]['part']
		if (post == 'conj'):
			sentence[i-1]['part'] = 'c:'+word['part']
			return True
		if (word == 'ender'):
			if post[:2] == 'e:':
				kind = post[2:]
			else:
				kind = post
			sentence[i]['part'] = 'e:'+kind
			return True
		if (word[0] != 'e') & (post == 'endall'):
			sentence.insert(i+1,{'head':'','part':'e:noun','describers':[]})
			return True
	if word[0] == 'e':
		return False


	if (i < len(sentence)-1) & (i >= 1): 
		pre = sentence[i-1]['part']
		post = sentence[i+1]['part']
		if (pre == 'prep') &\
		   (post == 'noun'):
			if (post[:2] == 'e:') and\
			   (describes(word,post[2:])):
				sentence[i-1]['describers'].append(sentence.pop(i))
				sentence.pop(i)
				return True
			if not describes('noun',post):
				sentence[i-1]['describers'].append(sentence.pop(i))
				sentence[i-1]['part'] = 'adv'
				return True
		if (describes(pre,word)):
			if (post[:2] == 'e:') and\
			   (describes(word,post[2:])):
				sentence[i-1]['describers'].append(sentence.pop(i))
				sentence.pop(i)
				return True
			if (not describes(word,post)):
				sentence[i-1]['describers'].append(sentence.pop(i))
				return True
	return False

def parse(sentence):
	index = len(sentence)-1
	while len(sentence) > 1:
		if (attempt(sentence,index)):
			index = len(sentence)-1
		else:
			index = index -1
			if index == 0:
				return False
	return(True)

def output(tree):
	if tree['describers'] == []:
		return '['+tree['head']+']'
	else:
		return '['+tree['head']+' ' +' '.join([output(describer) for describer in tree['describers']])+']'

def unparsed(string):
	words =  string.split(' ')
	o=[{'p':partOf(word),'w':word} for word in words] 
	return [{'head':u['w'],'part':u['p'],'describers':[]} for u in o]

def parsed(i):
	return output(sentence[i])


sentence = unparsed(' '.join(sys.argv[1:])+' ol')
parse(sentence)
for i in range(0,len(sentence)-1):
	done = parsed(i)
	if done != '[]':
		print(done)
