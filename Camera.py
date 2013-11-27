"""
File Info:
	
	Camera makes a rect that specifically displays an area around the player.
	Will stop scrolling if the edge of the map is reached.

"""

import pygame

class Camera(object):
    def __init__(self, cameraFunct, width, height):
        self.cameraFunct = cameraFunct
        self.state = Rect(0,0,width,height)
        
    def apply(self,target):
        return target.rect.move(self.state.topleft)

    def update(self,target):
        self.state = self.cameraFunct(self.state, target.rect)

def complexCamera(cameraRect, targetRect):
    tLeft, tTop, tWidth, tHeight = targetRect
    cLeft, cTop, cWidth, cHeight = cameraRect

    if (tLeft <= 0 or tLeft >= 2000 - cWidth):
    	left = cLeft
    else:
    	left = tLeft
    if (tTop <= 0 or tTop >= 2000 - cHeight):
    	top = cTop
    else:
    	top = tTop

    return Rect(left, top, cWidth, cHeight)