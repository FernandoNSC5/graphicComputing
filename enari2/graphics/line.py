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

from node import Node as nd

class Line:

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.width = 2
        self.color = (255, 255, 255)
        self.visible = True
        
    #######################################
    ##  Methods
    #######################################
    
    def changeColor(self, color):
        self.setColor(color)

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False

    def isVisible(self):
        return self.visible == 1

    def changeLineSize(self, newSize):
        self.width = int(newSize)
        
    #######################################
    ##  Getters and Setters
    #######################################

    def getNodes(self):
        return [self.node1, self.node2]

    def getNode1(self):
        return self.node1.getPos()

    def getNode2(self):
        return self.node2.getPos()

    def getColor(self):
        return self.color

    def getWidth(self):
        return self.width

    def setNodes(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def setNode1(self, node1):
        self.node1 = node1

    def setNode2(self, node2):
        self.node2 = node2

    def setColor(self, color):
        self.color = color

    def setWidth(self, width):
        self.width = width
