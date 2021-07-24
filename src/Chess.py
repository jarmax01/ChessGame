import pygame as pygame

from src import DATA


selectedPiece = None

def run():
    global selectedPiece
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
            if event.type == pygame.MOUSEBUTTONUP:
                if selectedPiece is not None:
                    if getPieceByCase(getCase(pygame.mouse.get_pos())) is not None:
                        getPieceByCase(getCase(pygame.mouse.get_pos())).alive = False
                    selectedPiece.position = getCase(pygame.mouse.get_pos())
                    selectedPiece = None
                else :
                    selectedPiece = getPieceByCase(getCase(pygame.mouse.get_pos()))


        pygame.display.flip()

def drawBoard(screen):
    colors = [pygame.Color(239,238,212), pygame.Color(116,149,92)]
    for row in range(DATA.DIMENSION):
        for col in range(DATA.DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*100,row*100,100,100))

def drawPiece(screen):
    for piece in DATA.pieces:
        if piece.alive:
            screen.blit(piece.getImage(), pygame.Rect((piece.position[0]-1) * DATA.SQ_SIZE, (piece.position[1]-1)  * DATA.SQ_SIZE, DATA.SQ_SIZE, DATA.SQ_SIZE))


def getCase(clickPosition):
    return ((clickPosition[0] // 100) + 1), ((clickPosition[1] // 100) + 1)

def getPieceByCase(position):
    for piece in DATA.pieces:
        if piece.position[0] == position[0] and piece.position[1] == position[1]:
            return piece
    return None

run()
