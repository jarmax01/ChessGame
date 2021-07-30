from src import DATA
from src.game.Move import Move
from src.game.piece.Piece import Piece


class King(Piece):

    def getPieceByCase(self, position):
        for piece in DATA.pieces:
            if piece.position[0] == position[0] and piece.position[1] == position[1]:
                if piece.alive:
                    return piece
        return None

    def getPlayableCases(self):
        playableCases = []
        currentRow = self.position[0]
        currentCol = self.position[1]
        playableCases.append((currentRow + 2, currentCol + 1))
        playableCases.append((currentRow + 2, currentCol - 1))
        playableCases.append((currentRow - 2, currentCol - 1))
        playableCases.append((currentRow - 2, currentCol + 1))
        playableCases.append((currentRow + 1, currentCol + 2))
        playableCases.append((currentRow - 1, currentCol + 2))
        playableCases.append((currentRow + 1, currentCol + 2))
        playableCases.append((currentRow - 1, currentCol + 2))

        return playableCases

    def getAttackableCases(self):
        attackableCases = []
        for case in self.getPlayableCases():
            if self.getPieceByCase(case) is not None:
                attackableCases.append(case)
        return attackableCases

    def tryMoveTo(self, toPosition):
        if self.getPlayableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.position = toPosition
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None

    def tryAttackTo(self, toPosition):
        if self.getAttackableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.getPieceByCase(toPosition).alive = False
            self.position = toPosition
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None
