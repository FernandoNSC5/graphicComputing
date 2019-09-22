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

    def __init__(self, node1, node2, size, color):
        self.node1 = node1
        self.node2 = node2
        self.size = size
        self.color = color
        self.visible = False
        
    #######################################
    ##  Methods
    #######################################
    
    def changeColor(self, color):
        self.setColor(color)

    def show(self):
        self.node1.show()
        self.visible = True

    def hide(self):
        self.node2.hide()
        self.visible = False
        
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

    def getSize(self):
        return self.size

    def setNodes(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def setNode1(self, node1):
        self.node1 = node1

    def setNode2(self, node2):
        self.node2 = node2

    def setColor(self, color):
        self.color = color

    def setSize(self, size):
        self.size = size
