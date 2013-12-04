"""
File Info:
	
	Define Entity type as a kind of pygame sprite.
	Could be used to define other types of entites 
	beyond the Player class.
	
"""

import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self):
		super(Entity,self).__init__()

