import pygame, sys
from pygame.locals import *
import random, time

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1)  # Play indefinitely

# Set the frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Set up the screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Set up inital speed, score, collected coins
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

# Load background image
background = pygame.image.load(".\\resources\\AnimatedStreet.png")

# Set up display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Define Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Define coin class 
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy_pos):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        while self.rect.collidelist(enemy_pos) != -1:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS_COLLECTED
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        elif pygame.sprite.spritecollideany(self, players):
            COINS_COLLECTED += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# DEfine Player class 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Create player, enemy, and coin instances
P1 = Player()
E1 = Enemy()
C1 = Coin([E1.rect])

# Create spire groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
players = pygame.sprite.Group()
players.add(P1)

# Set up event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Set the threshold for the number of coins to trigger speed increase
COIN_THRESHOLD = 10

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()


    coins_collected_text = font_small.render("Coins Collected: " + str(COINS_COLLECTED), True, BLACK)
    coins_collected_rect = coins_collected_text.get_rect()
    coins_collected_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coins_collected_text, coins_collected_rect)

    # Check if the played has collected enough coins to increase enemy speed
    if COINS_COLLECTED >= COIN_THRESHOLD:
        # Increase the speed of all enemies
        for enemy in enemies:
            SPEED += 1
        
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('carcrash.mp3').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()  

    pygame.display.update()
    FramePerSec.tick(FPS)