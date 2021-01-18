import pygame
import numpy
import time

import patrons

pygame.init()

# Alçada i amplada de la pantalla
width, height = 1000, 1000

# Creem la pantalla
screen = pygame.display.set_mode((height, width))

# Color del fons (gairebé negre)
bg = 25, 25, 25

# Pintem el fons
screen.fill(bg)

# Fixem el número de files i columnes
nxC, nyC = 50, 50

# Calculem les seves dimensions
dimCW = width / nxC
dimCH = height / nyC

# Estat de la matriu
gameState = numpy.zeros((nxC, nyC))

# Autòmats
patrons.carregar_naus(gameState)
#patrons.carregar_osciladors(gameState)





# Control de l'execució del joc
pauseExect = True

# Bucle d'execució
while True:

    newGameState = numpy.copy(gameState)
    screen.fill(bg)
    time.sleep(0.1)

    # Registrem esdeveniments del teclat o del ratolí
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        #Detectem si es pitja el ratolí
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(numpy.floor(posX / dimCW)), int(numpy.floor(posY / dimCH))
            newGameState[celX, celY] = not mouseClick[2]

    # Recorrem la matriu
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

                # Calculem les cel·les veïnes vives
                n_neigh = gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                          gameState[(x)     % nxC, (y - 1)  % nyC] + \
                          gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                          gameState[(x - 1) % nxC, (y)      % nyC] + \
                          gameState[(x + 1) % nxC, (y)      % nyC] + \
                          gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                          gameState[(x)     % nxC, (y + 1)  % nyC] + \
                          gameState[(x + 1) % nxC, (y + 1)  % nyC]

                #Regla #1 : una cèl·la morta amb exactament tres veïnes vives, reviu
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2 : una cel·la viva rodejada per menys de dos vives o per més de 3 acaba morint per soledat o superpoblació
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y] = 0

            # Creem el polígon a dibuixar de cada cel·la
            poligon = [(x * dimCW, y * dimCH),
                       ((x+1) * dimCW, y * dimCH),
                       ((x+1) * dimCW, (y+1) * dimCH),
                       (x * dimCW, (y+1) * dimCH)]


            # Dibuixem la cel·la per a cada parell x, y
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poligon, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poligon, 0)

    # Actualitzem el gameState
    gameState = numpy.copy(newGameState)

    # Actualitzem la pantalla
    pygame.display.flip()


