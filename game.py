import pygame
import os

WIDHT, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDHT, HEIGHT)) # set the window
pygame.display.set_caption("2 V 2 Space Shooting Game")

WHITE =  (255,255,255)

FPS = 60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IAMGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

def draw_window():
    WIN.fill(WHITE)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
