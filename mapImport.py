"""
File Info:
	
	Loads and reads the current tempmap file.
	Should be used both at initMap and at saveStates.

"""

def readMap():
	try:
		with open("mapfiles/tempmap", 'r') as f:
			mapStr = ""
			for line in f:
				mapStr += line
		print mapStr
	except IOError as e:
   		print "I/O error({0}): {1}".format(e.errno, e.strerror)

readMap()