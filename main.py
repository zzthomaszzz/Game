import pygame
import sys
import debug
import map
import player
pygame.init()

screen = pygame.display.set_mode((800, 600))
half_w = screen.get_width() // 2
half_h = screen.get_height() // 2
clock = pygame.time.Clock()
game_map = map.Map()
offset = pygame.math.Vector2(0, 0)
player = player.Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        offset -= pygame.math.Vector2(1,0)
    elif keys[pygame.K_a]:
        offset += pygame.math.Vector2(1,0)
    screen.fill((122, 120, 30))
    game_map.update(player)
    player.update()
    pygame.display.update()
    clock.tick(60)