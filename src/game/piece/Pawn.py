from src import DATA
from src.game.Move import Move
from src.game.piece.Piece import Piece
import pygame as pygame


class Pawn(Piece):
    hasAlreadyMoved = False

    def getPieceByCase(self, position):
        for piece in DATA.pieces:
            if piece.position[0] == position[0] and piece.position[1] == position[1]:
                if piece.alive:
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
        else:
            if self.hasAlreadyMoved:
                theoreticalCases = [(self.position[0], self.position[1] + 1)]
            else:
                theoreticalCases = [(self.position[0], self.position[1] + 1), (self.position[0], self.position[1] + 2)]

            playableCases = []
            for case in theoreticalCases:
                if 8 >= case[1] >= 1:
                    playableCases.append(case)

        realPlayableCases = []
        oldPosition = self.position
        for playableCase in playableCases:
            self.position = playableCase
            if not DATA.getKing(self.isWhite).isCheck():
                realPlayableCases.append(playableCase)
            self.position = oldPosition

        return realPlayableCases

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
            pygame.mixer.Sound.play(DATA.moveSound)
            DATA.whiteToPlay = not DATA.whiteToPlay
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None

    def tryAttackTo(self, toPosition):
        if self.getAttackableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.getPieceByCase(toPosition).alive = False
            self.position = toPosition
            self.hasAlreadyMoved = True
            pygame.mixer.Sound.play(DATA.captureSound)
            DATA.whiteToPlay = not DATA.whiteToPlay
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None

