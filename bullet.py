import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, sh_game):
        super().__init__()
        self.screen = sh_game.screen
        self.settings = sh_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        
        # Position the bullet based on the ship's direction
        self.rect.centerx = sh_game.ship.rect.centerx  # Center it horizontally on the ship
        self.rect.bottom = sh_game.ship.rect.bottom  # Position it at the ship's top
        
        # Store the bullet's position as a float
        self.x = float(self.rect.x)
    
    def update(self):
        # Move the bullet forward (in the direction of the ship)
        self.x += self.settings.bullet_speed  # Bullet moves to the right
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
