import math
from pprint import pprint

from player import Player
from board import Board
from pente import Pente

player1, player2 = Player("Bobby", 1), Player("Sam", 2)
board = Board(15)
pente = Pente(board, player1, player2)
pente.train(200)