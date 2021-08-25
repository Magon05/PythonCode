import pygame, random, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Snake")
FPS = pygame.time.Clock()
background = pygame.image.load("Background.png")
font = pygame.font.SysFont("Times New Roman", 40, False, True)
score = 0
speed = 15
crush_sound = pygame.mixer.Sound('Sounds/crush.mp3')
eat_sound = pygame.mixer.Sound('Sounds/eat.mp3')
speed_up_sound = pygame.mixer.Sound('Sounds/speed_up.mp3')
pygame.mixer.music.load('Sounds/backgroundmusic.mp3')

def main_menu():
    screen.blit(background, (0, 0))
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run_game = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        newgame_text = font.render("New game", True, (255, 255, 255))
        exit_text = font.render("Exit", True, (255, 255, 255))
        screen.blit(newgame_text, (600, 400))
        screen.blit(exit_text, (600, 450))
        if 770 > mouse[0] > 600 and 440 > mouse[1] > 400:
            if click == (1, 0, 0):
                start_game()
        elif 690 > mouse[0] > 600 and 490 > mouse[1] > 450:
            if click == (1, 0, 0):
                exit()
        pygame.display.update()

class Snake():
    lenght = 2
    x = screen.get_width() // 2
    y = screen.get_height() // 4
    move_x = -10
    move_y = 0
    direction = "l"
    XY = [(x, y)]
    count = 0

    def start_pos(self):
        self.lenght = 20
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 4
        self.move_x = -10
        self.move_y = 0
        self.direction = "l"
        self.XY = [(self.x, self.y)]
        self.count = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            if self.direction != "r":
                self.direction = "l"
                self.move_x = -10
                self.move_y = 0
        if pressed_keys[K_RIGHT]:
            if self.direction != "l":
                self.direction = "r"
                self.move_x = 10
                self.move_y = 0
        if pressed_keys[K_UP]:
            if self.direction != "d":
                self.direction = "u"
                self.move_x = 0
                self.move_y = -10
        if pressed_keys[K_DOWN]:
            if self.direction != "u":
                self.direction = "d"
                self.move_x = 0
                self.move_y = 10

    def draw(self):
        self.x += self.move_x
        self.y += self.move_y
        self.XY += [(self.x, self.y)]
        self.XY = self.XY[-self.lenght:]
        if self.x > screen.get_width():
            self.x = 0
        if self.x < 0:
            self.x = screen.get_width()
        if self.y > screen.get_height():
            self.y = 0
        if self.y < 0:
            self.y = screen.get_height()

        for kx, ky in self.XY:
            pygame.draw.rect(screen, "green", (kx, ky, 20, 20))

    def rise(self, ex, ey):
        global score, speed
        if self.x in range(ex-20, ex+20) and self.y in range(ey-20, ey+20):
            eat_sound.play()
            self.lenght += 1
            score += 1
            if score == 20:
                speed_up_sound.play()
                speed = 20
            elif score == 40:
                speed_up_sound.play()
                speed = 25
            elif score == 60:
                speed_up_sound.play()
                speed = 30
            return True

    def game_over(self):
        if len(set(self.XY)) != len(self.XY):
            return(True)

class Food():
    size = 20
    x = random.randrange(0, screen.get_width()-20)
    y = random.randrange(0, screen.get_height()-20)

    def draw(self):
        pygame.draw.rect(screen, "red", (self.x, self.y, 20, 20))

    def is_eaten(self):
        S.rise(self.x, self.y)
        if S.rise(self.x, self.y) is True:
            self.x = random.randrange(0, screen.get_width()-20)
            self.y = random.randrange(0, screen.get_height()-20)

S = Snake()
F = Food()

def start_game():
    global score, speed
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        score_text = font.render("Record: {}".format(score), True, (255, 255, 255))
        screen.blit(background, (0, 0))
        screen.blit(score_text, (1000, 30))
        S.move()
        S.draw()
        F.draw()
        F.is_eaten()
        if S.game_over() is True:
            crush_sound.play()
            time.sleep(3)
            score = 0
            speed = 15
            S.start_pos()
            break
        pygame.display.update()
        FPS.tick(speed)

main_menu()