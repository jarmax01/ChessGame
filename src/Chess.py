import pygame as pygame
from pygame import K_RSHIFT, K_LSHIFT

from src import DATA
from src.game.Move import Move


def run():
    pygame.init()
    screen = pygame.display.set_mode((DATA.HEIGHT, DATA.WIDTH), pygame.NOFRAME)
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    DATA.loadImages()

    running = True
    while running:
        clock.tick(15)
        drawBoard(screen)
        drawPiece(screen)
        for event in pygame.event.get():
            keyPressed = pygame.key.get_pressed()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT:
                    DATA.isShifting = False

            if event.type == pygame.KEYDOWN:
                if keyPressed[K_RSHIFT] or keyPressed[K_LSHIFT]:
                    DATA.isShifting = True

            if event.type == pygame.MOUSEBUTTONUP:
                button = event.button
                # Left click
                if button == 1:
                    pass
                # Right click
                elif button == 3:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = event.button
                # Left click
                if button == 1:
                    targetCase = getCase(pygame.mouse.get_pos())
                    targetPiece = getPieceByCase(targetCase)
                    selectedPiece = DATA.selectedPiece

                    if selectedPiece is not None:
                        if targetPiece is not None:
                            if selectedPiece.getAttackableCases().__contains__(targetPiece.position):
                                selectedPiece.tryAttackTo(targetCase)
                            else:
                                if targetPiece == selectedPiece:
                                    DATA.selectedPiece = None
                                else:
                                    DATA.selectedPiece = targetPiece
                        else:
                            selectedPiece.tryMoveTo(targetCase)
                            pass
                    else:
                        if targetPiece is not None:
                            DATA.selectedPiece = targetPiece

                # Right click
                elif button == 3:
                    if DATA.isShifting:
                        DATA.shift_right_clicked_cases.append(getCase(pygame.mouse.get_pos()))
                    else:
                        DATA.right_clicked_cases.append(getCase(pygame.mouse.get_pos()))

        pygame.display.flip()


def drawBoard(screen):
    colors = [pygame.Color(239, 238, 212), pygame.Color(116, 149, 92)]

    for row in range(DATA.DIMENSION):
        for col in range(DATA.DIMENSION):
            isWhite = (((row + col) % 2) == 0)
            caseRow = row + 1
            caseCol = col + 1

            if len(DATA.moves) != 0 and (DATA.moves[0].toLocation == (caseCol, caseRow) or DATA.moves[0].fromLocation == (caseCol, caseRow)):
                if isWhite:
                    color = DATA.WHITE_MOVE_COLOR
                else:
                    color = DATA.GREEN_MOVE_COLOR

            elif DATA.shift_right_clicked_cases.__contains__((caseCol, caseRow)):
                if isWhite:
                    color = DATA.WHITE_GREEN_COLOR
                else:
                    color = DATA.GREEN_GREEN_COLOR

            elif DATA.selectedPiece is not None and DATA.selectedPiece.position == (caseCol, caseRow):
                if isWhite:
                    color = DATA.WHITE_SELECTED_COLOR
                else:
                    color = DATA.GREEN_SELECTED_COLOR
            elif DATA.right_clicked_cases.__contains__((caseCol, caseRow)):
                if isWhite:
                    color = DATA.WHITE_RED_COLOR
                else:
                    color = DATA.GREEN_RED_COLOR

            else:
                color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col * 100, row * 100, 100, 100))

    # Call twice because rectangle override circle
    for row in range(DATA.DIMENSION):
        for col in range(DATA.DIMENSION):
            caseRow = row + 1
            caseCol = col + 1
            if DATA.selectedPiece is not None and DATA.selectedPiece.position == (caseCol, caseRow):
                for piece in DATA.selectedPiece.getPlayableCases():
                    piece_col = piece[0]
                    piece_row = piece[1]
                    center = (((piece_col - 1) * 100 + 50), ((piece_row - 1) * 100 + 50))
                    if isCaseWhite((piece_col, piece_row)):
                        pygame.draw.circle(screen, DATA.WHITE_CIRCLE_COLOR, center, 16)
                    else:
                        pygame.draw.circle(screen, DATA.GREEN_CIRCLE_COLOR, center, 16)
                for piece in DATA.selectedPiece.getAttackableCases():
                    piece_col = piece[0]
                    piece_row = piece[1]
                    center = (((piece_col - 1) * 100 + 50), ((piece_row - 1) * 100 + 50))
                    if isCaseWhite((piece_col, piece_row)):
                        pygame.draw.circle(screen, DATA.WHITE_ATTACKABLE_COLOR, center, 50, 7)
                    else:
                        pygame.draw.circle(screen, DATA.GREEN_ATTACKABLE_COLOR, center, 50, 7)



def drawPiece(screen):
    for piece in DATA.pieces:
        if piece.alive:
            screen.blit(piece.getImage(),
                        pygame.Rect((piece.position[0] - 1) * DATA.SQ_SIZE, (piece.position[1] - 1) * DATA.SQ_SIZE,
                                    DATA.SQ_SIZE, DATA.SQ_SIZE))


def getCase(clickPosition):
    return ((clickPosition[0] // 100) + 1), ((clickPosition[1] // 100) + 1)


def isCaseWhite(position):
    return ((position[0] + position[1]) % 2) == 0


def getPieceByCase(position):
    for piece in DATA.pieces:
        if piece.position[0] == position[0] and piece.position[1] == position[1]:
            if piece.alive:
                return piece
    return None


run()
