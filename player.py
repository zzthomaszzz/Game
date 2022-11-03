import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()

        self.image = pygame.image.load("assets/character.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(64, 128))
        # centering the player
        self.half_x = self.screen.get_width() // 2
        self.half_y = self.screen.get_height() // 2
        self.offset = pygame.math.Vector2()

        # Basic movement
        self.speed = 5
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = 0.4
        self.jumpSpeed = -15
        self.isJump = False

        # Bullets
        self.angleInRad = 0
        self.target_x, self.target_y = pygame.mouse.get_pos()
        self.bulletX = 0
        self.bulletY = 0
        # Collision detections

    def getAngle(self):
        self.angleInRad = math.atan2(-(self.target_y - -self.rect.center[1]), self.target_x - self.rect.center[0])

    def setBulletSpeed(self):
        self.bulletX = math.cos(self.angleInRad)
        self.bulletY = math.sin(self.angleInRad)


    def draw(self):
        offset = pygame.math.Vector2(self.rect.x + self.offset[0], self.rect.y + self.offset[1])
        self.screen.blit(self.image, offset)

    def updateOffSet(self):
        self.offset[0] = self.half_x - self.rect.x
        self.offset[1] = self.half_y - self.rect.y

    def controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and not self.isJump:
            self.direction.y = self.jumpSpeed
            self.isJump = True

    def applyGravity(self):
        self.direction.y += self.gravity

    def update(self):
        self.controller()
        self.applyGravity()
        self.updateOffSet()
        self.draw()

