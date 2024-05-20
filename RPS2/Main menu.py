import pygame
import sys
from pygame.locals import *
from Game import Game
from Settings import Settings
import threading
import moviepy.editor as mp

pygame.init()

mainClock = pygame.time.Clock()

#Video Intro
# video_path = "Images\RPS - Made with Clipchamp.mp4"
#
# video = mp.VideoFileClip(video_path)
#
# preview_thread = threading.Thread(target=video.preview, kwargs={'fullscreen':True})
# preview_thread.start()
#
# video_duration = video.duration

pygame.display.set_caption('Game Intro')
screen = pygame.display.set_mode((1920, 1080))

font = pygame.font.SysFont(None, 100)
fontop = pygame.font.SysFont(None, 64)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

audio_path = "Images\Creepy Organ Music.mp3"
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play(loops=-1)

while True:
    bg = pygame.image.load("Images\homescreen.png")
    bg = pygame.transform.scale(bg, (1920, 1090))
    screen.blit(bg, (0, 0))
    mainMenuRect = pygame.Rect(100, 90, 430, 80)
    pygame.draw.rect(screen, (255, 0, 0), mainMenuRect)
    draw_text('Main Menu', font, (255, 255, 255), screen, 130, 100)

    draw_text('Sponsored by MMT', font, (150, 150, 150), screen, 1250, 970)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect(160, 400, 300, 80)
    button_2 = pygame.Rect(160, 650, 300, 80)

    if button_1.collidepoint((mx, my)):
        if click:
            pygame.mixer.music.stop()
            game_instance = Game()
            game_instance.play_game()
    if button_2.collidepoint((mx, my)):
        if click:
            setting_instance = Settings()
            setting_instance.setting()

    pygame.draw.rect(screen, (0, 20, 255), button_1)
    pygame.draw.rect(screen, (0, 20, 255), button_2)

    draw_text('PLAY', font, (255, 255, 255), screen, 220, 410)
    draw_text('SETTINGS', fontop, (255, 255, 255), screen, 200, 670)

    click = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.display.update()
    pygame.time.Clock().tick(60)
