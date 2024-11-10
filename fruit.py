import pygame, random
import settings, graphics
from pygame.math import Vector2 as vk2

fruit_position = vk2(0, 0)


def randomize_fruit():
    global fruit_position
    fruit_position.x = random.randint(0, settings.CELL_NUMBER - 1)
    fruit_position.y = random.randint(0, settings.CELL_NUMBER - 1)


def draw_fruit():
    fruit_rect = pygame.Rect(int(fruit_position.x * settings.CELL_SIZE), int(fruit_position.y * settings.CELL_SIZE),
                             settings.CELL_SIZE, settings.CELL_SIZE)
    settings.SCREEN_SIZE.blit(graphics.APPLE_IMAGE, fruit_rect)
