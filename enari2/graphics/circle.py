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

    def __init__(self, center, radius, color, fill):
        self.center = center
        self.radius = radius
        self.color = color
        self.fill = fill
        self.visible = False
        
    #######################################
    ##  Methods
    #######################################
    
    def changeColor(self, color):
        self.setColor(color)

    def show(self):
        self.center.show()
        self.visible = True

    def hide(self):
        self.center.hide()
        self.visible = False
        
    #######################################
    ##  Getters and Setters
    #######################################

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def getFill(self):
        return self.fill

    def setCenter(self, center):
        self.center = center

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def setFill(self, fill):
        self.fill = fill
