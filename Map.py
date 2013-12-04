"""
File Info:
	
	Defines a map class as a subclass of Entity.

"""

import pygame
from mapOutput import *
from Tile import *

class Map(object):

    def __init__(self):
        self.tiles = {}
        self.mapDim = 40

        # sets tile size
        self.tileSize = (50,50)
        self.tileX = self.tileSize[0]
        self.tileY = self.tileSize[1]

        # load map
        buildFile(self.mapDim)
        self.mapStr = readMap("mapfiles/tempmap")
        self.mapWidth = self.mapDim*self.tileSize[0]
        self.mapHeight = self.mapDim*self.tileSize[1]

    def getTiles(self):
    	# sets tiles to specific locations and types based on their
    	# location in the map string and the character representing
    	# that tile
        for i in xrange(len(self.mapStr)):
            char = self.mapStr[i]
            (x,y) = self.getLocationFromIndex(i)
            if (i == 0 or i == 1):
                currTile = GroundTile3(x,y)
            elif (char == "i"):
                currTile = ItemTile(x,y,True)
            elif (char == '#'):
                currTile = BlockingTile1(x,y)

            elif (char == "!"):
                currTile = BlockingTile2(x,y)

            elif (char == "."):
                currTile = GroundTile3(x,y)

            elif (char == "-"):
                currTile = GroundTile2(x,y)

            elif (char == '+'):
                currTile = GroundTile1(x,y)

            if (char != "\n"):
            	self.tiles[(x,y)] = currTile
        return self.tiles

    def getLocationFromIndex(self,index):
    	# uses string index to find position on map
    	row = index/(self.mapDim + 1)
    	col = index%(self.mapDim + 1)
    	(x,y) = (col*self.tileX,row*self.tileY)
    	return (x,y)

    def generate(self,screen):
    	# generate a full map
    	# draw to screen
    	for row in xrange(self.mapDim):
    		for col in xrange(self.mapDim):
    			(x,y) = (col*self.tileX,row*self.tileY)
    			tile = self.tiles[(x,y)]
    			screen.blit(tile.image,(x,y))
