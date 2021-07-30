import pygame

from src import DATA
from src.game.Move import Move
from src.game.piece.Piece import Piece


class Bishop(Piece):

    def getPieceByCase(self, position):
        for piece in DATA.pieces:
            if piece.position[0] == position[0] and piece.position[1] == position[1]:
                if piece.alive:
                    return piece
        return None

    def getPlayableCases(self):
        theoreticalCases = []
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
                        theoreticalCases.append((endRow, endCol))
                    elif not casePiece.alive:
                        theoreticalCases.append((endRow, endCol))
                    elif casePiece.isWhite != self.isWhite:
                        theoreticalCases.append((endRow, endCol))
                        break
                    else:
                        break
                else:
                    break

        oldPosition = self.position
        for playableCase in theoreticalCases:
            self.position = playableCase
            if not DATA.getKing(self.isWhite).isCheck():
               playableCases.append(playableCase)
            self.position = oldPosition



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
            pygame.mixer.Sound.play(DATA.moveSound)
            DATA.whiteToPlay = not DATA.whiteToPlay
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None

    def tryAttackTo(self, toPosition):
        if self.getAttackableCases().__contains__(toPosition):
            DATA.moves.insert(0, (Move(self.position, toPosition, self)))
            self.getPieceByCase(toPosition).alive = False
            self.position = toPosition
            pygame.mixer.Sound.play(DATA.captureSound)
            DATA.whiteToPlay = not DATA.whiteToPlay
            if DATA.selectedPiece == self:
                DATA.selectedPiece = None
