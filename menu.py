import sys, pygame
import settings

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 350
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PLAY_BUTTON = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 50, 200, 50)
QUIT_BUTTON = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 60, 200, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAY_BUTTON_COLOR = (14, 176, 92)
QUIT_BUTTON_COLOR = (160, 29, 30)


def show_menu():
    while True:
        SCREEN.fill(WHITE)
        draw_text("Snake game", settings.GAME_FONT, BLACK, SCREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6)
        pygame.draw.rect(SCREEN, PLAY_BUTTON_COLOR, PLAY_BUTTON, border_radius=20)
        pygame.draw.rect(SCREEN, QUIT_BUTTON_COLOR, QUIT_BUTTON, border_radius=20)
        draw_text("Play", settings.GAME_FONT, BLACK, SCREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 25)
        draw_text("Quit", settings.GAME_FONT, BLACK, SCREEN, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 85)
        pygame.display.update()
        


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

show_menu()