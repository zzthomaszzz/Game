import pygame


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

        # Collision detections

    def draw(self):
        offset = pygame.math.Vector2(self.rect.x + self.offset[0], self.rect.y + self.offset[1])
        self.screen.blit(self.image, offset)

    def updateOffSet(self):
        self.offset[0] = self.half_x - self.rect.x
        self.offset[1] = self.half_y - self.rect.y

    def controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self):
        self.controller()
        self.updateOffSet()
        self.draw()

