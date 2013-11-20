"""
File Info: 
	
	**DON'T TURN THIS IN!!**

	Features:
	- player subclass of Character
	- sets player attributes
	- Methods:
		- pick up item (from location) <--hazy location description
		- place item (to location) <--hazy location description
		- learn attack
		- level up
		- reset to last save (if "died") <-- not written
		- [eventual AI attack??? or should this be in character class]

	This file is modifiable.

"""

from Character import Character

class Player(Character):
	# define attributes in init
	def __init__(self):
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
		self.location = (0,0) # not sure how to define this right now???
		self.status = "healthy"
		super(Player,self).__init__()

	def pickUpItem(self,location):
		# adds item from location to inventory if there's an item
		def itemInLocation(location):
			# not sure how to find location's type rn???
			if (location == "item"):
				return True
			return False

		# add item to list of all items and to type-specific lists 
		if (itemInLocation(location)):
			item = tile.getItem()
			allItems.append(item)
			if (item.getType() == "defensive"):
				defensiveItems.append(item)
			elif (item.getType() == "offensive"):
				offensiveItems.append(item)
			elif (item.getType() == "key"):
				keyItems.append(item)
			return True
		# returns False if no item
		return False

	def placeItem(self,location):
		# this function probably is gonna need lots of work
		def locationClear(location):
			# check if the tile can accept an item
			if location not in ["wall","item"]:
				return True
			return False

		# place item
		location =  "item"

	def learnAttack(self,attack):
		# adds attack to available attacks
		self.attacks.append(attack)
		if (attack.getType() == "offensive"):
			self.offensiveAttacks.append(attack)
		else:
			self.defensiveAttacks.append(attack)


	def levelUp(self):
		# increases players defense/offense multipliers + max health
		if (self.attackMult < 4):
			self.attackMult += .25
		if (self.defenseMult > .5):
			self.defenseMult -= .1
		self.maxHealth += 10

	def reset(self):
		# will return to this function when i determine how to access 
		# save states???
		pass