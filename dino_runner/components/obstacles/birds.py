import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_WIDTH


class Birds(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        self.rect.y = 245
        self.rect.x = 600

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.right < 0:
            self.reset_position()
    
    def reset_position(self):
        self.rect.x = SCREEN_WIDTH 
        self.rect.y = random.randint(200, 300)  