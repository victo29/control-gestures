import mediapipe as mp
import cv2

from app.utils.drawing import draw_hand_landmarks
from app.infra.hands.interfaces.hands_detector import HandDetector as HandDetectorInterface

mp_hands = mp.solutions.hands

class HandDetector(HandDetectorInterface):
    def __init__(self):
        self.hands = mp_hands.Hands()
        self.res_x = 1280
        self.res_y = 720

    def find_hands(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)
        hand_data = []

        if results.multi_hand_landmarks:
            for hand_side, hand_landmarks in zip(results.multi_handedness, results.multi_hand_landmarks):
                coords = [
                    (
                        int(lm.x * self.res_x),
                        int(lm.y * self.res_y),
                        int(lm.z * self.res_x)
                    ) for lm in hand_landmarks.landmark
                ]
                side = hand_side.classification[0].label
                draw_hand_landmarks(img, hand_landmarks)
                hand_data.append({"side": side, "coords": coords})

        return img, hand_data
