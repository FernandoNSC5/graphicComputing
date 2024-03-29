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

class Polyline:
    def __init__(self):
        self.nodes = []
        self.color = (255, 255, 255)
        self.width = 2
        self.visible = True

    #######################################
    ##  Methods
    #######################################
    def alterPosition(self, x, y):
        for n in range(len(self.nodes)):
            _x = self.nodes[n].getX()
            _y = self.nodes[n].getY()
            self.nodes[n].setX(_x+x)
            self.nodes[n].setY(_y+y)
    
    def push(self, node):
        self.nodes.append(node.getPos())
        
    def pop(self, pos):
        try:
            return self.nodes.pop(pos)
        except Exception:
            raise "Node not found."
        
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
    
    def isVisible(self):
        return self.visible == 1
        
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
