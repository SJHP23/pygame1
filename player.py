import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.original_image = self.image.copy()
        if hasattr(self, "containers"):
            self.add(self.containers)
        forward = pygame.Vector2(0, 1)
        right = pygame.Vector2(0, 1).rotate(90) * self.radius / 1.5
        center = pygame.Vector2(self.radius * 1.5, self.radius * 1.5)
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right

        pygame.draw.polygon(self.image, (255, 255, 255), [a, b, c])
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt # Reduce the timer by delta time
        self.rect.center = self.position

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        self.rect.center = self.position


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        vertices = self.triangle()
        pygame.draw.polygon(screen, (255, 255, 255), vertices)

    def shoot(self):
        if self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position)
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED
        return new_shot
        return None
