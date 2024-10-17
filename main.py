# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, os
from pygame.locals import *
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # os.environ['DISPLAY'] = ':0.0'
    # os.environ['SDL_VIDEODRIVER'] = 'x11'
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # screen.fill(color=(0,0,0))
    screen.fill("black")
   
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()


# pygame.init()
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 return

#         screen.fill("black")
#         pygame.display.flip()