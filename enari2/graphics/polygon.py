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
    def __init__(self, color, fill):
        self.nodes = []
        self.color = color
        self.fill = fill
        self.visible = False

    #######################################
    ##  Methods
    #######################################
    
    def push(self, node):
        self.nodes.append(node)
        
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
        for i in range(len(self.nodes)):
            self.nodes[i].show()
        self.visible = True

    def hide(self):
        for i in range(len(self.nodes)):
            self.nodes[i].hide()
        self.visible = False
        
    #######################################
    ##  Getters and Setters
    #######################################

    def getNodes(self):
        return self.nodes

    def getColor(self):
        return self.color

    def getFill(self):
        return self.fill

    def setNodes(self, nodes):
        self.nodes = nodes

    def setColor(self, color):
        self.color = color

    def setFill(self, fill):
        self.fill = fill
