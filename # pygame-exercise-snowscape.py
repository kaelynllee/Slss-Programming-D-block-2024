# pygame-exercise-snowscape.py

import random
import pygame as pg

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1280
HEIGHT = 720
TITLE = "Snowscape"

NUM_SNOW = 50


class Snow(pg.sprite.Sprite):
    def __init__(self, width: int):
    
        super().__init__()

        self.image = pg.Surface((width,width))

        pg.draw.circle(self.image, WHITE, (width// 2, width // 2), width // 2)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        # Initial coords
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = random.randrange(0, HEIGHT)

        self.vel_y = random.randrange(3, 7)
    
    
    def update(self):
        # Take the y position and add the velocity to it
        self.rect.centery += self.vel_y

        # if the y position is greater than HEIGHT, set it back to 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.y = random.randrange(0, HEIGHT) 
           
     
def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    background = pg.image.load("./images/cloud.png")
    background = pg.transform.scale(background, (WIDTH, HEIGHT))


    # Create a snow sprites group
    snow_sprites = pg.sprite.Group()
    for _ in range(NUM_SNOW):
        snow_sprites.add(Snow(12))

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # ----- RENDER
        screen.fill(BLACK)
        screen.blit(background, (0, -(background.get_height() // 2)))

        # Draw all the sprite groups
        snow_sprites.draw(screen)
        

        # ----- UPDATE DISPLAY
        pg.display.flip()
        clock.tick(60)

    pg.quit()

def random_coords():
    x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))
    return x, y


if __name__ == "__main__":
    main() 