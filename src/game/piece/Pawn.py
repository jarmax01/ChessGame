from src import DATA
from src.game.Move import Move
from src.game.piece.Piece import Piece


class Pawn(Piece):
    hasAlreadyMoved = False

    def getPieceByCase(self, piecePosition):
        for piece in DATA.pieces:
            if piece.position[0] == piecePosition[0] and piece.position[1] == piecePosition[1]:
                return piece
        return None

    def getPlayableCases(self):
        if self.isWhite:
            if self.hasAlreadyMoved:
                theoreticalCases = [(self.position[0], self.position[1] - 1)]
            else:
                theoreticalCases = [(self.position[0], self.position[1] - 1), (self.position[0], self.position[1] - 2)]

            playableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    playableCases.append(case)
            return playableCases
        else:
            if self.hasAlreadyMoved:
                theoreticalCases = [(self.position[0], self.position[1] + 1)]
            else:
                theoreticalCases = [(self.position[0], self.position[1] + 1), (self.position[0], self.position[1] + 2)]

            playableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    playableCases.append(case)
            return playableCases

    def getAttackableCases(self):
        if self.isWhite:
            theoreticalCases = [(self.position[0] - 1, self.position[1] - 1),
                                (self.position[0] + 1, self.position[1] - 1)]

            attackableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    if self.getPieceByCase(case) is not None:
                        if self.getPieceByCase(case).isWhite != self.isWhite:
                            attackableCases.append(case)
            return attackableCases
        else:
            theoreticalCases = [(self.position[0] - 1, self.position[1] + 1),
                                (self.position[0] + 1, self.position[1] + 1)]

            attackableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    if self.getPieceByCase(case) is not None:
                        if self.getPieceByCase(case).isWhite != self.isWhite:
                            attackableCases.append(case)
            return attackableCases

    def tryMoveTo(self, toPosition):
        if self.getPlayableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.position = toPosition
            self.hasAlreadyMoved = True
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None

    def tryAttackTo(self, toPosition):
        if self.getAttackableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.position = toPosition
            self.hasAlreadyMoved = True
            self.getPieceByCase(toPosition).alive = False
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None
