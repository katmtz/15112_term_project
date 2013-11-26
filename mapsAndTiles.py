import pygame
from mapOutput import *

#############################################################
# Convert to Tile Objects
#############################################################
"""
First creates a basic map tile class - just an image with a rect.
Then creates 5 subclasses with each different type of image.
"""
class MapTile(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class BlockingTile1(MapTile):
    def __init__(self,image,x,y):
        self.blocking = True

        super(BlockingTile1, self).__init__(self,image,x,y)

class BlockingTile2(MapTile):
    def __init__(self,image,x,y):
        self.blocking = True

        super(BlockingTile2,self).__init__(self,image,x,y)

class GroundTile1(MapTile):
    def __init__(self,image,x,y):
        self.blocking = False

        super(GroundTile1,self).__init__(self,image,x,y)

class GroundTile2(MapTile):
    def __init__(self,image,x,y):
        self.blocking = False

        super(GroundTile2,self).__init__(self,image,x,y)

class GroundTile3(MapTile):
    def __init__(self,image,x,y):
        self.blocking = False

        super(GroundTile3,self).__init__(self,image,x,y)

class Map:

    def __init__(self,resolution):
        self.scrollDir = None
        self.tiles = []
        self.camera = pygame.Rect((0, 0),resolution)        
        self.atTop = False
        self.atRight = False     
        self.atLeft = False
        self.atBottom = False
        self.horizScroll = False   
        self.vertScroll = False
        self.mapDim = 20
        #controls the speed the sprite walks around.
        self.scrollSpeed = 2

        # load tiles
        self.blockTile1 = pygame.image.load("temp media/blocking1.png").convert()
        self.blockTile2 = pygame.image.load("temp media/blocking2.png").convert()
        self.groundTile1 = pygame.image.load("temp media/ground1.png").convert()
        self.groundTile2 = pygame.image.load("temp media/ground2.png").convert()
        self.groundTile3 = pygame.image.load("temp media/ground3.png").convert()

        # sets tile size
        self.tileSize = (50,50)
        self.tileX = self.tileSize[0]
        self.tileY = self.tileSize[1]

        # load map
        buildFile(self.mapDim)
        self.mapStr = readMap("mapfiles/tempmap")
        self.mapWidth = self.mapDim*self.tileSize[0]
        self.mapHeight = self.mapDim*self.tileSize[1]

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

    def getTiles(self):
        for i in xrange(len(self.mapStr)):
            char = self.mapStr[i]
            (x,y) = None 
            if (char == '#'):
                tile = BlockingTile1(self.blockTile1)
                tile.blit(tile.image)

            elif (char == "!"):
                tile = BlockingTile2(self.blockTile2)
                tile.blit(tile.image)

            elif (char == "."):
                tile = GroundTile3(self.groundTile3)
                tile.blit(tile.image)

            elif (char == "-"):
                tile = GroundTile2(self.groundTile2)
                tile.blit(tile.image)

            elif (char == '+'):
                tile = GroundTile1(self.GroundTile1)
                tile.blit(tile.image)

            self.tiles.append[tile]

pygame.init()
while True:
    screen = pygame.display.set_mode((800,600))
    testMap = Map((800,600))
    testMap.getTiles()
testMap.tiles
