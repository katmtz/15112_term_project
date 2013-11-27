"""
File Info:

	Features:
	- runs title menu
	- shows game's story introduction
	- loads and displays map
	- *opens load menu, can select from different "load files"

	This is the modifiable, progress file. 

"""
import pygame
from mapOutput import *
from Camera import *
from Tile import * 
from Map import Map
from Player import Player
from Enemy import Enemy

###########################################################
# Event Handling
###########################################################

def keyPressed(event,data):
	# wrapper function, calls keyPressed for current mode
	if (event.key == pygame.K_ESCAPE):
		pygame.quit()
		data.mode == "Done"
	# title screen mode
	if (data.mode == "title"):
		titleKeyPressed(event,data)
	elif (data.mode == "story"):
		storyKeyPressed(event,data)
	elif (data.mode == "load"):
		loadKeyPressed(event,data)
	elif (data.mode == "game"):
		gameKeyPressed(event,data)

def titleKeyPressed(event,data):
	# handles title mode key presses
	selections = ["start","load","quit"]
	i = data.titleIndex# selection index

	# key presses iterate through a list of possible menu selections
	if (event.key == pygame.K_UP):
		i = (i - 1)%3
		data.titleSelection = selections[i]
		data.titleIndex = i
	elif (event.key == pygame.K_DOWN):
		i = (i + 1)%3
		data.titleSelection = selections[i]
		data.titleIndex = i
	elif (event.key == pygame.K_RETURN):
		if (data.titleSelection == "start"):
			data.mode = "story" # run game
		elif (data.titleSelection == "load"):
			data.mode = "load"
		elif (data.titleSelection == "quit"):
			pygame.quit() # quit the game

def loadKeyPressed(event,data):
	# load file menu key presses
	if (event.key == pygame.K_BACKSPACE):
		data.mode = "title"
	elif (event.key == pygame.K_UP):
		data.loadSelection = (data.loadSelection - 1)%3
	elif (event.key == pygame.K_DOWN):
		data.loadSelection = (data.loadSelection + 1)%3
	elif (event.key == pygame.K_RETURN):
		i = data.loadSelection
		loadedFile = data.saveFiles[i]
		loadFile(data,loadedFile)
		
def storyKeyPressed(event,data):
	# story card key presses
	if (event.key == pygame.K_BACKSPACE):
		data.mode = "title"
	elif (event.key == pygame.K_RETURN and data.currentPanel <= 5): # move through story cards
		data.currentPanel += 1
		if (data.currentPanel == 2):
			data.map = Map()
			data.tiles = data.map.getTiles()
		elif (data.currentPanel == 3):
			for key in data.tiles:
				tile = data.tiles[key]
				if (tile.blocking):
					data.blockingTiles.append(tile)
		elif (data.currentPanel == 4):
			data.mode = "game"


def gameKeyPressed(event,data):
	# updates player while in game
	if (event.key == pygame.K_UP):
		data.player.update(True,False,False,False,data.blockingTiles)

	elif (event.key == pygame.K_DOWN):
		data.player.update(False,True,False,False,data.blockingTiles)

	elif (event.key == pygame.K_LEFT):
		data.player.update(False,False,True,False,data.blockingTiles)

	elif (event.key == pygame.K_RIGHT):
		data.player.update(False,False,False,True,data.blockingTiles)

	# check for collisions with blocking tiles
	data.player.collide(data.blockingTiles)

	# updates camera view
	data.camera.update(data.player)
	data.camera.apply(data.player)

def timerFired(data):
	redrawAll(data)
	data.camera.update(data.player)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			data.mode = "Done"
		elif event.type == pygame.KEYDOWN:
			keyPressed(event,data)

###########################################################
# Draw Functions
###########################################################

def redrawAll(data):
	# redrawAll wrapper function
	data.screen.fill(data.colorBlack)
	if (data.mode == "title"):
		redrawTitle(data)
	elif (data.mode == "story"):
		redrawStory(data)
	elif (data.mode == "load"):
		redrawLoad(data)
	elif (data.mode == "game"):
		redrawGame(data) 
	pygame.display.flip()

def redrawTitle(data):
	# draws title menu
	data.screen.blit(data.titleBkg, [0,0])
	pygame.draw.rect(data.screen,data.hexDDDDAA,[data.width/3,3*data.height/5,
		data.width/3,data.width/5])
	titleHighlight(data)
	startGame = data.font.render("Start Game", False, data.colorWhite)
	loadGame = data.font.render("Load Game", False, data.colorWhite)
	quitGame = data.font.render("Quit", False, data.colorWhite)
	data.screen.blit(startGame, [45 + data.width/3,10 + 3*data.height/5])
	data.screen.blit(loadGame, [45 + data.width/3, 65 + 3*data.height/5])
	data.screen.blit(quitGame, [90 + data.width/3, 115 + 3*data.height/5])

def titleHighlight(data):
	selection = data.titleSelection
	if (selection == "start"):
		pygame.draw.rect(data.screen,data.hexCCBB88, [data.width/3,3*data.height/5,
		data.width/3,55]) # highlight start
	elif (selection == "load"):
		pygame.draw.rect(data.screen,data.hexCCBB88, [data.width/3,55 + 3*data.height/5,
		data.width/3,55]) # highlight load
	elif (selection == "quit"):
		pygame.draw.rect(data.screen,data.hexCCBB88, [data.width/3,110 + 3*data.height/5,
		data.width/3,55]) # highlight quit 

def redrawStory(data):
	# draws the story cards

	# intro panels
	if (data.currentPanel == 1):
		data.screen.blit(data.storycard1, [0,0])
	elif (data.currentPanel == 2):
		data.screen.blit(data.storycard2, [0,0])
	elif (data.currentPanel == 3):
		data.screen.blit(data.storycard3, [0,0])
	# game running
	elif (data.currentPanel == 4):
		pass
	# ending panel
	elif (data.currentPanel == 5):
		pass
	else:
		data.screen.fill(data.colorBlack)

def redrawLoad(data):
	# draws the file loading menu
	data.screen.blit(data.loadBkg, [0,0])
	loadHighlight(data)
	displayFiles(data)

def loadHighlight(data):
	# highlights the current selection in the load menu
	selection = data.loadSelection # integer 0-2
	(listX0,listY0,listX1,listY1) = (40,100,data.width-41,data.height-107)
	listHeight = listY1 - listY0
	listWidth = listX1 - listX0
	entryHeight  = 22 + listHeight/3

	rect = [listX0,listY0 + selection*entryHeight,listWidth,entryHeight]
	pygame.draw.rect(data.screen,data.hexBBBBAA,rect)

def displayFiles(data):
	# shows a list of all saved files
	(listX0,listY0,listX1,listY1) = (40,100,data.width-41,data.height-107)
	listHeight = listY1 - listY0
	listWidth = listX1 - listX0
	entryHeight  = 22 + listHeight/3

	files = data.saveFiles # returns a list of filenames
	if (len(files) > 3):
		# something's wrong, there should never be more than 3 files
		print "!!!! MORE THAN 3 FILES !!!!"
	for i in xrange(len(files)):
		filename = files[i]
		msg = "Load file: %s" % filename
		dispMsg = data.font.render(msg, False, data.colorWhite)
		position = [listX0 + 10, 10 + listY0 + i*entryHeight]
		data.screen.blit(dispMsg, position)

def redrawGame(data):
	# draw map tiles
	for row in xrange(data.map.mapDim):
		for col in xrange(data.map.mapDim):
			(x,y) = (row*data.map.tileY,col*data.map.tileX)
			currTile = data.tiles[(x,y)]
			data.screen.blit(currTile.image, (x,y))
	data.screen.blit(data.player.image, data.camera.apply(data.player))




###########################################################
# Data Loading/Management
###########################################################

def getFiles(data):
	# eventually will open filesaves, get files, and return their names
	return ["file one","file two", "file three"]

def loadFile(data,filename):
	# placeholder function for when I have eventual saved data
	print "%s loaded." % filename
	data.mode = "play"

def init(data):
	loadImages(data)
	loadColors(data)

	data.saveFiles = getFiles(data)
	data.screenSize = [800,600]
	data.mode = "title"
	data.width = data.screenSize[0]
	data.height = data.screenSize[1]
	data.font = pygame.font.Font(None, 50)
	data.mapDim = 2000 # map is square, don't need rows and cols
	data.titleSelection = None
	data.titleIndex = 3
	data.loadSelection = 0
	data.currentPanel = 1
	data.blockingTiles = []
	data.player = Player()
	data.camera = Camera(complexCamera, data.mapDim, data.mapDim)

def loadImages(data):
	data.imgIcon = pygame.image.load("temp media/icon.png")
	data.storycard1 = pygame.image.load("media/storycard1.png")
	data.storycard2 = pygame.image.load("media/storycard2.png")
	data.storycard3 = pygame.image.load("media/storycard3.png")
	data.titleBkg = pygame.image.load("temp media/temp title menu.png")
	data.loadBkg = pygame.image.load("temp media/load menu.png")
	# this vv is a place holder for where the game should g0
	data.tempPlayCard = pygame.image.load("temp media/temp play.png") 

def loadColors(data):
	data.colorBlack = (0,0,0)
	data.colorWhite = (255,255,255)
	data.hexDDDDAA = (221,221,170)
	data.hexCCBB88 = (204,187,136)
	data.hexBBBBAA = (187,187,170)

###########################################################
# Run Game
###########################################################

def run():
	pygame.init()

	class Struct(): pass
	data = Struct()

	init(data)

	data.screen = pygame.display.set_mode(data.screenSize)
	pygame.display.set_caption("im gonna think of a name for this eventually")
	pygame.display.set_icon(data.imgIcon)

	timerFired(data)

	while True:
		timerFired(data)

run()
