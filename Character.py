"""
File Info:
	
	**DON'T TURN THIS IN!!**

	Features:
	- defines Character class that can be subclassed into player and enemy.
	- Methods:
		- move
		- use attack (from attack list)
		- gain health (from item)
		- lose health (from attack)
		- *now loads all attributes here instead of subclasses

	data.vars added:
	- data.currentMap <= assumes map is an object w/ methods from map_generator
	- data.screenCenter
	- data.fieldLength
	- data.fieldHeight


"""

import pygame

class Character(pygame.sprite.Sprite):

	def __init__(self,data,image,location):

		super(Character,self).__init__()

		# import screen info from data
		self.screen = data.screen
		self.map = data.currentMap
		self.screenCenter = data.screenCenter
		self.fieldLength = data.fieldLength
		self.fieldHeight = data.fieldHeight

		# load image
		self.image = pygame.image.load(image).convert_alpha()
		self.imageSize = (50,50)
		# may add changing sprite with direction?

		self.rect = self.image.get_rect()
		self.radius = 25
		self.movement = 4 # does this need to stay?? not sure will check l8r
		self.speed = data.currentMap.scrollSpeed

		# ex. code has variables for animation here
		# im too lazy to do animation rn

		# initial position 
		self.x,self.y = location

		# other init variables here
		self.maxHealth = 100.0
		self.health = 100.0
		self.allItems = []
		self.defensiveItems = []
		self.offensiveItems = []
		self.keyItems = []
		self.attacks = []
		self.offensiveAttacks = []
		self.defensiveAttacks = []
		self.attackMult = 1.0
		self.defenseMult = 1.0
		self.level = 1
		self.status = "healthy"
		self.moveDir = "up"

	# skip load images function (for now)

	# skip animation function

	def move(self,data):
		# moves with the screen (screen movement not defined yet)
		self.moveDir = data.currentMap.scrollDir

		self.x = data.fieldLength/2
		self.y = data.fieldHeight/2

		self.rect.x = self.x
		self.rect.y = self.y

		self.screen.blit(self.image, )

	def useAttack(self):
		pass

	def gainHealth(self):
		pass

	def loseHealth(self):
		pass