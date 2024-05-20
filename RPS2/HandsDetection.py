import cv2
import mediapipe as mp

class HandsDetection:
    def __init__(self):
        self.mpHand = mp.solutions.hands
        self.hands = self.mpHand.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.lmList = None

    def detect_hands(self, frame):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                lmList = []
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))

                self.mpDraw.draw_landmarks(frame, handLms, self.mpHand.HAND_CONNECTIONS)
                self.lmList = lmList

        return True

    def get_hand_landmarks(self):

        if self.lmList:
            thumb, index, middle, ring, pinky = self.lmList[4], self.lmList[8], self.lmList[12], self.lmList[16], self.lmList[20]
            return thumb, index, middle, ring, pinky
        else:
            return None

    def release_camera(self):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    handsDetection_instance = HandsDetection()
    handsDetection_instance.detect_hands()
    hand_landmarks = handsDetection_instance.get_hand_landmarks()
    print(hand_landmarks) 
    handsDetection_instance.release_camera()
