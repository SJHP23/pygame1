import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius


    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_shape):
        distance = self.position.distance_to(other_shape.position)
        total_radii = self.radius + other_shape.radius
        if distance <= total_radii:
            return True
        else:
            return False

