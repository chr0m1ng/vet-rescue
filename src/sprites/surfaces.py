# Python imports
from typing import Dict, List

# Pip imports
from pygame.surface import Surface

# Internal imports
from decorators.singleton import singleton
from helpers.assets import import_surfaces_from_folder, import_surfaces_from_subfolders
from settings.app_settings import AppSettings


@singleton
class GameSurfaces:
    player: Dict[str, List[Surface]]
    maps: Dict[str, Surface]

    def __init__(self) -> None:
        self.player = import_surfaces_from_subfolders(AppSettings.player_path)
        self.maps = import_surfaces_from_folder(AppSettings.maps_path)
