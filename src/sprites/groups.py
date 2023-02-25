# Internal imports
from camera_group import CameraGroup
from decorators.singleton import singleton


@singleton
class SpriteGroups:
    def __init__(self) -> None:
        self.all_sprites = CameraGroup()
