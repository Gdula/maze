import pygame
import os

# Grafika

# Tło
bg = pygame.image.load(os.path.join('png', 'maze.png'))

# Grafika Postaci
STAND_R = pygame.image.load(os.path.join('png', 'player_1.png'))
STAND_D = pygame.image.load(os.path.join('png', 'player_2.png'))
STAND_L = pygame.image.load(os.path.join('png', 'player_3.png'))
STAND_U = pygame.image.load(os.path.join('png', 'player_4.png'))

# Grafika pól
BLACK_FIELD = pygame.image.load(os.path.join('png', 'black.png'))
ROCK_FIELD = pygame.image.load(os.path.join('png', 'rock.png'))
YELLOW_FIELD = pygame.image.load(os.path.join('png', 'yellow.png'))

# Okno główne
SIZESCREEN = WIDTH, HEIGHT = 1920, 1080
