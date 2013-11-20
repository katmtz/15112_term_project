"""
File Info:

	Features:
	- runs title menu

	This is the modifiable, progress file. 

	If shit gets fucked up, go back to one of the old saves.
	That's why they're there.

	Never turn this file in for anything ever.
"""

import pygame

def keyPressed(event,data):
	# wrapper function, calls keyPressed for current mode
	if (event.key == pygame.K_q):
		pygame.quit()
		data.mode == "Done"
	# title screen mode
	if (data.mode == "title"):
		titleKeyPressed(event,data)

def titleKeyPressed(event,data):
	# handles title mode key presses
	selections = ["start","load","quit"]
	i = data.titleIndex# selection index
	if (event.key == pygame.K_UP):
		print ">up press"
		print "initial i:", i
		i = (i - 1)%3
		print "changed i:", i 
		data.titleSelection = selections[i]
		data.titleIndex = i
		print "selection",data.titleSelection
	elif (event.key == pygame.K_DOWN):
		print ">down press"
		print "initial i:", i
		i = (i + 1)%3
		print "changed i:", i
		data.titleSelection = selections[i]
		data.titleIndex = i
		print data.titleSelection
	elif (event.key == pygame.K_RETURN):
		if (data.titleSelection == "start"):
			data.mode = "story" # run game
		elif (data.titleSelection == "load"):
			pass # open load menu
		elif (data.titleSelection == "quit"):
			pygame.quit() # quit the game

def mousePressed(event,data):
	pass

def timerFired(data):
	redrawAll(data)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			data.mode = "Done"
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mousePressed(event,data)
		elif event.type == pygame.KEYDOWN:
			keyPressed(event,data)

def redrawAll(data):
	data.screen.fill(data.colorBlack)
	if (data.mode == "title"):
		redrawTitle(data)
	elif (data.mode == "story"):
		redrawStory(data)
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
	data.screen.blit(data.storyBkg, [0,0])

def init(data):
	loadImages(data)
	loadColors(data)
	data.screenSize = [800,600]
	data.mode = "title"
	data.width = data.screenSize[0]
	data.height = data.screenSize[1]
	data.font = pygame.font.Font(None, 50)
	data.titleSelection = None
	data.titleIndex = 1

def loadImages(data):
	data.storyBkg = pygame.image.load("temp storycard.png")
	data.titleBkg = pygame.image.load("temp title menu.png")

def loadColors(data):
	data.colorBlack = (0,0,0)
	data.colorWhite = (255,255,255)
	data.hexDDDDAA = (221,221,170)
	data.hexCCBB88 = (204,187,136)

def run():
	pygame.init()

	class Struct(): pass
	data = Struct()

	init(data)

	data.screen = pygame.display.set_mode(data.screenSize)
	timerFired(data)

	while True:
		timerFired(data)

run()
