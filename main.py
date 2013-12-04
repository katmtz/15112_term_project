import pygame
from mapOutput import *
from Camera import Camera
from Tile import * 
from Map import Map
from Player import Player

###########################################################
# Event Handling
###########################################################

def keyPressed(event,data):
    # wrapper function, calls keyPressed for current mode
    if (event.key == pygame.K_ESCAPE):
        raise SystemExit, "ESC"
        data.mode == "Done"
    # title screen mode
    if (data.mode == "title"):
        titleKeyPressed(event,data)
    elif (data.mode == "story"):
        storyKeyPressed(event,data)
    elif (data.mode == "instructions"):
        instKeyPressed(event,data)
    elif (data.mode == "game"):
        gameKeyPressed(event,data)
    elif (data.mode == "lose"):
        loseKeyPressed(event,data)
    elif (data.mode == "win"):
        winKeyPressed(event,data)

def titleKeyPressed(event,data):
    # handles title mode key presses
    selections = ["start","instructions","quit"]
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
        pygame.mixer.stop()
        if (data.titleSelection == "start"):
            pygame.mixer.stop()
            data.storyMus.play()
            data.mode = "story" # run game
        elif (data.titleSelection == "instructions"):
            pygame.mixer.stop()
            data.titleMus.play()
            data.mode = "instructions"
        elif (data.titleSelection == "quit"):
            pygame.quit() # quit the game
        
def storyKeyPressed(event,data):
    # story card key presses
    if (event.key == pygame.K_BACKSPACE):
        pygame.mixer.stop()
        data.titleMus.play()
        data.mode = "title"
    elif (event.key == pygame.K_RETURN and data.currentPanel <= 5): # move through story cards
        data.currentPanel += 1
        if (data.currentPanel == 2):
            # build map and tiles dictionary
            data.map = Map()
            data.tiles = data.map.getTiles()
        elif (data.currentPanel == 3):
            # add tiles to respective lists
            for key in data.tiles:
                tile = data.tiles[key]
                if (tile.blocking): # these are the "bad" tiles
                    data.blockingTiles.append(tile)
                elif (isinstance(tile,ItemTile)): # these are item tiles
                    if (tile.active):
                        data.itemTiles.append(tile)
        elif (data.currentPanel == 4):
            pygame.mixer.stop()
            data.gameMus.play()
            data.mode = "game"

def instKeyPressed(event,data):
    if (event.key == pygame.K_RETURN):
        pygame.mixer.stop()
        data.titleMus.play()
        data.mode = "title"

def gameKeyPressed(event,data):
    # updates player and camera while in game
    if (event.key == pygame.K_UP):
        data.player.update(True,False,False,False,data.blockingTiles)
        data.camera.getScrollDir(True,False,False,False)

    elif (event.key == pygame.K_DOWN):
        data.player.update(False,True,False,False,data.blockingTiles)
        data.camera.getScrollDir(False,True,False,False)

    elif (event.key == pygame.K_LEFT):
        data.player.update(False,False,True,False,data.blockingTiles)
        data.camera.getScrollDir(False,False,True,False)

    elif (event.key == pygame.K_RIGHT):
        data.player.update(False,False,False,True,data.blockingTiles)
        data.camera.getScrollDir(False,False,False,True)

    if (event.key == pygame.K_RETURN):
        # addds an item if player is on an item tile
        potentialItemGet(data)

    data.camera.moveRect()

def potentialItemGet(data):
    for item in data.itemTiles:
        if (data.player.rect.colliderect(item)):
            data.player.items += 1
            item.update(False)

def loseKeyPressed(event,data):
    if (event.key == pygame.K_r):
        init(data)

def winKeyPressed(event,data):
    if (event.key == pygame.K_r):
        pygame.mixer.stop()
        data.titleMus.play()
        data.mode = "title"

def timerFired(data):
    redrawAll(data)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit, "QUIT"
            data.mode = "Done"
        elif event.type == pygame.KEYDOWN:
            keyPressed(event,data)
    if not(data.player.hasHealth()):
        data.mode = "lose"
    if (data.player.hasAllItems()):
        data.mode = "win"

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
    elif (data.mode == "instructions"):
        redrawInst(data)
    elif (data.mode == "game"):
        redrawGame(data)
    elif (data.mode == "lose"):
        redrawLose(data)
    elif (data.mode == "win"):
        redrawWin(data)
    pygame.display.flip()

def redrawTitle(data):
    # draws title menu
    data.screen.blit(data.titleBkg, [0,0])

    # box background and highlight
    pygame.draw.rect(data.screen,data.hexF6E0A5, [data.width/3,3*data.height/5,
        data.width/3,data.width/5])
    titleHighlight(data)

    # write menu options
    startGame = data.font.render("Start Game", False, data.hex543A20)
    instructions = data.font.render("Instructions", False, data.hex543A20)
    quitGame = data.font.render("Quit", False, data.hex543A20)
    data.screen.blit(startGame, [75 + data.width/3,10 + 3*data.height/5])
    data.screen.blit(instructions, [75 + data.width/3, 65 + 3*data.height/5])
    data.screen.blit(quitGame, [105 + data.width/3, 115 + 3*data.height/5])

def titleHighlight(data):
    selection = data.titleSelection
    if (selection == "start"):
        pygame.draw.rect(data.screen,data.hexF07A55, [data.width/3,3*data.height/5,
        data.width/3,55]) # highlight start
    elif (selection == "instructions"):
        pygame.draw.rect(data.screen,data.hexF07A55, [data.width/3,55 + 3*data.height/5,
        data.width/3,55]) # highlight instructions
    elif (selection == "quit"):
        pygame.draw.rect(data.screen,data.hexF07A55, [data.width/3,110 + 3*data.height/5,
        data.width/3,55]) # highlight quit 

def redrawStory(data):
    # draws the story cards
    if (data.currentPanel == 1):
        data.screen.blit(data.storycard1, [0,0])
    elif (data.currentPanel == 2):
        data.screen.blit(data.storycard2, [0,0])
    elif (data.currentPanel == 3):
        data.screen.blit(data.storycard3, [0,0])
    # game running
    elif (data.currentPanel == 4):
        pass
    else:
        data.screen.fill(data.colorBlack)

def redrawInst(data):
    data.screen.blit(data.storycard3, [0,0])

def redrawGame(data):
    # draw map tiles
    for row in xrange(data.map.mapDim):
        for col in xrange(data.map.mapDim):
            (x,y) = (row*data.map.tileY,col*data.map.tileX)
            currTile = data.tiles[(x,y)]
            data.screen.blit(currTile.image, (x,y))

    # draw player and stats
    data.screen.blit(data.player.image, data.camera.state)
    drawHealth(data)
    drawItemCount(data)

def drawHealth(data):
    text = "Health:"
    healthMsg = data.font.render(text, False, data.colorWhite)
    msgPos = [10,data.height - 40]
    barLen = data.player.health
    barPos = [100, data.height - 40, barLen, 20]
    data.screen.blit(healthMsg,msgPos)
    pygame.draw.rect(data.screen, data.colorWhite, barPos)

def drawItemCount(data):
    itemCount = data.player.items
    if (itemCount == 0):
        text = "Items Collected: None"
    else:
        text = "Items Collected: %d" % itemCount
    textPos = [data.width-250,data.height-40]
    itemMsg = data.font.render(text, False, data.colorWhite)
    data.screen.blit(itemMsg,textPos)
                     
def redrawLose(data):
    data.screen.blit(data.losecard, [0,0])

def redrawWin(data):
    data.screen.blit(data.wincard, [0,0])
    
###########################################################
# Data Loading/Management
###########################################################

def init(data):
    # load media
    loadImages(data)
    loadColors(data)
    loadSounds(data)

    data.screenSize = [800,600]
    data.mode = "title"
    data.width = data.screenSize[0]
    data.height = data.screenSize[1]
    data.font = pygame.font.Font("media/8514oem.fon", 100)
    data.mapDim = 2000 # map is square, don't need rows and cols
    data.titleSelection = 0
    data.titleIndex = 3
    data.currentPanel = 1
    data.blockingTiles = []
    data.itemTiles = []
    data.player = Player()
    data.camera = Camera(data)
    data.titleMus.play()

def loadImages(data):
    data.imgIcon = pygame.image.load("media/icon.png")
    data.storycard1 = pygame.image.load("media/storycard1.png")
    data.storycard2 = pygame.image.load("media/storycard2.png")
    data.storycard3 = pygame.image.load("media/storycard3.png")
    data.titleBkg = pygame.image.load("media/titlecard.png")
    data.losecard = pygame.image.load("media/losecard.png")
    data.wincard = pygame.image.load("media/wincard.png")

def loadColors(data):
    data.colorBlack = (0,0,0)
    data.colorWhite = (255,255,255)
    data.hexDDDDAA = (221,221,170)
    data.hexCCBB88 = (204,187,136)
    data.hexBBBBAA = (187,187,170)
    data.hex543A20 = (84,58,32)
    data.hexF6E0A5 = (246,244,165)
    data.hexF07A55 = (240,122,85)
 
def loadSounds(data):
    data.titleMus = pygame.mixer.Sound("media/audio/Soft Breeze.wav")
    data.storyMus = pygame.mixer.Sound("media/audio/Crystal Cave.wav")
    data.gameMus = pygame.mixer.Sound("media/audio/Ruinous Laments.wav")

###########################################################
# Run Game
###########################################################

def run():
    pygame.init()

    class Struct(): pass
    data = Struct()

    init(data)

    data.screen = pygame.display.set_mode(data.screenSize)
    pygame.display.set_caption("Restoration")
    pygame.display.set_icon(data.imgIcon)
    pygame.mouse.set_visible(False)
    pygame.key.set_repeat(150)

    timerFired(data)

    while True:
        timerFired(data)

run()
