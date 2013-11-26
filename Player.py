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

import pygame, Entity

class Player(Entity):
	def __init__(self,x,y):

		# image and rect load
		self.image = pygame.image.load("temp media/temp player sprite.png").convert()
		self.imageRect = self.image.get_rect()
		(self.imageRectX,self.imageRectY) = self.imageRect.topleft

		# movement constant
		self.velocity = 25

		# directions
		self.movingUp = False
		self.movingDown = False
		self.movingLeft = False
		self.movingRight = False

	def update(self, up, down, left, right):
		self.velocity = 25

		# gets information from keyPressed
		self.movingUp = up
		self.movingDown = down
		self.movingLeft = left
		self.movingRight = right

		# changes rect in response to keyPressed
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
		for wall in walls:
			if pygame.self.collide_rect(self,wall):
				self.velocity = 0

	def boundMovement(self):
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

