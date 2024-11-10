import snake, fruit, sounds


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
    pass


def check_fail():
    for block in snake.snake_body[1::]:
        if block == snake.snake_body[0]:
            game_over()


def update_game():
    snake.moves_snake()
    check_collision()
    check_fail()
