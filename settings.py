import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
CELL_SIZE = 40
CELL_NUMBER = 20
SCREEN_SIZE = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
CLOCK = pygame.time.Clock()
GRASS_COLOR = (167, 209, 61)
BACKGROUND_COLOR = (175, 215, 70)
SCORE_COLOR = (56, 74, 12)

# GAME_FONT default size 25 => class Font
"""https://younglinux.info/pygame/font"""
GAME_FONT = pygame.font.Font(r"Font/PoetsenOne-Regular.ttf", 25)
