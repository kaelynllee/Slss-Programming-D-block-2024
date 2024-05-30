import pygame as pg
import random
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
TITLE = "Cakeria"

WIDTH = 1280
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_CAKE = 1 

class Cake(pg.sprite.Sprite):
   def __init__(self):
       super().__init__()
       
       self.image = pg.image.load("cake catcher/images/white.png")

       self.rect = self.image.get_rect()

       self.rect.centerx = random.randrange(0, WIDTH + 1)
       self.rect.centery = random.randrange(0, HEIGHT)
       self.vel_y = random.randrange(3, 7)  

   def update(self):
       self.rect.centery += self.vel_y
       
       if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.y = random.randrange(0, HEIGHT) 

      
def start():
    
    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

 
def main():
    start()
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    background = pg.image.load("cake catcher/images/oven.webp")
    background = pg.transform.scale(background, (WIDTH, HEIGHT))

    cake_sprites = pg.sprite.Group()
    

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state

        # --- Draw items
        screen.fill(BLACK)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y

if __name__ == "__main__":
    main()