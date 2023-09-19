import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = CLOUD
        self.x = SCREEN_WIDTH
        self.y = random.randint(50, 100)
        self.width = self.image.get_width()

    def update(self, game_speed = 15):
        self.x -= game_speed
        if self.x < - self.width:
            self.x = SCREEN_WIDTH
            self.y = random.randint(20, 100)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))        