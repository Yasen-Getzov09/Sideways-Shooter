class Settings:
    """A class to store all settings for Sideways Shooter."""
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2
        
        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 5
        self.bullet_height = 13
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6