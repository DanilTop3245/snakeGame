import pygame
import settings, graphics
from pygame.math import Vector2 as vk2

snake_body = [vk2(5, 10), vk2(4, 10), vk2(3, 10)]
snake_direction = vk2(0, 0)
new_block = False
snake_head_img = graphics.HEAD_UP
snake_tail_img = graphics.TAIL_DOWN


def update_head_graphics():
    global snake_head_img
    if len(snake_body) > 1:
        head_direction = snake_body[1] - snake_body[0]
        if head_direction == vk2(-1, 0):
            snake_head_img = graphics.HEAD_RIGHT
        elif head_direction == vk2(1, 0):
            snake_head_img = graphics.HEAD_LEFT
        elif head_direction == vk2(0, -1):
            snake_head_img = graphics.HEAD_DOWN
        elif head_direction == vk2(0, 1):
            snake_head_img = graphics.HEAD_UP


def update_tail_graphics():
    global snake_tail_img
    if len(snake_body) > 1:
        tail_direction = snake_body[1] - snake_body[2]
        if tail_direction == vk2(1, 0):
            snake_tail_img = graphics.TAIL_LEFT
        elif tail_direction == vk2(-1, 0):
            snake_tail_img = graphics.TAIL_RIGHT
        elif tail_direction == vk2(0, 1):
            snake_tail_img = graphics.TAIL_UP
        elif tail_direction == vk2(0, -1):
            snake_tail_img = graphics.TAIL_DOWN


def add_block():
    global new_block
    new_block = True


def reset_snake():
    global snake_body, snake_direction, new_block
    snake_body = [vk2(5, 10), vk2(4, 10), vk2(3, 10)]
    snake_direction = vk2(0, 0)
    new_block = False


def draw_snake():
    update_head_graphics()
    update_tail_graphics()
    for idx, block in enumerate(snake_body):
        x_pos = block.x * settings.CELL_SIZE
        y_pos = block.y * settings.CELL_SIZE
        rectangle = pygame.Rect(x_pos, y_pos, settings.CELL_SIZE, settings.CELL_SIZE)
        if idx == 0:
            settings.SCREEN_SIZE.blit(snake_head_img, rectangle)
        elif idx == len(snake_body) - 1:
            settings.SCREEN_SIZE.blit(snake_tail_img, rectangle)
        else:
            prev_block = snake_body[idx - 1] - block  # tail
            next_block = snake_body[idx + 1] - block  # head
            if prev_block.x == next_block.x:
                settings.SCREEN_SIZE.blit(graphics.BODY_VERTICAL, rectangle)
            elif prev_block.y == next_block.y:
                settings.SCREEN_SIZE.blit(graphics.BODY_HORIZONTAL, rectangle)
            else:
                pass


def moves_snake():
    global snake_body, new_block, snake_direction
    if snake_direction != vk2(0, 0):
        if new_block:
            snake_body_copy = snake_body.copy()
            snake_body_copy.insert(-2, snake_body_copy[-2]+snake_direction)
            snake_body = snake_body_copy
            new_block = False
        else:
            new_block = True
            snake_direction = vk2(0, 0)
            # змейка не должна изменять позицию
