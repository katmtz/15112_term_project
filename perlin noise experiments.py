"""
File Info:
	**noise functions adapted from pseudocode by Hugo Elias**

	Features:
	- can generate a basic demonstration of how tile distribution will look on a larger
	map. (uses Tkinter)
"""

import random
import math
from Tkinter import *

#############################################
# basic functions
#############################################

def createMap(dimension):
	# creates an empty 2D list of specified size
	emptyMap = [[0 for i in xrange(dimension)] for i in xrange(dimension)]
	return emptyMap

def getInts(r):
	# given a set range, generate 2 random integers in a tuple
	int1 = random.randint(0,r)
	int2 = random.randint(0,r)
	return (int1, int2)

############################################
# noise generation
############################################

def interpolate(a, b, x):
	# smoothes curves
	f = (1 - math.cos(math.pi * x)) * .5
	return a*(1 - f) + b*f

def noise(x,y):
	# primary random noise function
	n = x + y*57
	n = (n<<13) ^ n
	return (1.0 - ( (n* (n**2 * 15731 + 789221) + 1376312589) 
		& 0x7fffffff) / 1073741824.0)

def smoothNoise(x,y):
	# initial smoothing
	corners = (noise(x - 1, y - 1) + noise(x + 1, y - 1) + 
		noise(x - 1, y + 1) + noise(x + 1, y + 1))/16 
	sides = (noise(x-1, y)  + noise(x + 1, y)  + noise(x, y - 1) +
		noise(x, y+1))/8
	center = noise(x,y)/4
	return corners + sides + center

def interpolNoise(x,y):
	# uses interpolation funct to smooth edges
	xInt = int(x)
	yInt = int(y)

	xFract = x - xInt
	yFract = y - yInt

	v1 = smoothNoise(xInt, yInt)
	v2 = smoothNoise(xInt + 1, yInt)
	v3 = smoothNoise(xInt, yInt + 1)
	v4 = smoothNoise(xInt + 1, yInt + 1)

	i1 = interpolate(v1, v2, xFract)
	i2 = interpolate(v3, v4, xFract)

	return interpolate(i1, i2, yFract)

def perlin2DNoise(x,y,persistence,n):
	# ties all the previous functions together
	total = 0
	for i in xrange(n):
		freq = 2**i
		amplitude = persistence**i
		total += interpolNoise(x*freq, y*freq) * amplitude
	return total

###########################################################
# map generation and filters
###########################################################

def makeSomeNoise(emptyMap):
	# applies noise funtion to each element of the an empty map
	(rows,cols) = (len(emptyMap),len(emptyMap[0]))
	persistence = .5
	n = 3
	for row in xrange(rows):
		for col in xrange(cols):
			(x,y) = getInts(5)
			offset = x
			tile = perlin2DNoise(row,col,persistence,n)
			emptyMap[row][col] = tile*offset
	return emptyMap


#########################################################################
# graphical test of perlin noise
#########################################################################

def createTexture(noiseMap):
	# init
	(rows,cols) = (len(noiseMap),len(noiseMap[0]))
	root = Tk()
	squareSize = 10
	cWidth = squareSize*cols
	cHeight  = squareSize*rows
	canvas = Canvas(root,width=cWidth,height=cHeight)
	canvas.pack()

	# draw
	for row in xrange(rows):
		for col in xrange(cols):
			color = getColor(noiseMap,row,col)
			color = '#%s' %color
			x0,y0 = col*squareSize,row*squareSize
			x1,y1 = x0 + squareSize,y0 + squareSize
			canvas.create_rectangle(x0,y0,x1,y1, fill = color)

	# launch app
	root.title("perlin noise!")
	root.mainloop()

def getColor(noiseMap,row,col):
	value = noiseMap[row][col]
	if (value > 1):
		color = 'bb9977'
	elif (value < 1 and value > .5):
		color = '998877'
	elif (value < .5 and value >= 0):
		color = '887766'
	elif (value < 0 and value > -1):
		color = '997766'
	else:
		color = 'ccbb88'
	return color

emptyMap = createMap(80)
noisyMap = makeSomeNoise(emptyMap)
createTexture(noisyMap)

