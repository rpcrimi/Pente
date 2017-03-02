class Player(object):
	def __init__(self, name, playerNum):
		self.name = name
		self.captures = 0
		self.playerNum = playerNum
		self.initial = name[0].upper()