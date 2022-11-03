import pygame


class Bullet:
    def __init__(self, player):
        self.direction = pygame.math.Vector2(player.bulletX, player.bulletY)
        self.speed = 10
        self.pos = pygame.math.Vector2(player.rect.x, player.rect.y)