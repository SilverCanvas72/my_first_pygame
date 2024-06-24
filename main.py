import pygame
import sys

# pygame setup
pygame.init()

screen_width = 800
screen_height = 400
x = 200
y = 150
velocity = 5
x_change = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My first game')
clock = pygame.time.Clock()
baby_blue = (178, 185, 235)
dino = pygame.image.load('assets/dino.png')
direction = [0, 0]

def player(x, y):

    screen.blit(dino,(x, y))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0

        #keys = pygame.key.get_pressed()

        #if keys[pygame.K_LEFT]:
            #x -= velocity

        #if keys[pygame.K_RIGHT]:
            #x += velocity

        #elif keys[pygame.K_UP]:
            #y -= velocity

        #elif keys[pygame.K_DOWN]:
            #y += velocity  
    x += x_change
    screen.fill(baby_blue)
    player(x, y)




    pygame.display.flip()

    clock.tick(60)

pygame.quit()