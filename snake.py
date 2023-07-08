import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the game window
window_width = 800
window_height = 600
window_size = (window_width, window_height)
game_window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')

# Set the clock for the game
clock = pygame.time.Clock()

# Set the size of each snake segment
segment_size = 20

# Set the initial speed of the snake
snake_speed = 20

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    rendered_message = font_style.render(msg, True, color)
    game_window.blit(rendered_message, [window_width / 6, window_height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initialize the starting position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Initialize the change in position of the snake
    x1_change = 0
    y1_change = 0

    # Create the snake body as a list of segments
    snake_segments = []
    snake_length = 1

    # Generate the initial position of the food
    food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            game_window.fill(BLACK)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            # Check for key press events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -segment_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = segment_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -segment_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = segment_size
                    x1_change = 0

        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(BLACK)
        pygame.draw.rect(game_window, GREEN, [food_x, food_y, segment_size, segment_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_segments.append(snake_head)
        if len(snake_segments) > snake_length:
            del snake_segments[0]

        for segment in snake_segments[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_segments:
            pygame.draw.rect(game_window, WHITE, [segment[0], segment[1], segment_size, segment_size])

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()


game_loop()



