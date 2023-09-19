from dino_runner.utils.constants import CLOCK, CLOCK_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Clock(PowerUp):
    def __init__(self):
        self.image = CLOCK 
        self.type = CLOCK_TYPE 
        super().__init__(self.image, self.type)
