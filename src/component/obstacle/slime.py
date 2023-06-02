import pygame

from random import randint
from src.util.constants import SLIME
from src.component.obstacle.obstacle import Obstacle


class Slime(Obstacle):
    def __init__(self):
        images = SLIME
        index = randint(0, len(images)-1)
        super().__init__(images, index)
        self.rect.y = 330
        self.sprite_index = 0

    def draw(self, display):
        self.image = self.images[self.sprite_index % len(self.images)].convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.obstacle_mask = pygame.mask.from_surface(self.image)
        self.mask = self.obstacle_mask.to_surface(unsetcolor=(0, 0, 0, 0))
        display.blit(self.image, self.rect)
        self.sprite_index += 1
