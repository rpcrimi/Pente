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
		doCheckLeft = True
		doCheckRight = True
		doCheckUp = True
		doCheckDown = True
		for direction in self.checkedDirections:
			if direction == "left":
				doCheckLeft = False
			if direction == "right":
				doCheckRight = False
			if direction == "up":
				doCheckUp = False
			if direction == "down":
				doCheckDown = False
		# left
		if x > 0 and (direction == "left" or direction == None) and doCheckLeft:
			if self.board[y][x-1] == playerNum:
				return "left"
		# right
		if x < self.boardSize - 1 and (direction == "right" or direction == None) and doCheckRight:
			if self.board[y][x+1] == playerNum:
				return "right"
		# up
		if y > 0 and (direction == "up" or direction == None) and doCheckUp:
			if self.board[y-1][x] == playerNum:
				return "up"
		# down
		if y < self.boardSize - 1 and (direction == "down" or direction == None) and doCheckDown:
			if self.board[y+1][x] == playerNum:
				return "down"
		return "nothing"

	def checkFor5(self):
		# go through each point, if we find a number, look for neighbor with the same number
		# checkforneighbor returns direction it found
		# has an optional direction it is looking for
		# need to mark what directions we've checked already and failed
		for x in range(self.boardSize):
			for y in range(self.boardSize):
				# check for number
				if self.board[y][x] > 0:
					playerNum = self.board[y][x]
					currentX = x
					currentY = y
					self.checkedDirections = [];
					currentDirection = self.checkForNeighbor(currentX, currentY, playerNum)
					if currentDirection != "nothing":
						self.checkedDirections.append(currentDirection)
					while currentDirection != "nothing":
						count = 0
						if currentDirection == "left":
							currentX = currentX - 1
							currentY = y
							while self.checkForNeighbor(currentX, currentY, playerNum, "left") != "nothing":
								count += 1
								currentX = currentX - 1
								if count == 5:
									return True
						if currentDirection == "right":
							currentX = currentX + 1
							currentY = y
							while self.checkForNeighbor(currentX, currentY, playerNum, "left") != "nothing":
								count += 1
								currentX = currentX + 1
								if count == 5:
									return True
						if currentDirection == "up":
							currentY = currentY - 1
							currentX = x
							while self.checkForNeighbor(currentX, currentY, playerNum, "left") != "nothing":
								count += 1
								currentY = currentY - 1
								if count == 5:
									return True
						if currentDirection == "down":
							currentY = currentY + 1
							currentX = x
							while self.checkForNeighbor(currentX, currentY, playerNum, "left") != "nothing":
								count += 1
								currentY = currentY + 1
								if count == 5:
									return True
						currentDirection = self.checkForNeighbor(x, y, playerNum)
						if currentDirection != "nothing":
							self.checkedDirections.append(currentDirection)
		return False

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


