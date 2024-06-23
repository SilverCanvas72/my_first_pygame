import pygame
import sys

# pygame setup
pygame.init()

screen_width = 400
screen_height = 300
x = 200
y = 150

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
baby_blue = (178, 185, 235)
dino = pygame.image.load('assets/dino.png')
direction = [0, 0]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = [-10, 0]
            elif event.key == pygame.K_RIGHT:
                direction = [10, 0]
            elif event.key == pygame.K_UP:
                direction = [0, -10]        
            elif event.key == pygame.K_DOWN:
                direction = [0, 10]       

        x += direction[0]
        y += direction[1]

    
    
    screen.fill(baby_blue)

    screen.blit(dino,(x, y))



    pygame.display.flip()

    clock.tick(60)

pygame.quit()