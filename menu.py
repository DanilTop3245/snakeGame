import subprocess
import sys, pygame
import settings
from run import run_game


def show_menu():
    while True:
        settings.SCREEN.fill(settings.WHITE)
        draw_text("Snake game", settings.GAME_FONT, settings.BLACK, settings.SCREEN, settings.SCREEN_WIDTH / 2,
                  settings.SCREEN_HEIGHT / 6)
        pygame.draw.rect(settings.SCREEN, settings.PLAY_BUTTON_COLOR, settings.PLAY_BUTTON, border_radius=20)
        pygame.draw.rect(settings.SCREEN, settings.QUIT_BUTTON_COLOR, settings.QUIT_BUTTON, border_radius=20)
        draw_text("Play", settings.GAME_FONT, settings.BLACK, settings.SCREEN, settings.SCREEN_WIDTH / 2,
                  settings.SCREEN_HEIGHT / 2 - 25)
        draw_text("Quit", settings.GAME_FONT, settings.BLACK, settings.SCREEN, settings.SCREEN_WIDTH / 2,
                  settings.SCREEN_HEIGHT / 2 + 85)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if settings.PLAY_BUTTON.collidepoint(mouse_pos):
                    run_game()
                    pygame.quit()
                    sys.exit()
                if settings.QUIT_BUTTON.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


show_menu()
