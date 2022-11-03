import pygame
import math
import bullet


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
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.4
        self.jumpSpeed = -15
        self.isJump = False

        # Bullets
        self.angleInRad = 0
        self.target_x, self.target_y = pygame.mouse.get_pos() - self.offset
        self.bulletX = 0
        self.bulletY = 0
        self.bulletList = []
        # Collision detections

    def getAngle(self):
        self.target_x, self.target_y = pygame.mouse.get_pos() - self.offset
        self.angleInRad = math.atan2(self.target_y - self.rect.center[1], self.target_x - self.rect.center[0])

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

        # TESTING
        if pygame.mouse.get_pressed()[0]:
            self.getAngle()
            self.setBulletSpeed()
            print(self.bulletX, self.bulletY)
            if len(self.bulletList) < 100:
                self.bulletList.append(bullet.Bullet(self))

    def drawBullet(self):
        if self.bulletList:
            for _bullet in self.bulletList:
                _bullet.pos += (_bullet.direction * _bullet.speed)
                offset = pygame.math.Vector2(_bullet.pos[0] + self.offset[0], _bullet.pos[1] + self.offset[1])
                pygame.draw.rect(self.screen, (255, 0, 0), (offset[0], offset[1], 5, 5))

    def applyGravity(self):
        self.direction.y += self.gravity

    def update(self):
        self.controller()
        self.applyGravity()
        self.updateOffSet()
        self.drawBullet()
        self.draw()
