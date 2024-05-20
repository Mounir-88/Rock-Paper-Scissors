import cv2
import pygame
import sys
from pygame.locals import *



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Statistics:
    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.rock_count = 0
        self.paper_count = 0
        self.scissors_count = 0

    def update_statistics(self, winner, player_move):
        if winner == "You win!":
            self.wins += 1
        elif winner == "AI wins!":
            self.losses += 1
        elif winner == "Draw!":
            self.ties += 1

        if player_move == "You Played Rock!":
            self.rock_count += 1
        elif player_move == "You Played Paper!":
            self.paper_count += 1
        elif player_move == "You Played Scissors!":
            self.scissors_count += 1

    def render(self, img):
        cv2.putText(img, "Statistics Page:", (1500, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Wins: {self.wins}", (1500, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Losses: {self.losses}", (1500, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Ties: {self.ties}", (1500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Rock Count: {self.rock_count}", (1500, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Paper Count: {self.paper_count}", (1500, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, f"Scissors Count: {self.scissors_count}", (1500, 800), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    def display_statistics(self):
        print("------ Statistics ------")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Ties: {self.ties}")
        print(f"Rock Count: {self.rock_count}")
        print(f"Paper Count: {self.paper_count}")
        print(f"Scissors Count: {self.scissors_count}")
        print("------------------------")
