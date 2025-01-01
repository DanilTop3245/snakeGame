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
SCREEN_UPDATE = pygame.USEREVENT
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
SNAKE_SPEED = 50
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAY_BUTTON = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50, 200, 50)
QUIT_BUTTON = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 60, 200, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAY_BUTTON_COLOR = (14, 176, 92)
QUIT_BUTTON_COLOR = (160, 29, 30)

# GAME_FONT default size 25 => class Font
"""https://younglinux.info/pygame/font"""
GAME_FONT = pygame.font.Font(r"Font/PoetsenOne-Regular.ttf", 25)
