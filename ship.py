import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings  # Access settings from main game

        # Load the ship image
        self.image = pygame.image.load('images/rocket_small.png')  # Change to a ship image
        self.rect = self.image.get_rect()

        # Position the ship on the left-center of the screen
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a float value for the ship's vertical position
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the ship’s position based on movement flags
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
