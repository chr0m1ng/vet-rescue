# Python imports
from typing import List, Tuple

# Pip imports
import pygame
from pygame.sprite import Group
from pygame.surface import Surface

# Internal imports
from settings.game_settings import GameSettings


class BaseSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: Tuple[int, int],
        surface: Surface,
        *groups: Group | List[Group],
        z_layer: int = GameSettings.layers["main"]
    ) -> None:
        super().__init__(*groups)
        self.image = surface
        if self.image:
            self.rect = self.image.get_rect(topleft=pos)
        self.z_layer = z_layer
