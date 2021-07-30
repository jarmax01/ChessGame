import pygame

from src import DATA
from src.game.Move import Move
from src.game.piece.Piece import Piece, PieceType


class King(Piece):

    def getPieceByCase(self, position):
        for piece in DATA.pieces:
            if piece.position[0] == position[0] and piece.position[1] == position[1]:
                if piece.alive:
                    return piece
        return None

    def getPlayableCases(self):
        playableCases = []
        theoreticalCases = []
        currentRow = self.position[0]
        currentCol = self.position[1]

        for i in range(-1, 2):
            for j in range(-1, 2):
                piece = self.getPieceByCase((currentRow + i, currentCol + j))
                if piece is None:
                    theoreticalCases.append((currentRow + i, currentCol + j))
                else:
                    if piece.isWhite != self.isWhite:
                        theoreticalCases.append((currentRow + i, currentCol + j))

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
            if self.getPieceByCase(case) is not None and self.getPieceByCase(case).isWhite != self.isWhite:
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

    def isCheck(self):
        currentRow = self.position[0]
        currentCol = self.position[1]

        # Rook and Queen check
        columnAndRow = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # Bishop and Queen check
        diagonals = ((-1, -1), (-1, 1), (1, -1), (1, 1))

        # Pawn check
        if self.isWhite:
            pawnPossibility = ((currentCol-1, currentRow+1), (currentCol-1, currentRow-1))
        else:
            pawnPossibility = ((currentCol+1, currentRow+1), (currentCol+1, currentRow-1))

        # Knight check
        knightCases = [(currentRow + 2, currentCol + 1), (currentRow + 2, currentCol - 1),
                       (currentRow - 2, currentCol - 1), (currentRow - 2, currentCol + 1),
                       (currentRow + 1, currentCol + 2), (currentRow + 1, currentCol - 2),
                       (currentRow - 1, currentCol - 2), (currentRow - 1, currentCol + 2)]

        for direction in diagonals:
            for i in range(1, 8):
                endRow = currentRow + i * direction[0]
                endCol = currentCol + i * direction[1]
                if 1 <= endCol <= 8 and 1 <= endRow <= 8:
                    casePiece = self.getPieceByCase((endRow, endCol))
                    if casePiece is None:
                        continue
                    elif not casePiece.alive:
                        continue
                    elif casePiece.isWhite != self.isWhite:
                        if casePiece.pieceType == PieceType.QUEEN or casePiece.pieceType == PieceType.BISHOP:
                            return True
                    else:
                        break
                else:
                    continue
        for direction in columnAndRow:
            for i in range(1, 8):
                endRow = currentRow + i * direction[0]
                endCol = currentCol + i * direction[1]
                if 1 <= endCol <= 8 and 1 <= endRow <= 8:
                    casePiece = self.getPieceByCase((endRow, endCol))
                    if casePiece is None:
                        continue
                    elif not casePiece.alive:
                        continue
                    elif casePiece.isWhite != self.isWhite:
                        if casePiece.pieceType == PieceType.QUEEN or casePiece.pieceType == PieceType.ROOK:
                            return True
                    else:
                        break
                else:
                    continue
        for case in pawnPossibility:
            piece = self.getPieceByCase(case)
            if piece is not None:
                if piece.pieceType == PieceType.PAWN:
                    if piece.isWhite != self.isWhite:
                        return True
        for case in knightCases:
            piece = self.getPieceByCase(case)
            if piece is not None:
                if piece.pieceType == PieceType.KNIGHT:
                    if piece.isWhite != self.isWhite:
                        return True

        return False
