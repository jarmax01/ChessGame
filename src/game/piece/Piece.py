from array import array
from enum import Enum

from src import DATA


class Piece:

    def __init__(self, position, alive, pieceType, isWhite):
        self.position = position
        self.alive = alive
        self.pieceType = pieceType
        self.isWhite = isWhite

    def getImage(self):
        if self.isWhite:
            return DATA.images["w"+self.pieceType.firstLetter]
        else:
            return DATA.images["b"+self.pieceType.firstLetter]

    def getPlayableCases(self):
        pass

    def getAttackableCases(self):
        pass

    def tryMoveTo(self, position):
        pass

    moves = []

class PieceType(Enum):
    PAWN = 1,"P"
    BISHOP = 3,"B"
    KNIGHT = 3,"N"
    ROOK = 5,"R"
    KING = 0,"K"
    QUEEN = 9,"Q"

    def __init__(self, piecePoint, firstLetter):
        self.piecePoint = piecePoint
        self.firstLetter = firstLetter
