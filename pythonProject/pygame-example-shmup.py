# pygame-example-shmup.py
# Shoot 'em Up

import pygame as pg
import random

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = 720
HEIGHT = 1000
SCREEN_SIZE = (WIDTH, HEIGHT)

# Player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("pythonProject/Images/galaga_ship.png").convert()
        self.image.set_colorkey(WHITE)  # Set white as transparent
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)

    def update(self):
        self.rect.center = pg.mouse.get_pos()
        if self.rect.top < HEIGHT - 200:
            self.rect.top = HEIGHT - 200

# Bullet class
class Bullet(pg.sprite.Sprite):
    def __init__(self, player_loc: list):
        super().__init__()
        self.image = pg.Surface((10, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_loc[0]
        self.rect.bottom = player_loc[1]

    def update(self):
        self.rect.y -= 10  # Move bullet upwards
        if self.rect.bottom < 0:  # Remove if off-screen
            self.kill()

# Enemy class
class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))  # Placeholder image
        self.image.fill((255, 0, 0))  # Red color for enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)  # Random horizontal speed

    def update(self):
        self.rect.y += 5  # Move enemy downwards
        self.rect.x += self.speedx  # Move enemy horizontally

        # Wrap around the screen if the enemy goes off-screen
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)  # Random horizontal speed

def start():
    pg.init()
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    all_sprites = pg.sprite.Group()
    bullets = pg.sprite.Group()
    enemies = pg.sprite.Group()

    player = Player()
    all_sprites.add(player)

    pg.display.set_caption("Shoot 'Em Up")

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                bullets.add(Bullet(player.rect.midtop))

        all_sprites.update()
        bullets.update()

        # Spawning enemies
        if len(enemies) < 10:  # Limit number of enemies on screen
            new_enemy = Enemy()
            all_sprites.add(new_enemy)
            enemies.add(new_enemy)

        # Check for collisions between bullets and enemies
        hits = pg.sprite.groupcollide(enemies, bullets, True, True)

        screen.fill(BLACK)
        all_sprites.draw(screen)
        bullets.draw(screen)
        enemies.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    start()
