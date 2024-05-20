import cv2
import time
import random

import numpy as np

from HandsDetection import HandsDetection
from Statistics import Statistics
import pygame.camera
import pygame.image
from pygame.locals import *

class Game:
    def __init__(self):
        self.hands_detector = HandsDetection()
        self.play = False
        self.result = False
        self.TF = True
        self.move = ""
        self.cmove = ""
        self.winner = ""
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.background = cv2.imread("Images/gamescreen.png")
        self.initial_time = time.time()
        self.statistics = Statistics(self.background)

        self.screen_width, self.screen_height = 1920, 1080
        self.display_surface = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        

    def play_game(self):
        pygame.init()
        audio_path1 = pygame.mixer.Sound("Images/battle.mp3")
        audio_path = pygame.mixer.Sound("Images/rps.mp3")
        audio_path1.play(loops=-1)
        audio_path1.set_volume(0.7)
        # screenshot_index = 0

        flag = -1
        while True:
            success, img = self.cap.read()

            if not self.hands_detector.detect_hands(img):
                continue

            img = cv2.resize(img, (640, 480))
            

            background = cv2.resize(self.background, (1920, 1100))
            
            display_img = background.copy()
            display_img[200:680, 150:790] = img
            cv2.line(display_img, (1400, 0), (1400, 1090), (0,0,0), 5)
            self.statistics.render(display_img)
            self.display_surface.blit(pygame.surfarray.make_surface(cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)),
                                      (0, 0))

            key = cv2.waitKey(1)
            if key == 27:  
                break

            if key == ord("s"):
                self.play = True
                self.result = False
                self.initial_time = time.time()
                self.move = ""
                self.cmove = ""
                self.winner = ""   
                audio_path.play()
                audio_path.set_volume(1.2)



            if self.play:
                if self.result is False:
                    timer = time.time() - self.initial_time
                    
                    hand_landmarks = self.hands_detector.get_hand_landmarks()
                    if hand_landmarks:
                        thumb, index, middle, ring, pinky = hand_landmarks


                    if timer <= 1:
                        cv2.putText(display_img, "Rock", (270, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 5)
                    elif timer <= 2:
                        cv2.putText(display_img, "Paper", (270, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 5)
                    elif timer <= 3:
                        cv2.putText(display_img, "Scissors", (160, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 5)
                    elif timer <4:
                        cv2.putText(display_img, "SHOOT!!!", (150, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 5)
                    else:
                        cv2.putText(display_img, "", (270, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0), 5)

                        

                        options = ("rock", "paper", "scissors")
                        computer = random.choice(options)

                        if index[1] < thumb[1] and middle[1] < thumb[1] and ring[1] < thumb[1] and pinky[1] < thumb[1]:
                            flag = 0
                        elif index[1] > thumb[1] and middle[1] > thumb[1] and ring[1] > thumb[1] and pinky[1] > thumb[1]:
                            flag = 1
                        elif index[1] > thumb[1] or middle[1] > thumb[1]:
                            flag = 2

                        if flag == 0:
                            self.move = "You Played Rock!"
                            
                        elif flag == 1:
                            self.move = "You Played Paper!"
                            
                        elif flag == 2:
                            self.move = "You Played Scissors!"
                            
                        else:
                            self.move = "Move was not recognized..."

                        if computer == "rock":
                            self.cmove = "The AI Played Rock!"
                        elif computer == "paper":
                            self.cmove = "The AI played Paper!"
                        else:
                            self.cmove = "The AI played Scissors!"

                        if computer == "rock" and flag == 0:
                            self.winner = "Draw!"
                        elif computer == "paper" and flag == 1:
                            self.winner = "Draw!"
                        elif computer == "scissors" and flag == 2:
                            self.winner = "Draw!"
                        elif computer == "rock" and flag == 1:
                            self.winner = "You win!"
                        elif computer == "rock" and flag == 2:
                            self.winner = "AI wins!"
                        elif computer == "paper" and flag == 0:
                            self.winner = "AI wins!"
                        elif computer == "paper" and flag == 2:
                            self.winner = "You win!"
                        elif computer == "scissors" and flag == 0:
                            self.winner = "You win!"
                        elif computer == "scissors" and flag == 1:
                            self.winner = "AI wins!"
                        self.statistics.update_statistics(self.winner, self.move)
                        self.play = False

                        

            cv2.putText(display_img, self.move, (920, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(display_img, self.cmove, (910, 560), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            if self.winner == "AI wins!":
                cv2.putText(display_img, self.winner, (860, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 3)
            elif self.winner == "Draw!":
                cv2.putText(display_img, self.winner, (890, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 3)
            elif self.winner == "You win!":
                cv2.putText(display_img, self.winner, (845, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 0), 3)

            cv2.putText(display_img, "Press 'S' to play again or 'ESC' to exit", (155, 800), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2)

            cv2.imshow("Game Started", display_img)

            key = cv2.waitKey(1) 
            if key == 27: 
                break
        audio_path1.stop()
        audio_path = "Images\Creepy Organ Music.mp3"
        pygame.mixer.music.load(audio_path)     
        pygame.mixer.music.play(loops=-1)
        self.cap.release()
        cv2.destroyAllWindows()
        self.statistics.display_statistics()

if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
