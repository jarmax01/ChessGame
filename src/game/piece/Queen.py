from src import DATA
from src.game.piece.Piece import Piece


class Queen(Piece):
    def getPlayableCases(self):
        if self.isWhite:
            theoreticalCases = []
            for i in range(1, 8):
                theoreticalCases.append((self.position[0] + i, self.position[1]))
                theoreticalCases.append((self.position[0] - i, self.position[1]))
                theoreticalCases.append((self.position[0], self.position[1] + i))
                theoreticalCases.append((self.position[0], self.position[1] - i))
                theoreticalCases.append((self.position[0] + i, self.position[1] + i))
                theoreticalCases.append((self.position[0] - i, self.position[1] - i))
                theoreticalCases.append((self.position[0] - i, self.position[1] + i))
                theoreticalCases.append((self.position[0] + i, self.position[1] - i))
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
                    attackableCases.append(case)
            return attackableCases
        else:
            theoreticalCases = [(self.position[0] - 1, self.position[1] + 1),
                                (self.position[0] + 1, self.position[1] + 1)]

            attackableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    attackableCases.append(case)
            return attackableCases

    def tryMoveTo(self, position):
        if self.getPlayableCases().__contains__(position):
            self.position = position
            self.hasAlreadyMoved = True
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None
