import pygame
import sys
import os
import random
WIN = 800
ROWS = 50

CAPTION = '2048'
SCREEN = pygame.display.set_mode((WIN, WIN))

YELLOW = (250, 248, 239)
BROWN = (187, 173, 161)
DBROWN = (119, 110, 102)
LBROWN = (214, 205, 196)
ARROWDARK = (119, 84, 71)
ARROWLIGHT = (219, 184, 171)
STARTDARK = (245, 131, 96)
STARTLIGHT = (255, 181, 146)
HSCOREDARK = (142, 122, 103)
HSCORELIGHT = (192, 172, 153)
WHITE = (255, 255, 255)

NUMBERS = {'2': (238, 228, 219), '4': (237, 224, 201), '8': (214, 176, 125), '16': (243, 149, 104), '32': (244, 124, 99), '64': (244, 95, 67), '128': (244, 70, 45), '256': (244, 50, 25), '512': (244, 30, 5), '1024': (205, 0, 205), '2048': (179, 0, 179), '4096': (154, 0, 154), '8192': (128, 0, 128), '16384': (103, 0, 103), '32768': (77, 0, 77), '65536': (0, 102, 205), '131072': (0, 90, 179), '262144': (0, 77, 154), '524288': (0, 64, 128), '1048576': (0, 51, 103)}

tiles = [pygame.image.load(os.path.join('Images', 'Tiny.png')), pygame.image.load(os.path.join('Images', 'Classic.png')), pygame.image.load(os.path.join('Images', 'Big.png')), pygame.image.load(os.path.join('Images', 'Bigger.png')), pygame.image.load(os.path.join('Images', 'Huge.png'))]

options = [2, 4]
probability = [0.9, 0.1]

""" 
TODO: 
score keeping
highscore
undo 
restart
"""

class Game(object):
    def __init__(self):
        self.done = False
        self.grid = []
        self.tempColumn = 0
        self.tempRow = 0
        self.numGrid = []
        self.choice = 2
        self.randx = 0
        self.randy = 0
        self.tile = [3, 4, 5, 6, 8]
        self.move = False
        self.coord = []

    def makeGrid(self):
        border = 15
        row = 130 + border
        self.tempColumn = 720 - ((self.tile[self.choice] + 1) * border)
        self.tempColumn = round(self.tempColumn / self.tile[self.choice])
        self.tempRow = 630 - ((self.tile[self.choice] + 1) * border)
        self.tempRow = round(self.tempRow / self.tile[self.choice])
        for i in range(self.tile[self.choice]):
            column = 40 + border
            self.numGrid.append([])
            self.grid.append([])
            for j in range(self.tile[self.choice]):
                self.numGrid[i].append(0)
                self.grid[i].append((row, column))
                column = column + self.tempColumn + border
            row = row + self.tempRow + border

    def drawGrid(self):
        for i in range(self.tile[self.choice]):
            for j in range(self.tile[self.choice]):
                # self.roundedRect(LBROWN, self.grid[i][j][1]+20, self.grid[i][j][0]+20, 213, 170, 10)
                pygame.draw.rect(SCREEN, LBROWN, (self.grid[i][j][1], self.grid[i][j][0], self.tempColumn, self.tempRow))
                # pygame.display.update()

    def drawNum(self):
        for i in range(self.tile[self.choice]):
            for j in range(self.tile[self.choice]):
                if self.numGrid[i][j] != 0:
                    pygame.draw.rect(SCREEN, NUMBERS[str(self.numGrid[i][j])], (self.grid[i][j][1], self.grid[i][j][0], self.tempColumn, self.tempRow))
                    if self.numGrid[i][j] == 2 or self.numGrid[i][j] == 4:
                        fontSize = int(0.7 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, DBROWN)
                    elif 7 < self.numGrid[i][j] < 515:
                        fontSize = int(0.5 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, WHITE)
                    elif 1000 < self.numGrid[i][j] < 9000:
                        fontSize = int(0.4 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, WHITE)
                    elif 10000 < self.numGrid[i][j] < 65540:
                        fontSize = int(0.325 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, WHITE)
                    elif 100000 < self.numGrid[i][j] < 524290:
                        fontSize = int(0.27 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, WHITE)
                    else:
                        fontSize = int(0.235 * self.tempColumn)
                        numFont = pygame.font.SysFont('comicsansms', fontSize, 1, 0)
                        numLabel = numFont.render(str(self.numGrid[i][j]), 1, WHITE)

                    SCREEN.blit(numLabel, ((self.grid[i][j][1] + (self.tempColumn // 2)) - numLabel.get_width() // 2, (self.grid[i][j][0] + self.tempRow // 2) - numLabel.get_height() // 2))
        pygame.display.update()

    def moveDown(self):
        for i in range(self.tile[self.choice] - 2, -1, -1):
            for j in range(self.tile[self.choice] - 1, -1, -1):
                k = i
                if self.numGrid[i][j] != 0:
                    for l in range(k, self.tile[self.choice] - 1):
                        if self.numGrid[l + 1][j] == 0 and self.numGrid[l][j] != 0:
                            self.numGrid[l + 1][j] = self.numGrid[l][j]
                            self.numGrid[l][j] = 0
                            self.move = True
                        else:
                            break

        for i in range(self.tile[self.choice] - 1, 0, -1):
            for j in range(self.tile[self.choice] - 1, -1, -1):
                if self.numGrid[i][j] == self.numGrid[i - 1][j] and self.numGrid[i][j] != 0:
                    self.numGrid[i][j] *= 2
                    self.numGrid[i - 1][j] = 0
                    self.move = True

        for i in range(self.tile[self.choice] - 2, -1, -1):
            for j in range(self.tile[self.choice] - 1, -1, -1):
                k = i
                if self.numGrid[i][j] != 0:
                    for l in range(k, self.tile[self.choice] - 1):
                        if self.numGrid[l + 1][j] == 0 and self.numGrid[l][j] != 0:
                            self.numGrid[l + 1][j] = self.numGrid[l][j]
                            self.numGrid[l][j] = 0
                        else:
                            break

    def moveUp(self):
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]
        self.moveDown()
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]

    def moveRight(self):
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]
        self.moveDown()
        self.numGrid = [list(r) for r in zip(*self.numGrid)][::-1]

    def moveLeft(self):
        self.numGrid = [list(r) for r in zip(*self.numGrid)][::-1]
        self.moveDown()
        self.numGrid = [list(r) for r in zip(*self.numGrid[::-1])]

    def randomTile(self):
        self.coord.append((self.randx, self.randy))
        self.randx = random.randrange(self.tile[self.choice])
        self.randy = random.randrange(self.tile[self.choice])
        if self.numGrid[self.randx][self.randy] < 1 and ((self.randx, self.randy) not in self.coord):
            self.numGrid[self.randx][self.randy] = random.choices(options, weights=(0.9, 0.1), k=1)[0]
        else:
            self.randomTile()

    def gameScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 70, 1, 0)
        scoreFont = pygame.font.SysFont('comicsansms', 18, 1, 0)
        numFont = pygame.font.SysFont('comicsansms', 50, 1, 0)
        self.randomTile()
        self.coord = []
        running = True
        while running:
            # displays 2048 in top left corner
            SCREEN.fill(YELLOW)
            titleLabel = titleFont.render('2048', 1, DBROWN)
            SCREEN.blit(titleLabel, (40, 0))

            # displays score
            pygame.draw.rect(SCREEN, BROWN, (int(WIN / 2) + 15, 20, 158, 60))
            scoreLabel = scoreFont.render('SCORE', 1, WHITE)
            SCREEN.blit(scoreLabel, (int(WIN / 2) + 93 - scoreLabel.get_width() // 2, 20))
            # scoreOnly = scoreFont.render('123456783', 1, WHITE)
            # SCREEN.blit(scoreOnly, (int(WIN / 2) + 93 - scoreOnly.get_width() / 2, 50))

            # displays High Score
            pygame.draw.rect(SCREEN, BROWN, (WIN - 40 - 15 - 156, 20, 158, 60))
            hscoreLabel = scoreFont.render('HIGH SCORE', 1, WHITE)
            SCREEN.blit(hscoreLabel, (WIN - 133 - hscoreLabel.get_width() // 2, 20))

            pygame.draw.rect(SCREEN, BROWN, (40, 90, 128, 30))
            homeLabel = scoreFont.render('HOME', 1, WHITE)
            SCREEN.blit(homeLabel, (104 - homeLabel.get_width() // 2, 92))

            pygame.draw.rect(SCREEN, BROWN, (430, 90, 128, 30))
            undoLabel = scoreFont.render('UNDO', 1, WHITE)
            SCREEN.blit(undoLabel, (494 - undoLabel.get_width() // 2, 92))

            pygame.draw.rect(SCREEN, BROWN, (603, 90, 128, 30))
            restartLabel = scoreFont.render('RESTART', 1, WHITE)
            SCREEN.blit(restartLabel, (667 - restartLabel.get_width() // 2, 92))

            pygame.draw.rect(SCREEN, DBROWN, (40, 130, WIN - 80, WIN - 170))
            self.drawGrid()
            mouse = pygame.mouse.get_pos()
            if 40 <= mouse[0] <= 168 and 90 <= mouse[1] <= 120:
                pygame.draw.rect(SCREEN, LBROWN, (40, 90, 128, 30))
                homeLabel = scoreFont.render('HOME', 1, WHITE)
                SCREEN.blit(homeLabel, (104 - homeLabel.get_width() // 2, 92))
            elif 430 <= mouse[0] <= 558 and 90 <= mouse[1] <= 120:
                pygame.draw.rect(SCREEN, LBROWN, (430, 90, 128, 30))
                undoLabel = scoreFont.render('UNDO', 1, WHITE)
                SCREEN.blit(undoLabel, (494 - undoLabel.get_width() // 2, 92))
            elif 603 <= mouse[0] <= 731 and 90 <= mouse[1] <= 120:
                pygame.draw.rect(SCREEN, LBROWN, (603, 90, 128, 30))
                restartLabel = scoreFont.render('RESTART', 1, WHITE)
                SCREEN.blit(restartLabel, (667 - restartLabel.get_width() // 2, 92))
            
            self.drawNum()

            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 40 <= mouse[0] <= 168 and 90 <= mouse[1] <= 120:
                        running = False
                    elif 430 <= mouse[0] <= 558 and 90 <= mouse[1] <= 120:
                        self.undo()
                    elif 603 <= mouse[0] <= 731 and 90 <= mouse[1] <= 120:
                        self.restart()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.moveUp()
                        if self.move:
                            self.randomTile()
                            self.move = False
                            self.coord = []
                        # print(self.numGrid[0])
                        # print(self.numGrid[1])
                        # print(self.numGrid[2])
                        # print(self.numGrid[3])
                        # print('')
                        self.drawNum()
                    elif event.key == pygame.K_DOWN:
                        self.moveDown()
                        if self.move:
                            self.randomTile()
                            self.move = False
                            self.coord = []
                        # print(self.numGrid[0])
                        # print(self.numGrid[1])
                        # print(self.numGrid[2])
                        # print(self.numGrid[3])
                        # print('')

                        self.drawNum()
                    elif event.key == pygame.K_LEFT:
                        self.moveLeft()
                        if self.move:
                            self.randomTile()
                            self.move = False
                            self.coord = []
                        # print(self.numGrid[0])
                        # print(self.numGrid[1])
                        # print(self.numGrid[2])
                        # print(self.numGrid[3])
                        # print('')

                        self.drawNum()
                    elif event.key == pygame.K_RIGHT:
                        self.moveRight()
                        if self.move:
                            self.randomTile()
                            self.move = False
                            self.coord = []
                        # print(self.numGrid[0])
                        # print(self.numGrid[1])
                        # print(self.numGrid[2])
                        # print(self.numGrid[3])
                        # print('')

                        self.drawNum()

    """
    This function displays all the images and text on the home screen
    """
    def homeScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 40, 0, 0)
        description = [titleFont.render('Tiny (3x3)', 1, BROWN), titleFont.render('Classic (4x4)', 1, BROWN), titleFont.render('Big (5x5)', 1, BROWN), titleFont.render('Bigger (6x6)', 1, BROWN), titleFont.render('Huge (8x8)', 1, BROWN)]
        running = True
        while running:

            SCREEN.fill(YELLOW)
            SCREEN.blit(tiles[self.choice], (int(WIN / 2 - tiles[self.choice].get_width() / 2), int(WIN / 16)))
            pygame.draw.polygon(SCREEN, ARROWDARK, ((int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40), int(WIN / 1.5)), (int(WIN / 2 - tiles[self.choice].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40), int(WIN / 1.5) + 60)))
            pygame.draw.polygon(SCREEN, ARROWDARK, ((int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40), int(WIN / 1.5)), (int(WIN / 2 + tiles[self.choice].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40), int(WIN / 1.5) + 60)))
            pygame.draw.rect(SCREEN, STARTDARK, (int(WIN / 2 - 150), int(WIN / 1.25), 300, 60))
            pygame.draw.rect(SCREEN, HSCOREDARK, (int(WIN / 2 - 150), int(WIN / 1.12), 300, 60))
            # titleLabel = titleFont.render('Tiny (3x3)', 1, BROWN)
            titleLabel = description[self.choice]
            startLabel = titleFont.render('Start Game', 1, WHITE)
            hscoreLabel = titleFont.render('High Scores', 1, WHITE)
            SCREEN.blit(titleLabel, (int(WIN / 2 - titleLabel.get_width() / 2), int(WIN / 1.5)))
            SCREEN.blit(startLabel, (int(WIN / 2 - startLabel.get_width() / 2), int(WIN / 1.25)))
            SCREEN.blit(hscoreLabel, (int(WIN / 2 - hscoreLabel.get_width() / 2), int(WIN / 1.12)))

            mouse = pygame.mouse.get_pos()
            if int(WIN / 2 - tiles[self.choice].get_width() / 2) <= mouse[0] <= int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                pygame.draw.polygon(SCREEN, ARROWLIGHT, ((int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40), int(WIN / 1.5)), (int(WIN / 2 - tiles[self.choice].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40), int(WIN / 1.5) + 60)))
            elif int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40) <= mouse[0] <= int(WIN / 2 + tiles[self.choice].get_width() / 2) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                pygame.draw.polygon(SCREEN, ARROWLIGHT, ((int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40), int(WIN / 1.5)), (int(WIN / 2 + tiles[self.choice].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40), int(WIN / 1.5) + 60)))
            elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.25) <= mouse[1] <= int(WIN / 1.25) + 60:
                pygame.draw.rect(SCREEN, STARTLIGHT, (int(WIN / 2 - 150), int(WIN / 1.25), 300, 60))
                SCREEN.blit(startLabel, (int(WIN / 2 - startLabel.get_width() / 2), int(WIN / 1.25)))
            elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.12) <= mouse[1] <= int(WIN / 1.12) + 60:
                pygame.draw.rect(SCREEN, HSCORELIGHT, (int(WIN / 2 - 150), int(WIN / 1.12), 300, 60))
                SCREEN.blit(hscoreLabel, (int(WIN / 2 - hscoreLabel.get_width() / 2), int(WIN / 1.12)))
            

            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
                # pygame.quit()
                # sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if int(WIN / 2 - tiles[self.choice].get_width() / 2) <= mouse[0] <= int(WIN / 2 - tiles[self.choice].get_width() / 2 + 40) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                        self.choice -= 1
                        if self.choice == -5:
                            self.choice = 0
                    elif int(WIN / 2 + tiles[self.choice].get_width() / 2 - 40) <= mouse[0] <= int(WIN / 2 + tiles[self.choice].get_width() / 2) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                        self.choice += 1
                        if self.choice == 5:
                            self.choice = 0
                    elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.25) <= mouse[1] <= int(WIN / 1.25) + 60:
                        self.makeGrid(self.choice)
                        self.gameScreen(self.choice)
                        self.grid = []
                        
                    elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.12) <= mouse[1] <= int(WIN / 1.12) + 60:
                        self.hscoreScreen

    def mainLoop(self):
        # self.homeScreen()
        self.makeGrid()
        # self.numGrid = [[2,4,8,16,32,64],
        #                 [128,256,512,1024,2048,4096],
        #                 [8192,16384,32768,65536,131072,262144],
        #                 [524288,1048576,0,0,0,0],
        #                 [0,0,0,0,0,0],
        #                 [0,0,0,0,0,0]]
        # self.numGrid = [[2,4,8,16,32],
        #                 [64,128,256,512,1024],
        #                 [2048,4096,8192,16384,32768],
        #                 [65536,131072,262144,524288,1048576],
        #                 [0,0,0,0,0]]
        self.gameScreen()
        # while not self.done:
        #     self.callEvent()

def main():
    pygame.init()
    pygame.display.set_caption(CAPTION)
    call = Game()
    call.mainLoop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
