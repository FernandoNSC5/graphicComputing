# Import a library of functions called 'pygame'
import pygame
from math import pi
import sys
sys.path.append('graphics')
import circle
import line
import node
import polygon
import polyline
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

###############################################
##
##  Control VAR
####################################################

# 0 -> dot
# 1 -> line
# 2 -> circle
# 3 -> polygon
_STRUCTURE = 0

# 0 -> black
# 1 -> white
# 2 -> blue
# 3 -> green
# 4 -> red
_COLOR = BLACK


###############################################
##
##  Geometric Types - INIT
#####################################################
#Nodes Example
nodeA_ForLine = node.Node(5, 5)
nodeB_ForLine = node.Node(10, 10)

#Dots Example
_dots = list()

#Lines example
_line = list()

#Circle Example
_circles = list()

#Polygon Example
_polygons = list()


#############################################################
 
size = [1000, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Enarin")

done = False
clock = pygame.time.Clock()
 
while not done:

	########################################################
	##
	##  User "interface"
	##################################################################
	
	print("####################")
	print("ADD AN:")
	print("0 - Dot")
	print("1 - Line")
	print("2 - Circle")
	print("3 - Polygon")

	_STRUCTURE = int(input())

	if(_STRUCTURE == 0):
		print("####################")
		print("ADD AN:")

	elif(_STRUCTURE == 1):
		print("####################")
		print("PLEASE, ENTER VALUE FOR: ")
		ax = int(input("Node A, X: "))
		ay = int(input("Node A, Y: "))
		bx = int(input("Node B, X: "))
		by = int(input("Node b, y: "))
		print("PLEASE, ENTER COLOR: ")
		print("0 - Black")
		print("1 - White")
		_COLOR = int(input())
		if(_COLOR):
			_COLOR = WHITE
		else:
			_COLOR = BLACK
		nodeA = node.Node(ax, ay)
		nodeB = node.Node(bx, by)
		_line.append(line.Line(nodeA, nodeB, 2, _COLOR))

	elif(_STRUCTURE == 2):
		print("####################")
		print("PLEASE, ENTER VALUE FOR CENTER: ")
		ax = int(input("Node A, X: "))
		ay = int(input("Node B, Y: "))
		raio = int(input("Radious: "))
		print("PLEASE, ENTER COLOR: ")
		print("0 - Black")
		print("1 - White")
		_COLOR = int(input())
		if(_COLOR):
			_COLOR = WHITE
		else:
			_COLOR = BLACK

		_circles.append(circle.Circle([ax, ay], raio, _COLOR))

	elif(_STRUCTURE == 3):
		print("####################")
		_num = int(input("Number of dots: "))
		_p = polygon.Polygon(BLACK, 5)
		for i in range(_num):
			a = int(input("X: "))
			b = int(input("Y: "))
			_n = node.Node(a, b)
			_p.push(_n)
		_polygons.append(_p)

	elif(_STRUCTURE == -1):
		done = True


	##################################################################

	clock.tick(10)
	 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True 
	 
	screen.fill(WHITE)

	#Draw all lines into _line vector
	for l in _line:
		pygame.draw.line(screen, l.getColor(), l.getNode1(), l.getNode2(), l.getSize())

	#Draws all circles into _circle vector
	for c in _circles:
		pygame.draw.circle(screen, c.getColor(), c.getCenter(), c.getRadius())

	#Draws all polygons into _polygons vextor
	for p in _polygons:
		pygame.draw.polygon(screen, p.getColor(), p.getNodes(), p.getSize())   

	#pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

	#Update function based on clock
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()