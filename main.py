import pygame
import sys

# pygame setup
pygame.init()

screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My first game')
clock = pygame.time.Clock()
baby_blue = (178, 185, 235)

x_change = 0
y_change = 0
obstacle = pygame.Rect(400,200, 80, 80)
velocity = 5
dino = pygame.image.load('assets/dino.png')
rect = dino.get_rect()
rect.x = 200
rect.y = 150

direction = [0, 0]

def player(x, y):

    screen.blit(dino,(x, y))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -velocity
            if event.key == pygame.K_RIGHT:
                x_change = velocity
            if event.key == pygame.K_UP:
                y_change = -velocity
            if event.key == pygame.K_DOWN:
                y_change = velocity

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_change = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_change = 0        

    new_rect = rect.copy()
    new_rect.x += x_change
    new_rect.y += y_change

    if not new_rect.colliderect(obstacle):
        rect.x = new_rect.x
        rect.y = new_rect.y

    screen.fill(baby_blue)
    pygame.draw.rect(screen, (58, 73, 92), obstacle)
    screen.blit(dino, rect)
    #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 32, 32))
    #player(x, y)
        
    screen.blit(dino, rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()