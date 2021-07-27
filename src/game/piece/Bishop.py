from src import DATA
from src.game.piece.Piece import Piece


class Bishop(Piece):

    def getPieceByCase(self, piecePosition):
        for piece in DATA.pieces:
            if piece.position[0] == piecePosition[0] and piece.position[1] == piecePosition[1]:
                return piece
        return None

    def getPlayableCases(self):
        playableCases = []
        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        currentRow = self.position[0]
        currentCol = self.position[1]
        for direction in directions:
            for i in range(1, 8):
                endRow = currentRow + i * direction[0]
                endCol = currentCol + i * direction[1]
                if 1 <= endCol <= 8 and 1 <= endRow <= 8:
                    casePiece = self.getPieceByCase((endRow, endCol))
                    if casePiece is None:
                        playableCases.append((endRow, endCol))
                    elif not casePiece.alive:
                        playableCases.append((endRow, endCol))
                    elif casePiece.isWhite != self.isWhite:
                        playableCases.append((endRow, endCol))
                        break
                    else:
                        break
                else:
                    break
        return playableCases

    def getAttackableCases(self):
        attackableCases = []
        for case in self.getPlayableCases():
            if self.getPieceByCase(case) is not None:
                attackableCases.append(case)
        return attackableCases

    def tryMoveTo(self, position):
        if self.getPlayableCases().__contains__(position):
            self.position = position
            self.hasAlreadyMoved = True
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None
