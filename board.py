import random
random.seed(5)

class Board(object):
	def __init__(self, boardSize):
		self.boardSize = boardSize
		self.board = [[0 for i in range(boardSize)] for j in range(boardSize)]
		self.moves = []

	def printBoard(self):
		colLine = "\t" + "\t".join([str(c) for c in range(self.boardSize)])
		print colLine
		print "-"*(len(colLine)*4+1)
		for r, row in enumerate(self.board):
			line = str(r) + "\t" + "\t".join([str(el) for el in row])
			print line

	def validateMove(self, move):
		try:
			y, x = int(move[0]),int(move[1])
			if y < 0 or x < 0 or y > self.boardSize or x > self.boardSize or self.board[y][x] != 0: 
				return 0
			return 1
		except ValueError:
			return 0

	def makeRandomMove(self, player):
		while True:
			y, x = random.randint(0, self.boardSize - 1), random.randint(0, self.boardSize - 1)
			if self.board[y][x] == 0:
				self.board[y][x] = player.playerNum
				self.moves.append([y,x])
				return y, x

	def makeMove(self, player):
		# Read in move
		move = raw_input("%s, enter your next move (row,col): " % player.name).split(",")
		while not self.validateMove(move):
			print "Invalid Move"
			move = raw_input("%s, enter your next move (row,col): " % player.name).split(",")

		y, x = int(move[0]), int(move[1])
		self.board[y][x] = player.playerNum
		self.moves.append([y,x])
		return y, x

	def checkForNeighbor(self, x, y, playerNum, direction=None):
		count = 0
		# left
		if x > 0 and (direction == "left" or direction == None):
			if self.board[y][x-1] == playerNum:
				count = 1 + self.checkForNeighbor(x-1, y, playerNum, "left")
		
		# right
		if count < 5:
			count = 0
			if x < self.boardSize - 1 and (direction == "right" or direction == None):
				if self.board[y][x+1] == playerNum:
					count = 1 + self.checkForNeighbor(x+1, y, playerNum, "right")
		# up
		if count < 5:
			count = 0
			if y > 0 and (direction == "up" or direction == None):
				if self.board[y-1][x] == playerNum:

					count = 1 + self.checkForNeighbor(x, y-1, playerNum, "up")
		# down
		if count < 5:
			count = 0
			if y < self.boardSize - 1 and (direction == "down" or direction == None):
				if self.board[y+1][x] == playerNum:
					count = 1 + self.checkForNeighbor(x, y+1, playerNum, "down")
		
		# up/left
		if (x > 0 and y > 0) and (direction == "up/left" or direction == None):
			if self.board[y-1][x-1] == playerNum:
				count = 1 + self.checkForNeighbor(x-1, y-1, playerNum, "up/left")
		
		# up/right
		if count < 5:
			count = 0
			if (x < self.boardSize - 1 and y > 0) and (direction == "up/right" or direction == None):
				if self.board[y-1][x+1] == playerNum:
					count = 1 + self.checkForNeighbor(x+1, y-1, playerNum, "up/right")
		# down/left
		if count < 5:
			count = 0
			if (x > 0 and y > self.boardSize - 1) and (direction == "down/left" or direction == None):
				if self.board[y+1][x-1] == playerNum:
					count = 1 + self.checkForNeighbor(x-1, y+1, playerNum, "down/left")
		# down/right
		if count < 5:
			count = 0
			if (x < self.boardSize -1 and y < self.boardSize - 1) and (direction == "down/right" or direction == None):
				if self.board[y+1][x+1] == playerNum:
					count = 1 + self.checkForNeighbor(x+1, y+1, playerNum, "down/right")
		return count

	def checkForCapture(self, player, waitingPlayer):
		y,x = self.moves[-1]
		pNum = player.playerNum
		wpNum = waitingPlayer.playerNum
		numCaptures = 0
		# Left
		if x > 2:
			if self.board[y][x-3] == pNum and self.board[y][x-2] == wpNum and self.board[y][x-1] == wpNum:
				print "CAPTURE!"
				self.board[y][x-2], self.board[y][x-1] = 0,0
				numCaptures += 1
		# Right
		if x < self.boardSize - 3:
			if self.board[y][x+3] == pNum and self.board[y][x+2] == wpNum and self.board[y][x+1] == wpNum:
				print "CAPTURE!"
				self.board[y][x+2], self.board[y][x+1] = 0,0
				numCaptures += 1
		# Up
		if y > 2:
			if self.board[y-3][x] == pNum and self.board[y-2][x] == wpNum and self.board[y-1][x] == wpNum:
				print "CAPTURE!"
				self.board[y-2][x], self.board[y-1][x] = 0,0
				numCaptures += 1
		# Down
		if y < self.boardSize - 3:
			if self.board[y+3][x] == pNum and self.board[y+2][x] == wpNum and self.board[y+1][x] == wpNum:
				print "CAPTURE!"
				self.board[y+2][x], self.board[y+1][x] = 0,0
				numCaptures += 1

		# Left/Up
		if x > 2 and y > 2:
			if self.board[y-3][x-3] == pNum and self.board[y-2][x-2] == wpNum and self.board[y-1][x-1] == wpNum:
				print "CAPTURE!"
				self.board[y-2][x-2], self.board[y-1][x-1] = 0,0
				numCaptures += 1

		# Right/Up
		if x < self.boardSize - 3 and y > 2:
			if self.board[y-3][x+3] == pNum and self.board[y-2][x+2] == wpNum and self.board[y-1][x+1] == wpNum:
				print "CAPTURE!"
				self.board[y-2][x+2], self.board[y-1][x+1] = 0,0
				numCaptures += 1

		# Left/Down
		if x > 2 and y < self.boardSize - 3:
			if self.board[y+3][x-3] == pNum and self.board[y+2][x-2] == wpNum and self.board[y+1][x-1] == wpNum:
				print "CAPTURE!"
				self.board[y+2][x-2], self.board[y+1][x-1] = 0,0
				numCaptures += 1

		# Right/Down
		if x < self.boardSize - 3 and y < self.boardSize - 3:
			if self.board[y+3][x+3] == pNum and self.board[y+2][x+2] == wpNum and self.board[y+1][x+1] == wpNum:
				print "CAPTURE!"
				self.board[y+2][x+2], self.board[y+1][x+1] = 0,0
				numCaptures += 1

		return numCaptures

	def checkFor5Recursive(self):
		for y in range(self.boardSize):
			for x in range(self.boardSize):
				if self.board[y][x] != 0:
					playerNum = self.board[y][x]
					if self.checkForNeighbor(x, y, playerNum) == 4:
						print "5 IN A ROW! Player %d wins" % playerNum



