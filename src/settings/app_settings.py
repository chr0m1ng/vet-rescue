# Python imports
from pathlib import Path


class AppSettings:
    root_path = Path(__file__).absolute().parent.parent
    assets_path = f"{root_path}/assets"
    maps_path = f"{assets_path}/maps"
    player_path = f"{assets_path}/player"
