from src import DATA
from src.game.piece.Piece import Piece


class Pawn(Piece):
    hasAlreadyMoved = False

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
            theoreticalCases = [(self.position[0]-1, self.position[1] - 1), (self.position[0]+1, self.position[1] - 1)]

            attackableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    attackableCases.append(case)
            return attackableCases
        else:
            theoreticalCases = [(self.position[0] - 1, self.position[1] + 1),(self.position[0] + 1, self.position[1] + 1)]

            attackableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    attackableCases.append(case)
            return attackableCases



    def moveTo(self, position):
        self.position = position
        self.hasAlreadyMoved = True
        if DATA.selectedPiece == self:
            DATA.selectedPiece = None
