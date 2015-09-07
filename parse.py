import json
import sys

import word
import phrase

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
 'n','aj','av','pr', 'ab']
desc = [
[False,False,False,True, False],
[True, False,False,False,False],
[True, True, True, True, False],
[True, True, True, True, False],
[True, True, True, True, False]
]
dummy = word.word('')
dummy.part = ':dnn'

def describes(head,tail):
	if (head == 'cj') or\
	   (tail == 'cj') or\
	   (head == 'dn')or\
	   (tail == 'dn'):
		return False
	if head[0] == ':':
		if head[1:3] == 'dn':
			return False
	if tail[0] == ':':
		if tail[1:3] == 'dn':
			return describes(head,tail[3:])

	head = parts.index(head)
	tail = parts.index(tail)
	return desc[tail][head]

def attempt(sentence,i):
	part = sentence[i].part
	if (i < len(sentence)-1) & (i >= 0):
		post = sentence[i+1].part
		if (post == 'cj'):
			sentence[i-1].part = ':cj'+part
			return True
		if (part == 'dn'):
			if post[:3] == ':dn':
				kind = post[3:]
			else:
				kind = post
			sentence[i].part = ':dn' + kind
			return True
		if (part not in ['dn',':dnn']) & (post == 'ed'):
			sentence.insert(i+1,phrase.phrase(dummy))
			return True
	if part[:3] == ':dn':
		return False

	if (i < len(sentence)-1) & (i >= 1): 
		pre = sentence[i-1].part
		post = sentence[i+1].part
		if (pre == 'pr') & (part == 'n'):
			if (post[:3] == ':dn') and\
			   (describes(part,post[3:])):
				sentence[i-1].desc.append(sentence.pop(i))
				sentence.pop(i)
				return True
			if not describes('n',post):
				sentence[i-1].desc.append(sentence.pop(i))
				sentence[i-1].part = 'av'
				return True
		if (describes(pre,part)):
			if (post[:3] == ':dn') and\
			   (describes(part,post[3:])):
				sentence[i-1].desc.append(sentence.pop(i))
				sentence.pop(i)
				return True
			if (not describes(part,post)):
				sentence[i-1].desc.append(sentence.pop(i))
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

def output(inphrase):
	if inphrase.desc == []:
		return '['+str(inphrase.head)+']'
	else:
		return '['+str(inphrase.head)+' ' +' '.join([output(describer) for describer in inphrase.desc])+']'

def unparsed(words):
	output=[phrase.phrase(word.rootword(actuword)) for actuword in words] 
	return output
