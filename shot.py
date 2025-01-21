from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position):
        # Initialize parent classes
        CircleShape.__init__(self, position.x, position.y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Add to sprite groups, if containers exist
        if hasattr(self, "containers"):
            self.add(self.containers)

        # Initialize velocity as zero (to be modified as needed)
        self.velocity = pygame.Vector2(0, 0)

        # Define the image for the Shot (a small circle)
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (SHOT_RADIUS, SHOT_RADIUS), SHOT_RADIUS)

        # Define the rect for positioning the Shot
        self.rect = self.image.get_rect()
        self.rect.center = (position.x, position.y)

        self.position = pygame.Vector2(position.x, position.y)

    def update(self,delta_time):
        self.position += self.velocity * delta_time
        self.rect.center = (self.position.x, self.position.y)
        if(self.position.x < 0 or self.position.x > SCREEN_WIDTH or self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()
