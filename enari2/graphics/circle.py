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

class Circle:

    def __init__(self, center, radius, filled):
        self.center = center
        self.radius = radius
        self.color = (255, 255, 255)
        self.filled = filled
        self.width = 2
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

    def getCenter(self):
        return self.center.getPos()

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def getWidth(self):
        return self.width

    def setCenter(self, center):
        self.center = center

    def setRadius(self, radius):
        self.radius = int(radius)

    def setColor(self, color):
        self.color = color

    def setWidth(self, width):
        self.width = width
