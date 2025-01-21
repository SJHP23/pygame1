import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots_group, updatable, drawable)

    print("Initial group sizes:")
    print(f"Updatable size: {len(updatable)}")
    print(f"Drawable size: {len(drawable)}")
    print(f"Asteroids size: {len(asteroids)}")

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.move(dt)
        if keys[pygame.K_s]:
            player.move(-dt)
        if keys[pygame.K_LEFT]:
            player.rotate(dt)
        if keys[pygame.K_RIGHT]:
            player.rotate(-dt)
        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            shots_group.add(new_shot)
            


        screen.fill((0, 0, 0))

        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in pygame.sprite.groupcollide(asteroids, shots_group, False, True): asteroid.split()

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()

        drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()   
