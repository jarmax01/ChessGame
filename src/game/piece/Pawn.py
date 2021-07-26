from src.game.piece.Piece import Piece


class Pawn(Piece):
    def getPlayableCases(self):
        if self.isWhite:
            theoreticalCases = [(self.position[0],self.position[1]-1), (self.position[0],self.position[1]-2)]

            playableCases = []
            for case in theoreticalCases:
                if case[0] < 8:
                    playableCases.append(case)
            return playableCases


