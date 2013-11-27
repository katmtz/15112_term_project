"""
File Info:

	Creates Player subclass of Entity.

	This is the user controlled sprite.

	Functions:
	- updates rect
	- checks for collisions with walls
	- bounds movement to just the map

	(add functions for item handling, health, attacks later)
"""
import pygame
from Entity import Entity

class Player(Entity):
	def __init__(self):

		# image and rect load
		self.image = pygame.image.load("temp media/temp player sprite.png")#.convert_alpha()
		self.rect = self.image.get_rect()
		(self.imageRectX,self.imageRectY) = self.rect.topleft

		# movement constant
		self.velocity = 25

		# directions
		self.movingUp = False
		self.movingDown = False
		self.movingLeft = False
		self.movingRight = False
		super(Player,self).__init__()

	def update(self, up, down, left, right):
		# updates sprite according to key presses
		self.velocity = 25

		# these are all boolean values
		self.movingUp = up
		self.movingDown = down
		self.movingLeft = left
		self.movingRight = right

		# changes rect in response to key presses
		if (self.movingUp):
			self.imageRect.topleft = (self.imageRectX, self.imageRectY-self.velocity)
		elif (self.movingDown):
			self.imageRect.topleft = (self.imageRectX, self.imageRectY+self.velocity)
		elif (self.movingLeft):
			self.imageRect.topleft = (self.imageRectX-self.velocity,self.imageRectY)
		elif (self.movingRight):
			self.imageRect.topleft = (self.imageRectX+self.velocity,self.imageRectY)
		self.boundMovement()

	def collide(self,walls):
		# checks for collisions with blocking tiles
		for wall in walls:
			if pygame.self.collide_rect(self,wall):
				self.velocity = 0

	def boundMovement(self):
		# keeps the sprite from walking off the map
		leftEdge,topEdge,width,height = self.imageRect
		if (leftEdge <= 0):
			leftEdge = 0
		elif (leftEdge >= 2000 - width):
			leftEdge = 2000 - width
		if (topEdge <= 0):
			topEdge = 0
		elif (topEdge >= 2000 - width):
			topEdge = 2000 - width
		self.imageRect = leftEdge,topEdge,width,height

