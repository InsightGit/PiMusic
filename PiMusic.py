import pygame
import random
import math
import sys
from pygame.locals import *
queue = 0
pygame.init()
def song(required):
    start = 1
    while start == 1:
        try:
            wav = None
            song = input("Which song would you like to play?")
            while wav != "yes" or "no":
                wav = input("Are you using a wav file?")
                if wav == "yes":
                    wav2 = pygame.mixer.Sound(song)
                    pygame.mixer.Sound.play(wav2,0)
                    start = 0
                    break
                if wav == "no":
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play(0)
                    start = 0
                    break
        except (KeyboardInterrupt,pygame.error):
            if required == False:
                start = 0

song(False)



pygame.display.set_caption('PiMusic')
screen = pygame.display.set_mode((426, 240))
font = pygame.font.SysFont(None, 36)
screen.fill((255, 255, 255))

def draw_text(display_string, font, surface, x_pos, y_pos):
    text_display = font.render(display_string, 1, (0, 0, 0))
    surface.blit(text_display, (x_pos, y_pos))

main_clock = pygame.time.Clock()

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            song(False)
        if event.type == KEYDOWN:
            if event.key == K_q or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()



    main_clock.tick(60)
    draw_text("Click to switch song.",font,screen,0,100)
    pygame.display.update()



