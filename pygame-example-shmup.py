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

WIDTH = 720  # Pixels
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/galaga_ship.png")

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pg.mouse.get_pos()

       # keep it in the botton 
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        # params: x, u coords of centerx and top
        super().__init__()
        # Green rectangle
        self.image = pg.Surface((10, 25))
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()
    player = Player()
    
    all_sprites.add(player)

    pg.display.set_caption("Slump")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.add((Bullet((player.rect.centerx, player.rect.top))))

        # --- Update the world state
        all_sprites.update()

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