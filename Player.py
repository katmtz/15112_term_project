"""
File Info:

    Creates Player subclass of Entity.

    This is the user controlled sprite.

    Functions:
    - updates rect
    - checks for collisions with walls
    - bounds movement to just the map
    - tests if out of health
    - tests if player has collected 5 items
    
"""
import pygame
from Entity import Entity

class Player(Entity):
    def __init__(self):

        # image and rect load
        self.rightImage = pygame.image.load("media/sprites/playerright.png")
        self.leftImage = pygame.transform.flip(self.rightImage,True,False)
        self.frontImage = pygame.image.load("media/sprites/playerfront.png")
        self.backImage = pygame.image.load("media/sprites/playerback.png")
        self.image = self.rightImage
        self.imagesize = self.image.get_size()
        self.rect = self.image.get_rect()
        (self.imageRectX,self.imageRectY) = self.rect.topleft

        # movement constant
        self.velocity = 25

        # directions
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        self.health = 100.0
        self.items = 0

        super(Player,self).__init__()

    def update(self, up, down, left, right, walls):
        # updates sprite according to key presses
        self.velocity = 25

        # these are all boolean values
        self.movingUp = up
        self.movingDown = down
        self.movingLeft = left
        self.movingRight = right

        self.boundMovement()
        self.collide(walls)

        # changes rect in response to key presses
        if (self.movingUp):
            self.image = self.backImage
            self.imageRectX += 0
            self.imageRectY -= self.velocity
            self.rect.topleft = (self.imageRectX, self.imageRectY)
        elif (self.movingDown):
            self.image = self.frontImage
            self.imageRectX += 0
            self.imageRectY += self.velocity
            self.rect.topleft = (self.imageRectX, self.imageRectY)
        elif (self.movingLeft):
            self.image = self.leftImage
            self.imageRectX -= self.velocity
            self.imageRectY += 0
            self.rect.topleft = (self.imageRectX,self.imageRectY)
        elif (self.movingRight):
            self.image = self.rightImage
            self.imageRectX += self.velocity
            self.imageRectY += 0
            self.rect.topleft = (self.imageRectX,self.imageRectY)

        # resets directional flags
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

    def collide(self,walls):
        # checks for collisions with blocking tiles
        for wall in walls:
            if pygame.sprite.collide_rect(self,wall):
                self.health -= .5

    def boundMovement(self):
        # keeps the sprite from walking off the map
        (leftEdge,topEdge,width,height) = self.rect
        if (self.rect.left < 0):
            self.rect.left = 0
        elif (self.rect.left > (2000 - width)):
            self.rect.left = (2000 - width)
        if (self.rect.top < 0):
            self.rect.top = 0
        elif (self.rect.top > (2000 - width)):
            self.rect.top = (2000 - height)

    def hasHealth(self):
        # returns false if player is out of health
        if (self.health <= 0):
            return False
        return True

    def hasAllItems(self):
        # returns true if player has 5 items
        if (self.items >= 5):
            return True
        return False

