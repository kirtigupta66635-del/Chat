import pygame
from settings import *

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite groups setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self, dt):
        # Draw everything
        self.display_surface.fill(WATER_COLOR)
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(dt)
        
        # Testing Text
        font = pygame.font.SysFont('Arial', 30)
        text = font.render("Game is Running! Level Loaded.", True, TEXT_COLOR)
        self.display_surface.blit(text, (500, 350))
      
