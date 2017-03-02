class Pente(object):
	def __init__(self, board, player1, player2):
		self.board = board
		self.player1 = player1
		self.player2 = player2
		self.currentPlayer = player1
		self.waitingPlayer = player2

	def switchCurrentPlayer(self):
		if self.currentPlayer == self.player1:
			self.currentPlayer = self.player2
			self.waitingPlayer = self.player1
		else:
			self.currentPlayer = self.player1
			self.waitingPlayer = self.player2

	def checkForWinner(self):
		if self.player1.captures == 5:
			return player1
		elif self.player2.captures == 5:
			return player2
		# Check for 5 in a row

	def playGame(self):
		self.board.printBoard()
		while True:
			self.board.makeMove(self.currentPlayer)
			numCaptures = self.board.checkForCapture(self.currentPlayer, self.waitingPlayer)
			if numCaptures:
				self.currentPlayer.captures += numCaptures
			self.checkForWinner()
			self.switchCurrentPlayer()
			self.board.printBoard()
