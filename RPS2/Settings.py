import pygame
from pygame.locals import *
import sys

pygame.init()

mainClock = pygame.time.Clock()

class Settings:
    def __init__(self):
        self.music_volume = 50
        self.brightness = 50

    def decrease_music_volume(self):
        self.music_volume = max(0, self.music_volume - 10)
        pygame.mixer.music.set_volume(self.music_volume / 100.0)

    def increase_music_volume(self):
        self.music_volume = min(100, self.music_volume + 10)
        pygame.mixer.music.set_volume(self.music_volume / 100.0)



    def setting(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((1920, 1080))

        font = pygame.font.SysFont(None, 100)
        fontop = pygame.font.SysFont(None, 64)
        def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect)
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    
                    if 600 <= event.pos[0] <= 700 and 500 <= event.pos[1] <= 550:
                        self.decrease_music_volume()
                    elif 1200 <= event.pos[0] <= 1300 and 500 <= event.pos[1] <= 550:
                        self.increase_music_volume()
                    elif 800 <= event.pos[0] <= 1100 and 700 <= event.pos[1] <= 780:
                        return


                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            bg = pygame.image.load("Images\homescreen.png")
            bg = pygame.transform.scale(bg, (1920, 1090))
            screen.blit(bg, (0, 0))
            line_color = (255, 255, 255)  


            start_pos = (0, 520)
            end_pos = (1920, 520)
            line_width = 150
            pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)
            draw_text('Sponsored by MMT', font, (150, 150, 150), screen, 1250, 970)

            text = fontop.render(f"Music Volume: {self.music_volume}", True, (0, 0, 0))
            screen.blit(text, (762, 510))
            

            pygame.draw.rect(screen, (255, 255, 255), (600, 500, 100, 50)) 
            pygame.draw.rect(screen, (255, 255, 255), (1200, 500, 100, 50))  
            draw_text('-', font, (0,0,0), screen, 640, 490)
            draw_text('+', font, (0,0,0), screen, 1230, 485)
            
            pygame.draw.rect(screen, (0, 0, 255), (800, 700, 300, 80))
            draw_text('Menu', font, (255,255,255), screen, 855, 710)
        

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    settings_instance = Settings()

    pygame.mixer.music.set_volume(settings_instance.music_volume / 100.0)

    mainClock = pygame.time.Clock()