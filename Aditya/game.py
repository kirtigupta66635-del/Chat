# game.py sections

import pygame
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # Pygame initialization
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('My Awesome Game')
        self.clock = pygame.time.Clock()

        # Level instance (Sari game logic level.py handle karega)
        self.level = Level()

    def run(self):
        while True:
            # 1. Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 2. Update Logic
            dt = self.clock.tick(FPS) / 1000  # Delta time for smooth movement
            self.level.run(dt)

            # 3. Refresh Screen
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
        
