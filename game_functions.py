import pygame

import snake, fruit, sounds, settings, graphics


def check_collision():
    if snake.snake_body[0] == fruit.fruit_position:
        fruit.randomize_fruit()
        snake.add_block()
        sounds.SOUND.play()
    for block in snake.snake_body[1::]:
        if block == fruit.fruit_position:
            fruit.randomize_fruit()
            # print('Happy New Year')


def game_over():
    snake.reset_snake()


def check_fail():
    if not 0 <= snake.snake_body[0].x < settings.CELL_NUMBER or not 0 <= snake.snake_body[0].y < settings.CELL_NUMBER:
        game_over()
    for block in snake.snake_body[1::]:
        if block == snake.snake_body[0]:
            game_over()


def update_game():
    snake.moves_snake()
    check_collision()
    check_fail()



def draw_grass():
    for row in range(settings.CELL_NUMBER):
        for col in range(settings.CELL_NUMBER):
            if (row + col) % 2 == 0:
                grass_rect = pygame.Rect(col * settings.CELL_SIZE, row * settings.CELL_SIZE, settings.CELL_SIZE,
                                         settings.CELL_SIZE)
                pygame.draw.rect(settings.SCREEN_SIZE, settings.GRASS_COLOR, grass_rect)


def draw_score():
    score_text = str(len(snake.snake_body) - 3)
    score_surface = settings.GAME_FONT.render(score_text, True, settings.SCORE_COLOR)
    score_x = int((settings.CELL_SIZE * settings.CELL_NUMBER) - 740)
    score_y = int((settings.CELL_SIZE * settings.CELL_NUMBER) - 768)
    score_rect = score_surface.get_rect(center=(score_x, score_y))
    apple_rect = graphics.APPLE_IMAGE.get_rect(midright=(score_rect.left, score_rect.centery))
    rectangle = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                            apple_rect.height)
    pygame.draw.rect(settings.SCREEN_SIZE, settings.GRASS_COLOR, rectangle)
    settings.SCREEN_SIZE.blit(score_surface, score_rect)
    settings.SCREEN_SIZE.blit(graphics.APPLE_IMAGE, apple_rect)
    pygame.draw.rect(settings.SCREEN_SIZE, settings.SCORE_COLOR, rectangle, 2)


def draw_elements():
    draw_grass()
    fruit.draw_fruit()
    snake.draw_snake()
    draw_score()

