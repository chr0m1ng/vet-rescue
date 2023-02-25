# Internal imports
from settings.game_settings import GameSettings
from sprites.base_sprite import BaseSprite
from sprites.groups import SpriteGroups
from sprites.surfaces import GameSurfaces


class MainMap(BaseSprite):
    def __init__(self) -> None:
        super().__init__(
            (0, 0), GameSurfaces().maps["main.png"], SpriteGroups().all_sprites, z_layer=GameSettings.layers["ground"]
        )
