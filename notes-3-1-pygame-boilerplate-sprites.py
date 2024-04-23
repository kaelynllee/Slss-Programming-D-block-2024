# Introduction to pygame
# - boilderplate is useful to set up our environments 
# - the sprite class has some really cool things in it 
# Pygame Boilerplate

import pygame

# Create a class representing the dvd log
# - child class of pygame sprites
# - create a constructor 
# image -> visual representative 
# rect -> hitbox representative

class Dvdlogo(pygame.sprite.Sprite):
    """Represents DVD logo sprite"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/dvd-logo.png/dvd-logo.png")
        
        self.rect = self.image.get_rect()




def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    EMERALD = (21, 219, 147)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    WIDTH = 1280  # Pixels
    HEIGHT = 720
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    pygame.display.set_caption("DVD Logo Screensaver")

    dvdlogo = Dvdlogo()

    all_sprites = pygame.sprite.Group()
    
    all_sprites.add(dvdlogo)

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)
        
        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()