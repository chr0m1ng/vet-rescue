# Python imports
import sys

# Pip imports
import pygame

# Internal imports
from settings.screen_settings import ScreenSettings
from world import World


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Vet Rescue")
        self.screen = pygame.display.set_mode((ScreenSettings.screen_width, ScreenSettings.screen_height))
        self.clock = pygame.time.Clock()
        self.world = World()

    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick() / 1000
            self.world.run(dt)
            pygame.display.update()
