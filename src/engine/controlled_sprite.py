# Python imports
from dataclasses import dataclass
from typing import Dict, List, Tuple

# Pip imports
import pygame
from pygame import Surface
from pygame.key import ScancodeWrapper
from pygame.sprite import Group

# Internal imports
from settings.game_settings import GameSettings
from sprites.base_sprite import BaseSprite


@dataclass
class ControlKeys:
    up: int
    down: int
    right: int
    left: int


class ControlledSprite(BaseSprite):
    def __init__(
        self,
        pos: Tuple[int, int],
        surfaces: Dict[str, List[Surface]],
        surface_frame_index: int,
        animation_status: str,
        keys: ControlKeys,
        speed: int,
        *groups: Group | List[Group],
        z_layer: int = GameSettings.layers["main"],
    ) -> None:
        super().__init__(pos, None, *groups, z_layer=z_layer)
        self.control_keys = keys
        self.speed = speed
        self.surfaces = surfaces
        self.surface_frame_index = surface_frame_index
        self.animation_status = animation_status

        self.image = self.surfaces[self.animation_status][self.surface_frame_index]
        self.rect = self.image.get_rect(center=pos)

        self.setup_movement_attributes()

    def setup_movement_attributes(self) -> None:
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)

    def handle_user_input(self, dt: float) -> None:
        pressed_keys = pygame.key.get_pressed()

        self.calculate_direction(pressed_keys)

        self.handle_movement(dt)

    def calculate_direction(self, pressed_keys: ScancodeWrapper) -> None:
        self.calculate_vertical_direction(pressed_keys)
        self.calculate_horizontal_direction(pressed_keys)

        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

    def calculate_vertical_direction(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[self.control_keys.up]:
            self.direction.y = -1
            self.animation_status = "up"
        elif pressed_keys[self.control_keys.down]:
            self.direction.y = 1
            self.animation_status = "down"
        else:
            self.direction.y = 0

    def calculate_horizontal_direction(self, pressed_keys: ScancodeWrapper) -> None:
        if pressed_keys[self.control_keys.right]:
            self.direction.x = 1
            self.animation_status = "right"
        elif pressed_keys[self.control_keys.left]:
            self.direction.x = -1
            self.animation_status = "left"
        else:
            self.direction.x = 0

    def handle_movement(self, dt: float) -> None:
        self.handle_vertical_movement(dt)
        self.handle_horizontal_movement(dt)
        self.set_animation_status()

    def handle_vertical_movement(self, dt: float) -> None:
        self.pos.y += self.calculate_movement_pos(self.direction.y, dt)
        self.rect.centery = self.pos.y

    def handle_horizontal_movement(self, dt: float) -> None:
        self.pos.x += self.calculate_movement_pos(self.direction.x, dt)
        self.rect.centerx = self.pos.x

    def calculate_movement_pos(self, direction: float, dt: float) -> float:
        return direction * self.speed * dt

    def animate(self, dt: float) -> None:
        animation_surfaces = self.surfaces[self.animation_status]
        len_animations = len(animation_surfaces)
        self.surface_frame_index = (self.surface_frame_index + dt * len_animations) % len_animations
        self.image = animation_surfaces[int(self.surface_frame_index)]

    def set_animation_status(self):
        if self.direction.magnitude() == 0:
            self.animation_status = f"{self.animation_status.split('_')[0]}_idle"

    def update(self, dt: float):
        self.handle_user_input(dt)
        self.animate(dt)
