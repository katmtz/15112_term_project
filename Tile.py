
"""
File Info:
    
    Defines tiles as a subclass of Entity.

    Defines 5 different kinds of tiles, 2 blocking and 3 normal.

    Each kind of map tile has a boolean blocking attribute and takes
    coordinates x and y in its init.

"""
import pygame
from Entity import Entity

class MapTile(Entity):
    def __init__(self,image,x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        super(MapTile, self).__init__()

    def update(self):
        pass

class BlockingTile1(MapTile):
    def __init__(self,x,y):
        self.blocking = True
        self.image = pygame.image.load("media/sprites/blocking1.png").convert()
        super(BlockingTile1, self).__init__(self.image,x,y)

class BlockingTile2(MapTile):
    def __init__(self,x,y):
        self.blocking = True
        self.image = pygame.image.load("media/sprites/blocking2.png").convert()
        super(BlockingTile2,self).__init__(self.image,x,y)

class GroundTile1(MapTile):
    def __init__(self,x,y):
        self.blocking = False
        self.image = pygame.image.load("media/sprites/ground1.png").convert()
        super(GroundTile1,self).__init__(self.image,x,y)

class GroundTile2(MapTile):
    def __init__(self,x,y):
        self.blocking = False
        self.image = pygame.image.load("media/sprites/ground2.png").convert()
        super(GroundTile2,self).__init__(self.image,x,y)

class GroundTile3(MapTile):
    def __init__(self,x,y):
        self.blocking = False
        self.image = pygame.image.load("media/sprites/ground3.png").convert()
        super(GroundTile3,self).__init__(self.image,x,y)

class ItemTile(MapTile):
    def __init__(self,x,y,active):
        self.blocking = False
        self.x = x
        self.y = y
        self.active = active
        if (active):
            self.image = pygame.image.load("media/sprites/item.png").convert()
        else:
            self.image = pygame.image.load("media/sprites/ground1.png").convert()
        super(ItemTile, self).__init__(self.image,x,y)

    def update(self,active):
        self.__init__(self.x,self.y,active)
