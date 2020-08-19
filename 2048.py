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
ARROW = (119, 84, 71)
START = (245, 131,96)


gameLogo = pygame.image.load(os.path.join('Images', '2048_logo.png'))
tiles = [pygame.image.load(os.path.join('Images', 'Tiny.png')), pygame.image.load(os.path.join('Images', 'Classic.png')), pygame.image.load(os.path.join('Images', 'Big.png')), pygame.image.load(os.path.join('Images', 'Bigger.png')), pygame.image.load(os.path.join('Images', 'Huge.png'))]
buttons = [pygame.image.load(os.path.join('Images', 'Left.png')), pygame.image.load(os.path.join('Images', 'Right.png'))]
startGame = pygame.image.load(os.path.join('Images', 'startgame.png'))
hScore = pygame.image.load(os.path.join('Images', 'highscore.png'))


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
        running = True
        tile = tiles[0]
        while running:
            SCREEN.fill(YELLOW)
            SCREEN.blit(tiles[0], (int(WIN / 2 - tile.get_width() / 2), int(WIN / 16)))
            # SCREEN.blit(buttons[0], (int(WIN / 2 - tile.get_width() / 2), int(WIN / 1.5)))
            # SCREEN.blit(buttons[1], (int(WIN / 2 + tile.get_width() / 2 - buttons[1].get_width()), int(WIN / 1.5)))
            pygame.draw.polygon(SCREEN, ARROW, ((int(WIN / 2 - tile.get_width() / 2 + 40), int(WIN / 1.5)), (int(WIN / 2 - tile.get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 - tile.get_width() / 2 + 40), int(WIN / 1.5) + 60)))
            pygame.draw.polygon(SCREEN, ARROW, ((int(WIN / 2 + tile.get_width() / 2 - 40), int(WIN / 1.5)), (int(WIN / 2 + tile.get_width() / 2), int(WIN / 1.5) + 30), (int(WIN / 2 + tile.get_width() / 2 - 40), int(WIN / 1.5) + 60)))
            titleLabel = titleFont.render('Tiny (3x3)', 1, BROWN)
            SCREEN.blit(titleLabel, (int(WIN / 2 - titleLabel.get_width() / 2), int(WIN / 1.5)))
            SCREEN.blit(startGame, (int(WIN / 2 - startGame.get_width() / 2), int(WIN / 1.25)))
            SCREEN.blit(hScore, (int(WIN / 2 - hScore.get_width() / 2), int(WIN / 1.12)))
            # pygame.draw.line(SCREEN, ARROW, (10, 10), (40,30), 15)
            # pygame.draw.line(SCREEN, ARROW, (40,30), (10, 60), 15)

            pygame.display.update()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_s]:
                self.gameScreen()

    def mainLoop(self):
        # self.makeGrid()
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
