# Python imports
from typing import Tuple

# Pip imports
import pygame

# Internal imports
from engine.controlled_sprite import ControlKeys, ControlledSprite
from settings.game_settings import GameSettings
from sprites.surfaces import GameSurfaces


class Player(ControlledSprite):
    def __init__(self, pos: Tuple[int, int]) -> None:
        # Internal imports
        from sprites.groups import SpriteGroups

        control_keys = ControlKeys(up=pygame.K_UP, down=pygame.K_DOWN, right=pygame.K_RIGHT, left=pygame.K_LEFT)
        super().__init__(
            pos,
            GameSurfaces().player,
            0,
            "down_idle",
            control_keys,
            GameSettings.player_speed,
            SpriteGroups().all_sprites,
        )
