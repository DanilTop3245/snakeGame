import pygame, sys, time
from pygame.math import Vector2 as vk2
import settings, game_functions, fruit, snake


def run_game():
    fruit.randomize_fruit()
    # pygame.time.set_timer(settings.SCREEN_UPDATE, 100)
    previous_time = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == settings.SCREEN_UPDATE:
                game_functions.update_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if snake.snake_direction.y != 1:
                        snake.snake_direction = vk2(0, -1)
                elif event.key == pygame.K_s:
                    if snake.snake_direction.y != -1:
                        snake.snake_direction = vk2(0, 1)
                elif event.key == pygame.K_d:
                    if snake.snake_direction.x != -1:
                        snake.snake_direction = vk2(1, 0)
                elif event.key == pygame.K_a:
                    if snake.snake_direction.x != 1:
                        snake.snake_direction = vk2(-1, 0)

        current_time = pygame.time.get_ticks()
        delta_time = current_time - previous_time
        if delta_time > settings.SNAKE_SPEED:
            game_functions.update_game()
            previous_time = current_time
        settings.SCREEN_SIZE.fill(settings.BACKGROUND_COLOR)
        game_functions.draw_elements()
        pygame.display.update()
        settings.CLOCK.tick(80)
