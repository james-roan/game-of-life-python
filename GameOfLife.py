# GameOfLife.py

from pprint import pprint

""" Board is stored in _board where coords are _board[y][x] """
class Board():
	def __init__(self, dimensions):
		# dimensions should be a 2 element tuple
		#print(len(dimensions))
		if (dimensions[0] <= 1) | (dimensions[1] <= 1):
			#print('INCORRECT DIMESIONS')
			raise ValueError('Dimensions must be greater than one')

		self.dimensions = dimensions
		self.zeroBoard()

	def zeroBoard(self):
		"""used to clear the board"""
		#print('zeroBoard called')
		self._board = [[0] * self.dimensions[0] for _ in range(self.dimensions[1])]
		#self._board[1][2] = 1
		#self.printBoard()

	def printBoard(self):
		pprint(self._board)
		
	def placeConwayObject(self, obj, cord):
		"""TODO"""
		pass

	def placeBlinker(self, cord):
		self._board[cord[1]][cord[0] + 0] = 1
		self._board[cord[1]][cord[0] + 1] = 1
		self._board[cord[1]][cord[0] + 2] = 1
		#self.printBoard()

	def _alive(self, row, col):
		"""
		Rules:
		* If a cell has less than 2 live neighbors, it will die (or stay dead)
		* If a cell has 2 live neighbors, it will stay its current state
		* If a cell has 3 live neighbors, it will be alive
		(either by staying alive or coming alive)
		* If a cell has move than 3 live neighbors, it will die (or stay dead)

		Live neighbors are calculated by looking at its octile neighbors. That is
		for a cell X, you look at the neighbors A-H as in:

		A B C
		D X E
		F G H

		Note that a cell does not itself count towards its own live neighbor count 
		"""
		neighbors = 0
		for i in range(-1,2):
			for k in range(-1,2):
				try:
					neighbors += self._board[row+i][col+k]
				except IndexError:
					# if the element is out of range, we count it as a zero (i.e. do nothing)
					pass
			pass
		pass
		neighbors -= self._board[row][col]
		#print('neighbors:',neighbors)

		# Determine fate
		if (neighbors > 3):
			return 0
		elif (neighbors == 3):
			return 1
		elif (neighbors < 2):
			return 0
		elif (neighbors == 2):
			return self._board[row][col]

	def tick(self):
		self._tboard = [[0] * self.dimensions[0] for _ in range(self.dimensions[1])]
		for i in range(len(self._board)):
			for k in range(len(self._board[i])):
				self._tboard[i][k] = self._alive(i,k)
				pass
			pass
		self._board = self._tboard