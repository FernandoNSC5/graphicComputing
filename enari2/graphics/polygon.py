#####################################################################
##                                                                 ##
##  #######  ####     ##    ######    ######    ###  ####     ##   ##
##  ##       ######   ##   ##    ##   ##   ##   ###  ######   ##   ##
##  ##       ##  ###  ##  ##      ##  ##    ##  ###  ##  ###  ##   ##
##  #######  ##   ### ##  ##      ##  ##    ##  ###  ##   ### ##   ##
##  ##       ##    #####  ##########  #######   ###  ##    #####   ##
##  ##       ##     ####  ##      ##  ##   ##   ###  ##     ####   ##
##  #######  ##      ###  ##      ##  ##    ##  ###  ##      ###   ##
##                                              JUST WORKS         ##
#####################################################################
##                                                                 ##
##   Fernando Nogueira Da Silva Costa                              ##
##   Gabriel Ferrari Carvalho                                      ##
##   João Pedro Silvino Paes                                       ##
##   Pedro Miranda Santos Bueno dos Reis                           ##
##                                                                 ##
#####################################################################

from node import Node as Nd

class Polygon:

    def __init__(self, filled):
        self.nodes = []
        self.color = (255, 255, 255)
        self.width = 2
        self.filled = filled
        self.visible = True

    #######################################
    ##  Methods
    #######################################

    def alterPosition(self, x, y):
        for n in range(len(self.nodes)):
            _x = nodes[n].getX()
            _y = nodes[n].getY()
            nodes[n].setX(_x+x)
            nodes[n].setY(_y+y)
    
    def push(self, node):
        self.nodes.append(node.getPos())
        
    def pop(self, pos):
        try:
            return self.nodes.pop(pos)
        except Exception:
            raise "Node not found."

    def changePolygonSize(self, newSize, op):
        newSize = int(newSize)
        if(op):
            for i in range(len(self.nodes)):
                if i == 0: continue
                self.nodes[i] = [self.nodes[i][0]+newSize, self.nodes[i][1]+newSize]
        else:
            for i in range(len(self.nodes)):
                if i == 0: continue
                self.nodes[i] = [self.nodes[i][0]-newSize, self.nodes[i][1]-newSize]
        
    def popFirst(self):
        try:
            return self.nodes.pop(0)
        except Exception:
            raise "Polyline doesn't have any nodes."
        
    def popLast(self):
        try:
            return self.nodes.pop()
        except Exception:
            raise "Polyline doesn't have any nodes."
    
    def changeColor(self, color):
        self.setColor(color)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def fill(self):
        self.filled = 1
    
    def deplenish(self):
        self.filled = 0
    
    def isVisible(self):
        return self.visible == 1

    def isFilled(self):
        return self.filled == 1
        
    #######################################
    ##  Getters and Setters
    #######################################

    def getNodes(self):
        return self.nodes

    def getColor(self):
        return self.color

    def getWidth(self):
        return self.width

    def setNodes(self, nodes):
        self.nodes = nodes

    def setColor(self, color):
        self.color = color

    def setWidth(self, width):
        self.width = width
