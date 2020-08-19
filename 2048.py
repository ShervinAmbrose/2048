import pygame
import sys
import os

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


tiles = [pygame.image.load(os.path.join('Images', 'Tiny.png')), pygame.image.load(os.path.join('Images', 'Classic.png')), pygame.image.load(os.path.join('Images', 'Big.png')), pygame.image.load(os.path.join('Images', 'Bigger.png')), pygame.image.load(os.path.join('Images', 'Huge.png'))]



class Game(object):
    def __init__(self):
        self.done = False
        self.grid = []
    def roundedRect(self, colour, coordX, coordY, width, height, radius):
        pygame.draw.rect(SCREEN, colour, (coordX, coordY, width, height))
        pygame.draw.rect(SCREEN, colour, (coordX + radius, coordY - radius, width - (2 * radius), height + (2 * radius)))
        pygame.draw.circle(SCREEN, colour, (coordX + radius, coordY), radius)
        pygame.draw.circle(SCREEN, colour, (coordX + width - radius, coordY), radius)
        pygame.draw.circle(SCREEN, colour, (coordX + radius, coordY + height), radius)
        pygame.draw.circle(SCREEN, colour, (coordX + width - radius, coordY + height), radius)

    # def makeGrid(self):
    #     row = 120
    #     for i in range(3):
    #         column = 60
    #         self.grid.append([])
    #         for j in range(3):
    #             self.grid[i].append((row, column))
    #             column += 220
    #         row += 190
    #     # self.drawGrid()

    def makeGrid(self):
        row = 150
        for i in range(3):
            column = 60
            self.grid.append([])
            for j in range(3):
                self.grid[i].append((row, column))
                column += 233
            row += 203

    def drawGrid(self):
        for i in range(3):
            for j in range(3):
                # self.roundedRect(LBROWN, self.grid[i][j][1]+20, self.grid[i][j][0]+20, 213, 170, 10)
                pygame.draw.rect(SCREEN, LBROWN, (self.grid[i][j][1], self.grid[i][j][0], 213, 183))
                # pygame.display.update()

    def gameScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 60, 1, 0)
        running = True
        while running:
            SCREEN.fill(YELLOW)
            # pygame.display.update()
            titleLabel = titleFont.render('2048', 1, DBROWN)
            SCREEN.blit(titleLabel, (40, 0))
            # pygame.display.update()
            # self.roundedRect(DBROWN, 40, 130, WIN - 80, WIN - 170, 10)
            # pygame.draw.line(SCREEN, DBROWN, (40,120), (760,120))
            # pygame.draw.line(SCREEN, DBROWN, (760,120), (760,770))
            pygame.draw.rect(SCREEN, DBROWN, (40, 130, WIN - 80, WIN - 170))

            # pygame.draw.rect(SCREEN, LBROWN, (40, 130, WIN - 80, WIN - 170))
            # pygame.draw.rect(SCREEN, LBROWN, (40, 130, WIN - 80, WIN - 170))
            # pygame.draw.rect(SCREEN, LBROWN, (40, 130, WIN - 80, WIN - 170))

            # pygame.display.update()
            self.drawGrid()
            # self.roundedRect(LBROWN, 60, 150, 223, 226, 10)
            # self.roundedRect(LBROWN, 293, 150, 223, 226, 10)
            # self.roundedRect(LBROWN, 526, 150, 223, 226, 10)

            pygame.display.update()
            # self.roundedRect(LBROWN, 50, 380, 230, 190, 10)
            # self.roundedRect(LBROWN, 290, 380, 230, 190, 10)
            # self.roundedRect(LBROWN, 530, 380, 220, 190, 10)

            # self.roundedRect(LBROWN, 50, 600, 230, 150, 10)
            # self.roundedRect(LBROWN, 290, 600, 230, 150, 10)
            # self.roundedRect(LBROWN, 530, 600, 220, 150, 10)


            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_s]:
                self.gameScreen()

    """
    This function displays all the images and text on the home screen
    """
    def homeScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 40, 0, 0)
        description = [titleFont.render('Tiny (3x3)', 1, BROWN), titleFont.render('Classic (4x4)', 1, BROWN), titleFont.render('Big (5x5)', 1, BROWN), titleFont.render('Bigger (6x6)', 1, BROWN), titleFont.render('Huge (8x8)', 1, BROWN)]
        running = True
        i = 0
        while running:
            SCREEN.fill(YELLOW)
            SCREEN.blit(tiles[i], (int(WIN / 2 - tiles[i].get_width() / 2), int(WIN / 16)))
            pygame.draw.polygon(SCREEN, ARROWDARK, ((int(WIN / 2 - tiles[i].get_width() / 2 + 40), int(WIN / 1.5)), (int(WIN / 2 - tiles[i].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 - tiles[i].get_width() / 2 + 40), int(WIN / 1.5) + 60)))
            pygame.draw.polygon(SCREEN, ARROWDARK, ((int(WIN / 2 + tiles[i].get_width() / 2 - 40), int(WIN / 1.5)), (int(WIN / 2 + tiles[i].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 + tiles[i].get_width() / 2 - 40), int(WIN / 1.5) + 60)))
            pygame.draw.rect(SCREEN, STARTDARK, (int(WIN / 2 - 150), int(WIN / 1.25), 300, 60))
            pygame.draw.rect(SCREEN, HSCOREDARK, (int(WIN / 2 - 150), int(WIN / 1.12), 300, 60))
            # titleLabel = titleFont.render('Tiny (3x3)', 1, BROWN)
            titleLabel = description[i]
            startLabel = titleFont.render('Start Game', 1, WHITE)
            hscoreLabel = titleFont.render('High Scores', 1, WHITE)
            SCREEN.blit(titleLabel, (int(WIN / 2 - titleLabel.get_width() / 2), int(WIN / 1.5)))
            SCREEN.blit(startLabel, (int(WIN / 2 - startLabel.get_width() / 2), int(WIN / 1.25)))
            SCREEN.blit(hscoreLabel, (int(WIN / 2 - hscoreLabel.get_width() / 2), int(WIN / 1.12)))
            
            mouse = pygame.mouse.get_pos()
            if int(WIN / 2 - tiles[i].get_width() / 2) <= mouse[0] <= int(WIN / 2 - tiles[i].get_width() / 2 + 40) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                pygame.draw.polygon(SCREEN, ARROWLIGHT, ((int(WIN / 2 - tiles[i].get_width() / 2 + 40), int(WIN / 1.5)), (int(WIN / 2 - tiles[i].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 - tiles[i].get_width() / 2 + 40), int(WIN / 1.5) + 60)))
            elif int(WIN / 2 + tiles[i].get_width() / 2 - 40) <= mouse[0] <= int(WIN / 2 + tiles[i].get_width() / 2) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                pygame.draw.polygon(SCREEN, ARROWLIGHT, ((int(WIN / 2 + tiles[i].get_width() / 2 - 40), int(WIN / 1.5)), (int(WIN / 2 + tiles[i].get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 + tiles[i].get_width() / 2 - 40), int(WIN / 1.5) + 60)))
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
            if keys[pygame.K_s]:
                self.gameScreen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if int(WIN / 2 - tiles[i].get_width() / 2) <= mouse[0] <= int(WIN / 2 - tiles[i].get_width() / 2 + 40) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                        i -= 1
                        if i == -5:
                            i = 0
                    elif int(WIN / 2 + tiles[i].get_width() / 2 - 40) <= mouse[0] <= int(WIN / 2 + tiles[i].get_width() / 2) and int(WIN / 1.5) <= mouse[1] <= int(WIN / 1.5) + 60:
                        i += 1
                        if i == 5:
                            i = 0
                    elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.25) <= mouse[1] <= int(WIN / 1.25) + 60:
                        self.gameScreen()
                    elif int(WIN / 2 - 150) <= mouse[0] <= int(WIN / 2 - 150) + 300 and int(WIN / 1.12) <= mouse[1] <= int(WIN / 1.12) + 60:
                        self.hscoreScreen
                        

    def mainLoop(self):
        self.makeGrid()
        self.homeScreen()
        # self.gameScreen()
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
