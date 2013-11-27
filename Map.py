"""
File Info:
	
	Defines a map class as a subclass of Entity.

"""

import pygame, Tile

class Map(object):

    def __init__(self):
        self.scrollDir = None
        self.tiles = {}
        #self.camera = pygame.Rect((0, 0),resolution)        
        #self.atTop = False
        #self.atRight = False     
        #self.atLeft = False
        #self.atBottom = False
        #self.horizScroll = False   
        #self.vertScroll = False
        self.mapDim = 20
        #controls the speed the sprite walks around.
        self.scrollSpeed = 2
        self.mapSurface = pygame.Surface(self.mapDim*50,self.mapDim*)

        # sets tile size
        self.tileSize = (50,50)
        self.tileX = self.tileSize[0]
        self.tileY = self.tileSize[1]

        # load map
        buildFile(self.mapDim)
        self.mapStr = readMap("mapfiles/tempmap")
        self.mapWidth = self.mapDim*self.tileSize[0]
        self.mapHeight = self.mapDim*self.tileSize[1]

        # create map surface
        self.mapSurface = pygame.Surface(self.mapDim*self.tileX,self.mapDim*self.tileY)
"""

**not currently using this code**

        self.leftEdge = 0
        self.rightEdge = self.mapWidth - self.camera.w
        self.topEdge = 0
        self.bottomEdge = self.mapHeight - self.camera.w

    def boundsCheck(self):
        if (self.camera.x <= 0):
            self.atLeft = True
            self.camera.x = 0
        else:
            self.atLeft = False

        if (self.camera.y <= 0):
            self.atTop = True
            self.camera.y = 0
        else:
            self.atTop = False

        if (self.camera.x + self.camera.w >= self.rightEdge):
            self.atRight = True
            self.camera.x = self.rightEdge
        else:
            self.atRight = False

        if (self.camera.y + self.camera.h >= self.bottomEdge):
            self.atBottom = True
            self.camera.y = self.bottomEdge
        else:
            self.atBottom = False
"""
    def getTiles(self):
    	# sets tiles to specific locations and types based on their
    	# location in the map string and the character representing
    	# that tile
        for i in xrange(len(self.mapStr)):
            char = self.mapStr[i]
            (x,y) = self.getLocation(i)
            if (char == '#'):
                tile = BlockingTile1(self.blockTile1,x,y)

            elif (char == "!"):
                tile = BlockingTile2(self.blockTile2,x,y)

            elif (char == "."):
                tile = GroundTile3(self.groundTile3,x,y)

            elif (char == "-"):
                tile = GroundTile2(self.groundTile2,x,y)

            elif (char == '+'):
                tile = GroundTile1(self.GroundTile1,x,y)

            if (char != "\n"):
            	self.tiles[(x,y)] = tile
        return self.tiles

    def getLocation(self,index):
    	# uses string index to find position on map
    	row = index/(self.mapDim + 1)
    	col = index%(self.mapDim + 1)
    	(x,y) = (row*self.tileX, col*self.tileY)
    	return (x,y)

    def generate(self,screen):
    	# generate a full map

    	# populate tile dict
    	self.getTiles()

    	# draw to 
    	for row in xrange(self.mapDim):
    		for col in xrange(self.mapDim):
    			(x,y) = (row*self.tileX, col*self.tileY)
    			tile = self.tiles[(x,y)]
    			screen.blit(tile.image,(x,y))
