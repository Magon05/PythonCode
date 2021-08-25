import pygame
from pygame.locals import *
import time, random

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("CatRunner")
FPS = pygame.time.Clock()
background = pygame.image.load("Image/background.jpg")
score = 0
font = pygame.font.SysFont("arial", 25, False, True)
reload = 0
speed = 10
jump_sound = pygame.mixer.Sound('Sounds/jump_06.wav')
crush_sound = pygame.mixer.Sound('Sounds/crush.mp3')

def menu():
    screen.blit(background, (0, 0))
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run_game = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        newgame_text = font.render("New game", True, (0, 0, 0))
        score_text = font.render("Exit", True, (0, 0, 0))
        screen.blit(newgame_text, (600, 400))
        screen.blit(score_text, (600, 450))
        if 700 > mouse[0] > 600 and 425 > mouse[1] > 400:
            if click == (1, 0, 0):
                game_loop()
        elif 700 > mouse[0] > 600 and 475 > mouse[1] > 450:
            if click == (1, 0, 0):
                exit()
        pygame.display.update()

class Hero(pygame.sprite.Sprite):
    imagelist = ["Image/herorun1.png", "Image/herorun2.png", "Image/herorun3.png", "Image/herorun4.png", "Image/herorun5.png",
                 "Image/herorun6.png", "Image/herorun7.png", "Image/herorun8.png"]
    image = pygame.image.load("Image/herorun1.png")
    rect = image.get_rect(center=(100, 800))

    def walk_and_gravitation(self, animpoint):
        if self.rect.top < 700:
            self.image = pygame.image.load("Image/herofall.png")
            self.rect.move_ip(0, 30)
        else:
            self.image = pygame.image.load(self.imagelist[animpoint])
        screen.blit(self.image, self.rect)

    def jump(self):
        self.image = pygame.image.load("Image/herojump.png")
        #jump_sound.play()
        if self.rect.top > 400:
            self.rect.y -= 100
        screen.blit(self.image, self.rect)

class Rock(pygame.sprite.Sprite):
    image = pygame.image.load("Image/rock.png")
    rect = image.get_rect(center=(1200, 840))

    def draw(self):
        global score, reload
        self.x = random.randrange(1200, 1400)
        if self.rect.right < 0:
            score += 1
            self.rect = self.image.get_rect(center=(self.x, 840))
        elif reload == 1:
            score = 0
            self.rect.left = self.x
        else:
            screen.blit(self.image, self.rect)
            self.rect.move_ip(-25, 0)

class Tree(pygame.sprite.Sprite):
    image = pygame.image.load("Image/tree.png")
    rect = image.get_rect(center=(2500, 800))

    def draw(self):
        global score, reload
        self.x = random.randrange(2500, 3000)
        if self.rect.right < 0:
            score += 1
            self.rect = self.image.get_rect(center=(self.x, 800))
        elif reload == 1:
            score = 0
            self.rect.left = self.x
        else:
            screen.blit(self.image, self.rect)
            self.rect.move_ip(-30, 0)

class Bee(pygame.sprite.Sprite):
    image = pygame.image.load("Image/bee.png")
    rect = image.get_rect(center=(1800, 400))
    anim = 0

    def draw(self):
        global score, reload
        self.x = random.randrange(1600, 1800)
        self.y = random.randrange(400, 500)
        if self.rect.right < 0:
            score += 1
            self.rect = self.image.get_rect(center=(self.x, self.y))
        elif reload == 1:
            score = 0
            self.rect.left = self.x
            self.rect.top = self.y
        else:
            screen.blit(self.image, self.rect)
            self.rect.move_ip(-30, 0)

H1 = Hero()
R1 = Rock()
B1 = Bee()
T1 = Tree()
enemies = pygame.sprite.Group()
enemies.add(R1, B1, T1)

def game_loop():
    global score, speed, reload
    screen.blit(background, (0, 0))
    pygame.mixer.music.load('Sounds/Happy walk.mp3')
    pygame.mixer.music.play()
    animpoint = 0
    run_game = True
    while run_game:
        if animpoint == 8:
            animpoint = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run_game = False

        screen.blit(background, (0, 0))
        if pygame.sprite.spritecollideany(Hero, enemies):
            crush_sound.play()
            time.sleep(3)
            reload = 1
            run_game = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            H1.jump()
        else:
            H1.walk_and_gravitation(animpoint)
        if score == 10:
            speed = 15
        elif score == 20:
            speed = 20
        elif score == 30:
            speed = 25
        elif score == 40:
            speed = 30
        animpoint += 1
        R1.draw()
        B1.draw()
        #T1.draw()
        reload = 0
        score_text = font.render("Record: {}".format(score), True, (0, 0, 0))
        screen.blit(score_text, (1000, 50))
        pygame.display.update()
        FPS.tick(speed)

menu()