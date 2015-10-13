from ASCIIImage.asciiimage import asciiimage as image

from phrase import phrase
'''
word--word-+-word
           |
           +-word
'''

#Connections
HOR = '-'
HOR_DOWN = '+'
DOWN_RIGHT = '`'
VERT_RIGHT = '+'
VERT = '|'
#Boudaries
TOP =          '-'
SIDE =         '|'
TOP_RIGHT =    '.'
TOP_LEFT =     ','
BOTTOM_RIGHT = "'"
BOTTOM_LEFT =  '`'

#Connections
HOR = '─'
HOR_DOWN = '┬'
DOWN_RIGHT = '└'
VERT_RIGHT = '├'
VERT = '│'
#Boudaries
TOP =          '─'
SIDE =         '│'
TOP_RIGHT =    '┐'
TOP_LEFT =     "┌"
BOTTOM_RIGHT = '┘'
BOTTOM_LEFT =  '└'

'''
HOR       =image(HOR)
HOR_DOWN  =image(HOR_DOWN)
DOWN_RIGHT=image(DOWN_RIGHT)
VERT_RIGHT=image(VERT_RIGHT)
VERT      =image(VERT)
TOP       =image(TOP)
SIDE      =image(SIDE)
TOP_RIGHT =image(TOP_RIGHT)
TOP_LEFT  =image(TOP_LEFT)
BOTTOM_RIGHT=image(BOTTOM_RIGHT)
BOTTOM_LEFT=image(BOTTOM_LEFT)
'''


tree = {'describers': [{'describers': [{'describers': [], 'head': 'un', 'part': 'adv'}, {'describers': [{'describers': [{'describers': [{'describers': [], 'head': 'joj', 'part': 'noun'}], 'head': 'fi7', 'part': 'prep'}], 'head': 'joj', 'part': 'noun'}], 'head': 'ot', 'part': 'prep'}], 'head': 'ric', 'part': 'adj'}], 'head': 'xox', 'part': 'noun'}
tree = {'part': 'noun', 'describers': [{'part': 'adj', 'describers': [{'part': 'adverboid', 'describers': [], 'head': 'xo'}, {'part': 'prep', 'describers': [{'part': 'noun', 'describers': [{'part': 'adj', 'describers': [], 'head': 'co'}], 'head': '0a0'}], 'head': 'u0'}, {'part': 'prep', 'describers': [{'part': 'noun', 'describers': [{'part': 'adj', 'describers': [], 'head': 'co'}], 'head': 'joj'}], 'head': 'ot'}], 'head': '8ec'}], 'head': 'xox'}

def border(text):
	minx = -text.origin[0]-1
	miny = -text.origin[1]-1
	maxx = minx+text.getWidth()+1
	maxy = miny+text.getLength()+1

	text = text.overlay(image(TOP_LEFT),minx,miny)
	text = text.overlay(image(TOP_RIGHT),maxx,miny)
	text = text.overlay(image(BOTTOM_LEFT),minx,maxy)
	text = text.overlay(image(BOTTOM_RIGHT),maxx,maxy)

	text = text.fill(minx+1,miny,maxx,miny+1,TOP)
	text = text.fill(minx+1,maxy,maxx,maxy+1,TOP)
	text = text.fill(minx,miny+1,minx+1,maxy,SIDE)
	text = text.fill(maxx,miny+1,maxx+1,maxy,SIDE)
	return text

def draw(head,tails):
	drawing = head
	oldy = 0
	y = 0
	x = drawing.getWidth()
	for i in range(0,len(tails)):
		desc = drawPhrase(tails[i])
		if i == len(tails)-1:
			if i == 0:
				connection = HOR
			else:
				connection = DOWN_RIGHT
		else:
			if i == 0:
				connection = HOR_DOWN
			else:
				connection = VERT_RIGHT
		connection = image(connection)
		y = y + desc.getLength()
		start = oldy#+desc.origin[1]
		oldy = y
		if (tails[i].zhozh == True) and (tails[i].part == 'n'):
			desc = border(desc)
			

		drawing = drawing.overlay(connection,x,start)
		drawing = drawing.overlay(desc,x+desc.origin[0]+1,start)
		if (tails[i].zhozh == True) and (tails[i].part != 'n'):
			return draw(border(drawing),tails[i+1:])
	return drawing

def drawPhrase(tree):
	return draw(image(str(tree.head)),tree.desc)

def asciiimage(x):
	return image(x)

#print(draw(tree))
