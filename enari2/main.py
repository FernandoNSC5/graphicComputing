# Import a library of functions called 'pygame'
import os
import pygame
from math import pi
import sys
sys.path.append('graphics')
import circle
import line
import time
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
_COLOR = WHITE


###############################################
##
##  Geometric Types - INIT
#####################################################
#Nodes Example
nodeA_ForLine = node.Node(5, 5)
nodeB_ForLine = node.Node(10, 10)

#Dots Example
_nodes = list()

#Lines example
_lines = list()

#Circle Example
_circles = list()

#Polygon Example
_polygons = list()

#Polyline Example
_polylines = list()

#############################################################
 
size = [1000, 800]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Enarin")

done = False
_SLEEP_TIME = 2
clock = pygame.time.Clock()
 
while not done:

	########################################################
	##
	##  User "interface"
	##################################################################
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print("SELECT WHAT TO DRAW:")
	print("0: Node")
	print("1: Line")
	print("2: Circle")
	print("3: Polygon")
	print("4: Polyline")
	print("5: Change Sizes")
	print("6: Move X|Y")
	print("7: Exit")

	_STRUCTURE = int(input("\nACTION: "))
	os.system('cls' if os.name == 'nt' else 'clear')

	if(_STRUCTURE == 0):
		print("####################\nNODE\n####################")
		print("PLEASE, ENTER THE VALUES:")
		x = int(input("X: "))
		y = int(input("Y: "))
		_nodes.append(node.Node(x, y))

	elif(_STRUCTURE == 1):
		print("####################\nLINE\n####################")
		print("PLEASE, ENTER THE VALUES:")
		x = int(input("X1: "))
		y = int(input("Y1: "))
		node1 = node.Node(x, y)
		x = int(input("X2: "))
		y = int(input("Y2: "))
		node2 = node.Node(x, y)
		_lines.append(line.Line(node1, node2))

	elif(_STRUCTURE == 2):
		print("####################\nCIRCLE\n####################")
		print("PLEASE, ENTER THE VALUES:")
		x = int(input("X: "))
		y = int(input("Y: "))
		radius = int(input("Radius: "))
		filled = int(input("Filled(0 => False, 1 => True): "))
		_circles.append(circle.Circle(node.Node(x, y), radius, filled))

	elif(_STRUCTURE == 3):
		print("####################\nPOLYGON\n####################")
		filled = int(input("Filled(0 => False, 1 => True): "))
		p = polygon.Polygon(filled)
		n = int(input("PLEASE, ENTER THE NUMBER OF NODES OF THIS POLYGON: "))
		for i in range(n):
			x = int(input("X" + str(i+1) + ": "))
			y = int(input("Y" + str(i+1) + ": "))
			p.push(node.Node(x, y))
		_polygons.append(p)

	elif(_STRUCTURE == 4):
		print("####################\nPOLYLINE\n####################")
		p = polyline.Polyline()
		n = int(input("PLEASE, ENTER THE NUMBER OF NODES OF THIS POLYLINE: "))
		for i in range(n):
			x = int(input("X" + str(i+1) + ": "))
			y = int(input("Y" + str(i+1) + ": "))
			p.push(node.Node(x, y))
		_polylines.append(p)

	elif(_STRUCTURE == 5):
		print("####################\nSIZE MODULATION\n####################")
		print("WHAT TO CHANGE:")
		print("a: Line")
		print("b: Circle")
		print("c: Polygon")
		print("d: Polyline")
		wtc = input()

		#####################################################################
		##	Listing existing elements
		#####################################################################
		if(wtc == 'a'):
			if(len(_lines) == 0):
				print("No line on screen")
				time.sleep(_SLEEP_TIME)
				continue
			else:
				counter = 0
				print("####################\nELEMENTS ON SCREEN\n####################\n")
				for i in _lines:
					print("Line " + str(counter))
					counter = counter + 1
				print("\n\n####################\nSELECT THE ELEMENT TO CHANGE\n####################\n")
				vetIndex = int(input("Element to change: "))
				newSize = input("New size: ")
				_lines[vetIndex].changeLineSize(newSize)
		elif(wtc == 'b'):
			if(len(_circles) == 0):
				print("No circles on screen")
				time.sleep(_SLEEP_TIME)
				continue
			else:
				counter = 0
				print("####################\nELEMENTS ON SCREEN\n####################\n")
				for i in _circles:
					print("Circle " + str(counter))
					counter = counter + 1
				print("\n\n####################\nSELECT THE ELEMENT TO CHANGE\n####################\n")
				vetIndex = int(input("Element to change: "))
				newSize = input("New radio size: ")
				_circles[vetIndex].setRadius(newSize)
		elif(wtc == 'c'):
			if(len(_polygons) == 0):
				print("No polygon on screen")
				time.sleep(_SLEEP_TIME)
				continue
			else:
				counter = 0
				print("####################\nELEMENTS ON SCREEN\n####################\n")
				for i in _polygons:
					print("Polygon " + str(counter))
					counter = counter + 1
				print("\n\n####################\nSELECT THE ELEMENT TO CHANGE\n####################\n")
				vetIndex = int(input("Element to change: "))
				print("\n\n####################\nIncrease size/Decrease size\n####################\n")
				print("0 - Increase")
				print("1 - Decrease")
				incDec = int(input())
				if(incDec):
					newSize = input("Pixel Decrease: ")
					_polygons[vetIndex].changePolygonSize(newSize, incDec)
				else:
					newSize = input("Pixel Increase: ")
					_polygons[vetIndex].changePolygonSize(newSize, incDec)
		#elif(wtc == 'd'):
		#elif(wtc == 'e'):
		else:
			print("Inexistent option")
			time.sleep(2)
			continue


	else:
		print("Thanks for using our humble code.")
		break


	##################################################################

	clock.tick(10)
	 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True 
	 
	screen.fill(BLACK)

	#Draw all nodes inside the _nodes vector
	for n in _nodes:
		if (n.isVisible()):
			screen.set_at((n.getX(), n.getY()), n.getColor())

	#Draw all lines inside the _lines vector
	for l in _lines:
		if (l.isVisible()):
			pygame.draw.line(screen, l.getColor(), l.getNode1(), l.getNode2(), l.getWidth())

	#Draws all circles inside the _circle vector
	for c in _circles:
		if (c.isVisible()):
			width = c.getWidth()
			if (c.isFilled()):
				width = 0
			pygame.draw.circle(screen, c.getColor(), c.getCenter(), c.getRadius(), width)

	#Draws all polygons inside the _polygons vector
	for p in _polygons:
		if (p.isVisible()):
			width = p.getWidth()
			if (p.isFilled()):
				width = 0
			pygame.draw.polygon(screen, p.getColor(), p.getNodes(), width)

	#Draws all polylines inside the _polylines vector
	for p in _polylines:
		if (p.isVisible()):
			print(p.getNodes())
			pygame.draw.lines(screen, p.getColor(), False, p.getNodes(), p.getWidth())

	#Update function based on clock
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()