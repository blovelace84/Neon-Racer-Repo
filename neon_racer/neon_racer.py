import pygame
from game_window import WIDTH
from game_window import HEIGHT

# Initialize player properties
player_x = WIDTH // 2
player_y = HEIGHT - 120
player_speed = 7

def move_player(keys, x):
    if keys[pygame.K_LEFT] and x > 0:
        x -= player_speed
    if keys[pygame.K_RIGHT] and x < WIDTH - 60:
        x += player_speed
    return x

# To test, call move_player inside your game loop and draw a rectangle representing the vehicle:
# pygame.draw.rect(screen, (0, 255, 255), (player_x, player_y, 60, 30))