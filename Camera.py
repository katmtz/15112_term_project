"""
File Info:
	
	Camera makes a rect that specifically displays an area around the player.
	Will stop scrolling if the edge of the map is reached.

"""

import pygame

class Camera(object):
    def __init__(self,data):
        width = data.width
        height = data.height
        self.state = pygame.Rect(0,0,width,height)
        self.halfHeight = height/2
        self.halfWidth = width/2

        # directional flags
        self.leftScroll = False
        self.rightScroll = False
        self.upScroll = False
        self.downScroll = False

        self.scrollSpeed = data.player.velocity
        self.target = data.player
        
    def getScrollDir(self,up,down,left,right):
        # changes flags according to keypresses
        self.upScroll = up
        self.downScroll = down
        self.rightScroll = right
        self.leftScroll = left
        
    def moveRect(self):
        # moves the rect
        if (self.upScroll):
            self.state.centery -= self.scrollSpeed
        elif (self.downScroll):
            self.state.centery += self.scrollSpeed
        elif (self.leftScroll):
            self.state.centerx -= self.scrollSpeed
        elif (self.rightScroll):
            self.state.centerx += self.scrollSpeed
        
        # reverses movement if out of bounds
        if (self.checkBounds() == False):
            if (self.upScroll):
                self.state.centery += self.scrollSpeed
            elif (self.downScroll):
                self.state.centery -= self.scrollSpeed
            elif (self.leftScroll):
                self.state.centerx += self.scrollSpeed
            elif (self.rightScroll):
                self.state.centerx -= self.scrollSpeed
       
    def checkBounds(self):
        # checks that state rect is not out of bounds
        if (self.state.top < 0):
            return False
        elif (self.state.left < 0):
            return False
        elif (self.state.right > 2000):
            return False
        elif (self.state.bottom > 2000):
            return False
        return True
        
        
        
        
        
        
        
