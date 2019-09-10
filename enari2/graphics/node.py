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

class Node:

    def __init__(self, x, y):
        print("[SYSTEM] Node class created")
        self.x = x
        self.y = y
        self.color = '#FFFFFF'
        self.visible = False


    #######################################
    ##  Methods
    #######################################

    def moveTo(self, x, y):
        self.setPos(x, y)

    def changeColor(self, color):
        self.color = color

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False
        
    #######################################
    ##  Getters and Setters
    #######################################

    def getPos(self):
        return [self.x, self.y]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getColor(self):
        return self.color

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setColor(self, color):
        self.color = color
