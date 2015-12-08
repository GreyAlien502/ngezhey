from ASCIIImage.asciiimage import asciiimage as image

from phrase import phrase
'''
word--word-+-word
           |
           +-word
	'''
mode = 8

if mode == 7:
#Connections
	HOR = image('-')
	HOR_DOWN = image('+')
	DOWN_RIGHT = image('`')
	VERT_RIGHT = image('+')
	VERT = image('|')
#Boudaries
	TOP =          image('-')
	SIDE =         image('|')
	TOP_RIGHT =    image('.')
	TOP_LEFT =     image(',')
	BOTTOM_RIGHT = image("'")
	BOTTOM_LEFT =  image('`')
else:
#Connections
	HOR = image('─')
	HOR_DOWN = image('┬')
	DOWN_RIGHT = image('└')
	VERT_RIGHT = image('├')
	VERT = image('│')
#Boudaries
	TOP =          image('─')
	SIDE =         image('│')
	TOP_RIGHT =    image('┐')
	TOP_LEFT =     image('┌')
	BOTTOM_RIGHT = image('┘')
	BOTTOM_LEFT =  image('└')

tree = {'describers': [{'describers': [{'describers': [], 'head': 'un', 'part': 'adv'}, {'describers': [{'describers': [{'describers': [{'describers': [], 'head': 'joj', 'part': 'noun'}], 'head': 'fi7', 'part': 'prep'}], 'head': 'joj', 'part': 'noun'}], 'head': 'ot', 'part': 'prep'}], 'head': 'ric', 'part': 'adj'}], 'head': 'xox', 'part': 'noun'}
tree = {'part': 'noun', 'describers': [{'part': 'adj', 'describers': [{'part': 'adverboid', 'describers': [], 'head': 'xo'}, {'part': 'prep', 'describers': [{'part': 'noun', 'describers': [{'part': 'adj', 'describers': [], 'head': 'co'}], 'head': '0a0'}], 'head': 'u0'}, {'part': 'prep', 'describers': [{'part': 'noun', 'describers': [{'part': 'adj', 'describers': [], 'head': 'co'}], 'head': 'joj'}], 'head': 'ot'}], 'head': '8ec'}], 'head': 'xox'}

def border(text):
	minx = -text.origin[0]-1
	miny = -text.origin[1]-1
	maxx = minx+text.getWidth()+1
	maxy = miny+text.getLength()+1

	text = text.overlay(TOP_LEFT,minx,miny)
	text = text.overlay(TOP_RIGHT,maxx,miny)
	text = text.overlay(BOTTOM_LEFT,minx,maxy)
	text = text.overlay(BOTTOM_RIGHT,maxx,maxy)

	text = text.fill(minx+1,miny,maxx,miny+1,TOP)
	text = text.fill(minx+1,maxy,maxx,maxy+1,TOP)
	text = text.fill(minx,miny+1,minx+1,maxy,SIDE)
	text = text.fill(maxx,miny+1,maxx+1,maxy,SIDE)
	text.origin[0]=text.origin[0]-1
	return text

def draw(head,tails):
	drawing = head
	oldy = 0
	y = 0
	x = drawing.getWidth()
	for i in range(0,len(tails)):
		desc = drawPhrase(tails[i])
		if i == 0:
			drawing = drawing.overlay(HOR,x,y)
			drawing = drawing.overlay(desc,x+1,y)
		elif i == 1:
			drawing = drawing.overlay(HOR_DOWN,x,oldy)
			drawing = drawing.fill(x,oldy+1,x+1,y+desc.origin[1],VERT)
			drawing = drawing.overlay(DOWN_RIGHT,x,y+desc.origin[1])
			drawing = drawing.overlay(desc,x+1,y+desc.origin[1])
		else:
			drawing = drawing.overlay(VERT_RIGHT,x,oldy)
			drawing = drawing.fill(x,oldy+1,x+1,y+desc.origin[1],VERT)
			drawing = drawing.overlay(DOWN_RIGHT,x,y+desc.origin[1])
			drawing = drawing.overlay(desc,x+1,y+desc.origin[1])
		oldy = y
		y = y + desc.maxy()
		if (tails[i].zhozh == True) and (tails[i].part == 'n'):
			desc = border(desc)
		if (tails[i].zhozh == True) and (tails[i].part != 'n'):
			return draw(border(drawing),tails[i+1:])

	return drawing

def drawPhrase(tree):
	return draw(image(str(tree.head)),tree.desc)

def asciiimage(x):
	return image(x)

#print(draw(tree))
