import pygame


class Bullet:
    def __init__(self, player):
        self.direction = pygame.math.Vector2(player.bulletX, player.bulletY)
        self.speed = 25
        self.pos = pygame.math.Vector2(player.rect.centerx, player.rect.centery)