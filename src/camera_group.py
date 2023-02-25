# Python imports
from typing import List

# Pip imports
import pygame

# Internal imports
from settings.screen_settings import ScreenSettings
from sprites.base_sprite import BaseSprite
from sprites.player.player import Player


class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player: Player) -> None:
        self.set_camera_offset(player.rect)

        self.display_surface.fill("black")
        for sprite in self.sorted_sprites:
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)

    def set_camera_offset(self, player_rect: pygame.Rect) -> None:
        self.offset.x = player_rect.centerx - ScreenSettings.screen_width / 2
        self.offset.y = player_rect.centery - ScreenSettings.screen_height / 2

    @property
    def sorted_sprites(self) -> List[BaseSprite]:
        return sorted(self.sprites(), key=lambda s: s.z_layer * 10000 + s.rect.centery)
