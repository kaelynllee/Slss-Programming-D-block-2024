# Introduction to pygame
# - boilderplate is useful to set up our environments 
# - the sprite class has some really cool things in it 
# Pygame Boilerplate

import random
import pygame as pg
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
NUM_LOGOS = 50
# Create a class representing the dvd log
# - child class of pygame sprites
# - create a constructor 
# image -> visual representative 
# rect -> hitbox representative

class Dvdlogo(pg.sprite.Sprite):
    """Represents DVD logo sprite"""
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/dvd-logo.png")
        
        self.rect = self.image.get_rect()
        # spawn in random location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width) 
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)
        # Veloctiy of Dvd logo
        self.vel_x = random.choice([-6,-5,-4,-3,3,4,5,6,])
        self.vel_y = random.choice([-6,-5,-4,-3,3,4,5,6,])
    def update(self):
        # update the location of the dvd logo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # bouncer if reaches bottom 
        # if the bottom of the sprite is past the bottom of screen
        # conver to negative (* -1)
        if self.rect.bottom > HEIGHT:
            self.vel_y *= -1
        # top 
        if self.rect.top < 0:
            self.vel_y *= -1
        # left 
        if self.rect.left < 0:
            self.vel_x *= -1
        # right
        if self.rect.right > WIDTH:
            self.vel_x *= -1

class Snowflake(pg.sprite.Sprite): 
    def __init__(self, size: int):
        super().__init__()
        self.image = pg.Surface(size,size)
        pg.draw.circle(
            self.image, WHITE, 
            (size // 2, size // 2), size // 2
        )
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2 
        self.rect.centery = HEIGHT // 2
def start():
    """Environment Setup and Game Loop"""
    
    pg.init()


    # --VARIABLES--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    dvdlogo = Dvdlogo()
    # dvdlogo.rect.centerx = WIDTH // 2
    # dvdlogo.rect.centery = HEIGHT // 2

    all_sprites = pg.sprite.Group()

    all_sprites.add(Snowflake(10))
    
    pg.display.set_caption("Snowflakes falling")
    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if pg.key.get_pressed()[pg.K_SPACE]:
                    all_sprites.add(Dvdlogo())
        # Update the location of dvdlogo
        
        all_sprites.update()

        # dvdlogo.rect.x + dvdlogo.vel_x
        # dvdlogo.rect.x = dvdlogo.rect.x + dvdlogo.vel_x 
        # dvdlogo.rect.y + dvdlogo.vel_y
        # print(dvdlogo.rect.x, dvdlogo.rect.y)


        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)
        
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps
        
def main():
    start()

if __name__ == "__main__":
    main()