# Internal imports
from sprites.groups import SpriteGroups
from sprites.maps.main import MainMap
from sprites.player.player import Player
from sprites.surfaces import GameSurfaces


class World:
    def __init__(self) -> None:
        self.setup()

    def setup(self) -> None:
        GameSurfaces()
        MainMap()
        self.player = Player((640, 360))

    def run(self, dt: float) -> None:
        SpriteGroups().all_sprites.custom_draw(self.player)
        SpriteGroups().all_sprites.update(dt)
