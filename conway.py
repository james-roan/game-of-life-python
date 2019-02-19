# conways game of life

from GameOfLife import Board
import os, time

#

dimensions = (10, 10)
b = Board(dimensions)
b.placeBlinker((4,4))
#b.printBoard()
#print(b._alive(1,2))
#b.tick()
#b.printBoard()

while True:
	os.system('clear')
	b.printBoard()
	b.tick()
	time.sleep(1)
	pass