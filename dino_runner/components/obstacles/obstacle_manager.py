import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import HAMMER_TYPE



class ObstacleManager:
    def _init_(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])

        obstacles_to_remove = []  # Lista para rastrear obstáculos a serem removidos        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.has_power_up:
                    if game.player.type == HAMMER_TYPE:  # Se o dinossauro tiver o power-up do martelo
                        self.obstacles.remove(obstacle)  # Remova o obstáculo quando o dinossauro estiver com o martelo
                elif not game.player.shield_active:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                else:
                    pass



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []