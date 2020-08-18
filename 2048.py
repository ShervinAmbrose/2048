import pygame
import sys
import os

WIN = 800
ROWS = 50

CAPTION = '2048'
SCREEN = pygame.display.set_mode((WIN, WIN))

YELLOW = (250, 248, 239)
BROWN = (187, 173, 161)

gameLogo = pygame.image.load(os.path.join('Images', '2048_logo.png'))
tiles = [pygame.image.load(os.path.join('Images', 'Tiny.png')), pygame.image.load(os.path.join('Images', 'Classic.png')), pygame.image.load(os.path.join('Images', 'Big.png')), pygame.image.load(os.path.join('Images', 'Bigger.png')), pygame.image.load(os.path.join('Images', 'Huge.png'))]
buttons = [pygame.image.load(os.path.join('Images', 'Left.png')), pygame.image.load(os.path.join('Images', 'Right.png'))]
startGame = pygame.image.load(os.path.join('Images', 'startgame.png'))
hScore = pygame.image.load(os.path.join('Images', 'highscore.png'))


class Game(object):
    def __init__(self):
        self.done = False

    def gameScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 40, 0, 0)
        running = True
        while running:
            SCREEN.fill(YELLOW)
            
            pygame.display.update()


    """ 
    This function displays all the images and text on the home screen
    """    
    def homeScreen(self):
        titleFont = pygame.font.SysFont('comicsansms', 40, 0, 0)
        running = True
        while running:
            SCREEN.fill(YELLOW)
            SCREEN.blit(tiles[0], (int(WIN / 2 - tiles[0].get_width() / 2), int(WIN / 16)))
            SCREEN.blit(buttons[0], (int(WIN / 2 - tiles[0].get_width() / 2), int(WIN / 1.5)))
            SCREEN.blit(buttons[1], (int(WIN / 2 + tiles[0].get_width() / 2 - buttons[1].get_width()), int(WIN / 1.5)))
            titleLabel = titleFont.render('Tiny (3x3)', 1, BROWN)
            SCREEN.blit(titleLabel, (int(WIN / 2 - titleLabel.get_width() / 2), int(WIN / 1.5)))
            SCREEN.blit(startGame, (int(WIN / 2 - startGame.get_width() / 2), int(WIN / 1.25)))
            SCREEN.blit(hScore, (int(WIN / 2 - hScore.get_width() / 2), int(WIN / 1.12)))
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
        # self.homeScreen()
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
