def carregar_osciladors(gameState):
    # Oscil·lador1
    baseO1x, baseO1y = 4, 3

    gameState[baseO1x, baseO1y] = 1
    gameState[baseO1x + 1, baseO1y] = 1
    gameState[baseO1x, baseO1y + 1] = 1
    gameState[baseO1x + 1, baseO1y + 1] = 1
    gameState[baseO1x + 3, baseO1y + 1] = 1
    gameState[baseO1x + 4, baseO1y + 2] = 1
    gameState[baseO1x + 1, baseO1y + 3] = 1
    gameState[baseO1x + 2, baseO1y + 4] = 1
    gameState[baseO1x + 4, baseO1y + 4] = 1
    gameState[baseO1x + 4, baseO1y + 5] = 1
    gameState[baseO1x + 5, baseO1y + 4] = 1
    gameState[baseO1x + 5, baseO1y + 5] = 1

    # Oscil·lador2
    baseO2x, baseO2y = 15, 1

    gameState[baseO2x, baseO2y] = 1
    gameState[baseO2x + 1, baseO2y] = 1
    gameState[baseO2x + 1, baseO2y + 1] = 1
    gameState[baseO2x + 1, baseO2y + 2] = 1
    gameState[baseO2x + 2, baseO2y + 3] = 1
    gameState[baseO2x + 3, baseO2y + 3] = 1
    gameState[baseO2x + 3, baseO2y + 2] = 1

    gameState[baseO2x + 5, baseO2y + 5] = 1
    gameState[baseO2x + 6, baseO2y + 5] = 1
    gameState[baseO2x + 7, baseO2y + 5] = 1
    gameState[baseO2x + 8, baseO2y + 5] = 1
    gameState[baseO2x + 9, baseO2y + 5] = 1

    gameState[baseO2x + 11, baseO2y + 2] = 1
    gameState[baseO2x + 11, baseO2y + 3] = 1
    gameState[baseO2x + 12, baseO2y + 3] = 1
    gameState[baseO2x + 13, baseO2y + 2] = 1
    gameState[baseO2x + 13, baseO2y + 1] = 1
    gameState[baseO2x + 13, baseO2y] = 1
    gameState[baseO2x + 14, baseO2y] = 1

    gameState[baseO2x + 3, baseO2y + 7] = 1
    gameState[baseO2x + 2, baseO2y + 7] = 1
    gameState[baseO2x + 3, baseO2y + 8] = 1
    gameState[baseO2x + 1, baseO2y + 8] = 1
    gameState[baseO2x + 1, baseO2y + 9] = 1
    gameState[baseO2x + 1, baseO2y + 10] = 1
    gameState[baseO2x, baseO2y + 10] = 1

    gameState[baseO2x + 11, baseO2y + 7] = 1
    gameState[baseO2x + 11, baseO2y + 8] = 1
    gameState[baseO2x + 12, baseO2y + 7] = 1
    gameState[baseO2x + 13, baseO2y + 8] = 1
    gameState[baseO2x + 13, baseO2y + 9] = 1
    gameState[baseO2x + 13, baseO2y + 10] = 1
    gameState[baseO2x + 14, baseO2y + 10] = 1

    # Oscil·lador3
    baseO3x, baseO3y = 35, 1

    gameState[baseO3x, baseO3y] = 1
    gameState[baseO3x, baseO3y + 1] = 1
    gameState[baseO3x, baseO3y + 2] = 1
    gameState[baseO3x + 1, baseO3y + 1] = 1
    gameState[baseO3x + 1, baseO3y + 2] = 1
    gameState[baseO3x + 1, baseO3y + 3] = 1

    # Oscil·lador4
    baseO4x, baseO4y = 40, 1

    gameState[baseO4x, baseO4y] = 1
    gameState[baseO4x + 1, baseO4y] = 1
    gameState[baseO4x, baseO4y + 1] = 1
    gameState[baseO4x + 1, baseO4y + 1] = 1

    gameState[baseO4x + 2, baseO4y + 2] = 1
    gameState[baseO4x + 3, baseO4y + 2] = 1
    gameState[baseO4x + 2, baseO4y + 3] = 1
    gameState[baseO4x + 3, baseO4y + 3] = 1

    # Oscil·lador5
    baseO5x, baseO5y = 34, 10

    gameState[baseO5x, baseO5y] = 1
    gameState[baseO5x + 1, baseO5y - 1] = 1
    gameState[baseO5x + 1, baseO5y - 2] = 1
    gameState[baseO5x + 2, baseO5y] = 1
    gameState[baseO5x + 2, baseO5y + 1] = 1
    gameState[baseO5x + 3, baseO5y - 1] = 1

def carregar_naus(gameState):
    # Nau1
    baseN1x, baseN1y = 3, 17

    gameState[baseN1x, baseN1y] = 1
    gameState[baseN1x + 2, baseN1y + 1] = 1
    gameState[baseN1x + 3, baseN1y + 2] = 1
    gameState[baseN1x + 3, baseN1y + 3] = 1
    gameState[baseN1x - 1, baseN1y + 4] = 1
    gameState[baseN1x - 2, baseN1y + 1] = 1
    gameState[baseN1x - 2, baseN1y + 3] = 1
    gameState[baseN1x, baseN1y + 4] = 1
    gameState[baseN1x + 1, baseN1y + 4] = 1
    gameState[baseN1x + 2, baseN1y + 4] = 1
    gameState[baseN1x + 3, baseN1y + 4] = 1

    #Gosper Gun
    baseGGx, baseGGy = 1, 35

    gameState[baseGGx, baseGGy] = 1
    gameState[baseGGx + 1, baseGGy + 1] = 1
    gameState[baseGGx + 1, baseGGy] = 1
    gameState[baseGGx, baseGGy + 1] = 1

    gameState[baseGGx + 10, baseGGy] = 1
    gameState[baseGGx + 10, baseGGy + 1] = 1
    gameState[baseGGx + 10, baseGGy + 2] = 1
    gameState[baseGGx + 11, baseGGy + 3] = 1
    gameState[baseGGx + 12, baseGGy + 4] = 1
    gameState[baseGGx + 13, baseGGy + 4] = 1
    gameState[baseGGx + 11, baseGGy - 1] = 1
    gameState[baseGGx + 12, baseGGy - 2] = 1
    gameState[baseGGx + 13, baseGGy - 2] = 1

    gameState[baseGGx + 14, baseGGy + 1] = 1
    gameState[baseGGx + 15, baseGGy - 1] = 1
    gameState[baseGGx + 16, baseGGy] = 1
    gameState[baseGGx + 16, baseGGy + 1] = 1
    gameState[baseGGx + 16, baseGGy + 2] = 1
    gameState[baseGGx + 15, baseGGy + 3] = 1
    gameState[baseGGx + 17, baseGGy + 1] = 1

    gameState[baseGGx + 20, baseGGy] = 1
    gameState[baseGGx + 20, baseGGy - 1] = 1
    gameState[baseGGx + 20, baseGGy - 2] = 1
    gameState[baseGGx + 21, baseGGy] = 1
    gameState[baseGGx + 21, baseGGy - 1] = 1
    gameState[baseGGx + 21, baseGGy - 2] = 1
    gameState[baseGGx + 22, baseGGy + 1] = 1
    gameState[baseGGx + 22, baseGGy - 3] = 1
    gameState[baseGGx + 24, baseGGy - 3] = 1
    gameState[baseGGx + 24, baseGGy - 4] = 1
    gameState[baseGGx + 24, baseGGy + 1] = 1
    gameState[baseGGx + 24, baseGGy + 2] = 1

    gameState[baseGGx + 34, baseGGy -1] = 1
    gameState[baseGGx + 34, baseGGy -2] = 1
    gameState[baseGGx + 35, baseGGy -1] = 1
    gameState[baseGGx + 35, baseGGy -2] = 1



