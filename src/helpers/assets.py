# Python imports
from typing import Dict, List

# Pip imports
import pygame
from pygame.surface import Surface

# Internal imports
from helpers.folders import list_folder_files, list_subfolders_files


def import_surfaces_from_subfolders(path: str) -> Dict[str, List[Surface]]:
    subfolders = list_subfolders_files(path)
    return {folder: [pygame.image.load(img["full_path"]) for img in imgs] for folder, imgs in subfolders.items()}


def import_surfaces_from_folder(path: str) -> Dict[str, Surface]:
    return {file["file_name"]: pygame.image.load(file["full_path"]).convert_alpha() for file in list_folder_files(path)}
