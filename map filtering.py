# map filter functions - this is on hold until i get the file i/o down

def getRandLocation(noisyMap):
	rows,cols = len(noisyMap), len(noisyMap[0])
	x,y = getInts(len(noisyMap))
	for row in xrange(rows):
		for col in xrange(cols):
			if (row == y and col == x):
				location = (row,col)
				if (areaClear(location, noisyMap)):
					return location
				else:
					return getRandLocation(noisyMap)

def areaClear(location,noisyMap):
	# should be called on a map with tile blocking established already???
	(row,col) = location
	dirs = [
	(-1,-1), (-1, 0), (-1,+1),
	( 0,-1),          ( 0,+1),
	(+1,-1), (+1, 0), (+1,+1)
	]
	for dir in dirs:
		drow,dcol = dir
		checkRow,checkCol = row + checkRow, col + checkCol
		if ("tile is blocking"): # tiles should be objects with possible 
		                         # blocking attribute
			return False
	return True

def addLocation(noisyMap):
	# i need to figure out how im gonna save maps first
	pass