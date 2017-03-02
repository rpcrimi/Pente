class Pente(object):
	def __init__(self, board, player1, player2):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		self.currentPlayer = player1
		self.waitingPlayer = player2
		self.fiveInARow = False
		self.moves = []

	def switchCurrentPlayer(self):
		if self.currentPlayer == self.player1:
			self.currentPlayer = self.player2
			self.waitingPlayer = self.player1
		else:
			self.currentPlayer = self.player1
			self.waitingPlayer = self.player2

	def checkForWinner(self):
		if self.player1.captures == 5:
			return self.player1
		elif self.player2.captures == 5:
			return self.player2
		elif self.fiveInARow:
			return self.currentPlayer
		else:
			return None


	def playGame(self):
		self.board.printBoard()
		while True:
			self.moves.append(self.board.makeMove(self.currentPlayer))
			self.currentPlayer.captures += self.board.checkForCapture(self.currentPlayer, self.waitingPlayer)
			self.fiveInARow = self.board.checkFor5()
			self.checkForWinner()
			self.switchCurrentPlayer()
			self.board.printBoard()


	def train(self, maxIter):
		for i in range(maxIter):
			self.moves.append(self.board.makeRandomMove(self.currentPlayer))
			self.currentPlayer.captures += self.board.checkForCapture(self.currentPlayer, self.waitingPlayer)
			self.fiveInARow = self.board.checkFor5()
			winner = self.checkForWinner()
			if winner:
				print "WINNER: Player %d" % winner.playerNum 
				print "Captures: %d" % winner.captures
				break
			self.switchCurrentPlayer()
			print ""
			self.board.printBoard()