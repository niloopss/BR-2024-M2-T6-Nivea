import random
import pygame

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.clock import Clock


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        self.power_up_limit = 1  ##limite de PU que podem aparecer
        self.clock_active = False

    def generate_power_up(self,game):
        current_time = pygame.time.get_ticks() #definindo tempo do jogo em milisegundos
        
        if len(self.power_ups) < self.power_up_limit and current_time - self.when_appears >= random.randint(200, 400):
            self.when_appears = current_time
            random_number = random.random()
            if random_number < 0.33:
                self.power_ups.append(Clock()) 
            elif random_number < 0.66:
                self.power_ups.append(Shield())
            else:
                self.power_ups.append(Hammer())  

    def update(self, game):
        self.generate_power_up(game.score) #gera novos PU usando a pontuação do jogo
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups) ##saber o comportamento dos power ups e a posição
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = power_up.type
                game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)

                if power_up.type == "clock":
                    self.clock_active = True
                    ##diminui a velocidade do jogo quando o "Clock" tiver ativo
                    game.game_speed = 10 
                                
                    self.power_ups.remove(power_up)

        if self.clock_active and pygame.time.get_ticks() >= game.player.power_up_time:
            game.game_speed = 20  #restaura a velocidade normal
            self.clock_active = False

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50, 80)