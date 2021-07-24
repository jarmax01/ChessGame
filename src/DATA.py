import DATA as DATA
import pygame as pygame

from src.game.piece import *
from src.game.piece.Bishop import Bishop
from src.game.piece.King import King
from src.game.piece.Knight import Knight
from src.game.piece.Pawn import Pawn

from src.game.piece.Piece import PieceType
from src.game.piece.Queen import Queen
from src.game.piece.Rook import Rook

HEIGHT = 800
WIDTH = 800
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION

images = {}

pieces = {
    Rook((1, 1), True, PieceType.ROOK, False),
    King((2, 1), True, PieceType.KNIGHT, False),
    Bishop((3, 1), True, PieceType.BISHOP, False),
    Queen((4, 1), True, PieceType.QUEEN, False),
    King((5, 1), True, PieceType.KING, False),
    Bishop((6, 1), True, PieceType.BISHOP, False),
    Knight((7, 1), True, PieceType.KNIGHT, False),
    Rook((8, 1), True, PieceType.ROOK, False),

    Pawn((1, 2), True, PieceType.PAWN, False),
    Pawn((2, 2), True, PieceType.PAWN, False),
    Pawn((3, 2), True, PieceType.PAWN, False),
    Pawn((4, 2), True, PieceType.PAWN, False),
    Pawn((5, 2), True, PieceType.PAWN, False),
    Pawn((6, 2), True, PieceType.PAWN, False),
    Pawn((7, 2), True, PieceType.PAWN, False),
    Pawn((8, 2), True, PieceType.PAWN, False),

    Pawn((1, 7), True, PieceType.PAWN, True),
    Pawn((2, 7), True, PieceType.PAWN, True),
    Pawn((3, 7), True, PieceType.PAWN, True),
    Pawn((4, 7), True, PieceType.PAWN, True),
    Pawn((5, 7), True, PieceType.PAWN, True),
    Pawn((6, 7), True, PieceType.PAWN, True),
    Pawn((7, 7), True, PieceType.PAWN, True),
    Pawn((8, 7), True, PieceType.PAWN, True),

    Rook((1, 8), True, PieceType.ROOK, True),
    King((2, 8), True, PieceType.KNIGHT, True),
    Bishop((3, 8), True, PieceType.BISHOP, True),
    Queen((4, 8), True, PieceType.QUEEN, True),
    King((5, 8), True, PieceType.KING, True),
    Bishop((6, 8), True, PieceType.BISHOP, True),
    Knight((7, 8), True, PieceType.KNIGHT, True),
    Rook((8, 8), True, PieceType.ROOK, True),
}



def loadImages():
    piecesName = ["bB", "bK", "bN", "bP", "bQ", "bR", "wB", "wK", "wN", "wP", "wQ", "wR"]
    for pieceName in piecesName:
        print("ressources/"+pieceName+".png")
        images[pieceName] = pygame.transform.scale(pygame.image.load("/Users/maxime/PycharmProjects/ChessProject/ressources/"+pieceName+ ".png"), (DATA.SQ_SIZE,DATA.SQ_SIZE))

