"""
File Info:

	Features:
	- runs title menu
	- *opens load menu, can select from different "load files"

	This is the modifiable, progress file. 

"""
import pygame, mapOutput, mapsAndTiles, Camera

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

def titleKeyPressed(event,data):
	# handles title mode key presses
	selections = ["start","load","quit"]
	i = data.titleIndex# selection index
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
	if (event.key == pygame.K_BACKSPACE):
		data.mode = "title"
	while (data.current != 4):
		if (event.key == pygame.K_RETURN):
			panelCounter += 1
			data.currentPanel += 1
	if (data.currentPanel == 4):
		initMap(data) # loads map file
		data.mode = "play"

def gameKeyPressed(event,data):
	if (event.key == pygame.K_UP):
		data.player.update(True,False,False,False)

	elif (event.key == pygame.K_DOWN):
		data.player.update(False,True,False,False)

	elif (event.key == pygame.K_LEFT):
		data.player.update(False,False,True,False)

	elif (event.key == pygame.K_RIGHT):
		data.player.update(False,False,False,True)
	player.collide(blockingTiles)

def timerFired(data):
	redrawAll(data)
	data.camera.update(data.player)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			data.mode = "Done"
		elif event.type == pygame.KEYDOWN:
			keyPressed(event,data)

def redrawAll(data):
	data.screen.fill(data.colorBlack)
	if (data.mode == "title"):
		redrawTitle(data)
	elif (data.mode == "story"):
		redrawStory(data)
	elif (data.mode == "load"):
		redrawLoad(data)
	elif (data.mode == "play"):
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
	# intro panels
	if (data.currentPanel == 1):
		data.screen.blit(data.storyBkg, [0,0])
	elif (data.currentPanel == 2):
		pass
	elif (data.currentPanel == 3):
		pass
	# game running
	elif (data.currentPanel == 4):
		pass
	# ending panel
	elif (data.currentPanel == 5):
		pass
	else:
		data.screen.fill(data.colorBlack)

def redrawLoad(data):
	data.screen.blit(data.loadBkg, [0,0])
	loadHighlight(data)
	displayFiles(data)

def loadHighlight(data):
	selection = data.loadSelection # integer 0-2
	(listX0,listY0,listX1,listY1) = (40,100,data.width-41,data.height-107)
	listHeight = listY1 - listY0
	listWidth = listX1 - listX0
	entryHeight  = 22 + listHeight/3

	rect = [listX0,listY0 + selection*entryHeight,listWidth,entryHeight]
	pygame.draw.rect(data.screen,data.hexBBBBAA,rect)

def displayFiles(data):
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
	# this will eventually be the game redrawAll function!!
	data.screen.blit(data.tempPlayCard,[0,0])

def getFiles(data):
	# eventually will open filesaves, get files, and return their names
	return ["file one","file two", "file three"]

def loadFile(data,filename):
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
	data.titleSelection = None
	data.titleIndex = 3
	data.loadSelection = 0
	data.currentPanel = 1
	data.player = Player(32,32)
	data.camera = Camera(complexCamera, 2000,2000) # 2000x2000 is map dimensions

def loadImages(data):
	data.imgIcon = pygame.image.load("temp media/icon.png")
	data.storyBkg = pygame.image.load("temp media/temp storycard.png")
	data.titleBkg = pygame.image.load("temp media/temp title menu.png")
	data.loadBkg = pygame.image.load("temp media/load menu.png")
	# this vv is a place holder for where the game should go???
	data.tempPlayCard = pygame.image.load("temp media/temp play.png") 

def loadColors(data):
	data.colorBlack = (0,0,0)
	data.colorWhite = (255,255,255)
	data.hexDDDDAA = (221,221,170)
	data.hexCCBB88 = (204,187,136)
	data.hexBBBBAA = (187,187,170)

def initMap(data):
	map = Map()

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
