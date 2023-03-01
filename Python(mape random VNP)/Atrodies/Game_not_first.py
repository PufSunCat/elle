import pygame
import random

pygame.init()

window = pygame.display.set_mode([480, 715])
pygame.display.set_caption('Pew pew Spaceship')

BACKGROUND = pygame.image.load('stars.jpg')
SPACESHIP = pygame.image.load('spaceship.png')
ASTEROID = pygame.image.load('asteroid.png')
MISSILE = pygame.image.load('missile.png')

FONT = pygame.font.SysFont('')    #hfvzyhjffgjhfzhvfhzv

spaceship_x = 100
spaceship_y = 100

spaceship_x_change = 0
spaceship_y_change = 0

health = 100
score = 0

asteroids_coord = []
missile_coord = []

def add_asteroid():
    asteroid_x = random.randint(20, 420)
    asteroid_y = random.randint(-100, -30)

    asteroids_coord.append([asteroid_x, asteroid_y])

# izveidoju custom notikumu
CREATE_ASTEROID = pygame.USEREVENT
pygame.time.set_timer(CREATE_ASTEROID, 215)

while True:

    # saraksts ar visiem notikumiem
    events = pygame.event.get()

    for event in events: 

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                spaceship_y_change = -0.3
                spaceship_x_change = 0

            elif event.key == pygame.K_a:
                spaceship_y_change = 0
                spaceship_x_change = -0.3

            elif event.key == pygame.K_s:
                spaceship_y_change = 0.3
                spaceship_x_change = 0

            elif event.key == pygame.K_d:
                spaceship_y_change = 0
                spaceship_x_change = 0.3

            elif event.key == pygame.K_e:
                missile_x = spaceship_x + (SPACESHIP.get_width() / 2)
                missile_y = spaceship_y + MISSILE.get_height()

                missile_coord.append([missile_x, missile_y])

        if event.type == CREATE_ASTEROID:
            add_asteroid()

    if spaceship_x < 0 or spaceship_x > 436:
        spaceship_x_change = -spaceship_x_change

    if spaceship_y < 0 or spaceship_y > 651:
        spaceship_y_change = -spaceship_y_change

    spaceship_x += spaceship_x_change
    spaceship_y += spaceship_y_change

    window.blit(BACKGROUND, [0, 0])
    window.blit(SPACESHIP, [spaceship_x, spaceship_y])

    text = FONT.render(f'Cats kill:{score}', True, [234, 76, 82])
    window.blit(text, [10,10])

    for coords in missile_coord:
        coords[1] -= 0.8
        window.blit(MISSILE, coords)

        if coords[1] < -100:
            missile_coord.remove(coords)

    for asteroid_coords in asteroids_coord:
        asteroid_coords[1] += 0.4
        window.blit(ASTEROID, asteroid_coords)

        if asteroid_coords[1] > 800:
            asteroids_coord.remove(asteroid_coords)

        asteroid_rect = ASTEROID.get_rect()
        missile_rect = MISSILE.get_rect()
        spaceship_rect = SPACESHIP.get_rect()

        asteroid_rect.topleft = asteroid_coords
        spaceship_rect.topleft = [spaceship_x, spaceship_y]

        if asteroid_rect.colliderect(spaceship_rect):
            health -= 15
            asteroids_coord.remove(asteroid_coords)


        # katru asteroidu matchojam ar katru missile
        for coords in missile_coord:
            asteroid_rect.topleft = asteroid_coords
            missile_rect.topleft = coords

            if asteroid_rect.colliderect(missile_rect):
                missile_coord.remove(coords)
                asteroids_coord.remove(asteroid_coords)

        if health <= 0:
            pygame.quit()

    pygame.display.update()
    #eee