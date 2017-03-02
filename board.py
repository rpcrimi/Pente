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

	def makeMove(self, player):
		# Read in move
		move = raw_input("%s, enter your next move (row,col): " % player.name).split(",")
		while not self.validateMove(move):
			print "Invalid Move"
			move = raw_input("%s, enter your next move (row,col): " % player.name).split(",")

		y, x = int(move[0]), int(move[1])
		self.board[y][x] = player.playerNum
		self.moves.append([y,x])
		return y,x

	def checkFor5(self):
		return

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


