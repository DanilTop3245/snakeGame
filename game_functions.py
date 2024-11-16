import snake, fruit, sounds, settings


def check_collision():
    if snake.snake_body[0] == fruit.fruit_position:
        fruit.randomize_fruit()
        snake.new_block()
        sounds.SOUND.play()
    for block in snake.snake_body[1::]:
        if block == fruit.fruit_position:
            fruit.randomize_fruit()
            # print('Happy New Year')


def game_over():
    snake.reset_snake()


def check_fail():
    for block in snake.snake_body[1::]:
        if block == snake.snake_body[0]:
            game_over()
    if not 0 <= snake.snake_body[0].x < settings.CELL_NUMBER and not 0 <= snake.snake_body[0].y < settings.CELL_NUMBER:
        game_over()


def update_game():
    snake.moves_snake()
    check_collision()
    check_fail()


def draw_grass():
    pass


def draw_score():
    pass


def draw_elements():
    draw_grass()
    fruit.draw_fruit()
    snake.draw_snake()
    draw_score()

