import pygame


class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/block.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x,y))


class Map:
    map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def __init__(self):
        self.block_list = []
        self.screen = pygame.display.get_surface()
        count_y = 0
        for y in self.map:
            count_x = 0
            for x in y:
                if x == 1:
                    self.block_list.append(Block(count_x*64, count_y*64))
                count_x += 1
            count_y += 1

    def draw(self, playerOffset):
        for item in self.block_list:
            offset = (item.rect.x + playerOffset[0], item.rect.y + playerOffset[1])
            self.screen.blit(item.image, offset)

    def checkHorizontalCollision(self, player):
        player.rect.x += player.direction.x * player.speed
        for block in self.block_list:
            if player.rect.colliderect(block):
                if player.direction.x > 0:
                    player.rect.right = block.rect.left
                elif player.direction.x < 0:
                    player.rect.left = block.rect.right

    def checkVerticalCollision(self, player):
        player.applyGravity()
        player.rect.y += player.direction.y
        for block in self.block_list:
            if player.rect.colliderect(block):
                if player.direction.y > 0:
                    player.rect.bottom = block.rect.top
                    player.direction.y = 0
                    player.isJump = False
                elif player.direction.y < 0:
                    player.rect.top = block.rect.bottom
                    player.direction.y = 0

    def update(self, player):
        self.draw(player.offset)
        self.checkHorizontalCollision(player)
        self.checkVerticalCollision(player)





