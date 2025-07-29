import cv2
import math

from app.infra.camera.interfaces.video_stream import VideoStream
from app.infra.hands.interfaces.hands_detector import HandDetector
from app.infra.hands.interfaces.gesture import GestureRecognizer
from app.infra.actions.interfaces.gesture_action import GestureActions

class HandGesture:

    def __init__(self, video_stream: VideoStream, detector: HandDetector,
                 recognizer: GestureRecognizer, action_handler: GestureActions):
        self.__video_stream = video_stream
        self.__detector = detector
        self.__recognizer = recognizer
        self.__action_handler = action_handler

    def run(self):
        while self.__video_stream.is_open():
            frame = self.__video_stream.read()
            frame = cv2.flip(frame, 1)

            img, hands = self.__detector.find_hands(frame)

            if self.__hands_too_close(hands) or self.__fingers_too_close(hands):
                cv2.putText(img, "Maos muito proximas - gesto ignorado",
                            (30, 100),  # posição X, Y
                            cv2.FONT_HERSHEY_SIMPLEX, 1.0,  # fonte e tamanho
                            (0, 255, 255),  # cor: amarelo
                            3,  # espessura
                            cv2.LINE_AA)
                gestures = []
            else:
                gestures = self.__recognizer.get_gestures(hands)

            for side in ["Right", "Left"]:
                for gesture, hand_side in gestures:
                    if gesture and hand_side == side:
                        self.__action_handler.handle(gesture)
                        break
                else:
                    continue
                break

            cv2.imshow("Camera", img)

            if cv2.waitKey(1) == 27:
                break

        self.__video_stream.release()


    def __hands_too_close(self, hands: list) -> bool:
        if len(hands) < 2:
            return False

        x1, y1, _ = hands[0]["center"]
        x2, y2, _ = hands[1]["center"]

        distance = math.hypot(x2 - x1, y2 - y1)

        return distance < 200

    def __fingers_too_close(self, hands: list) -> bool:

        if len(hands) < 2:
            return False

        hand1 = hands[0]["coords"]
        hand2 = hands[1]["coords"]

        finger_indices = [4, 8, 12, 16, 20]

        for i in finger_indices:
            x1, y1, _ = hand1[i]
            x2, y2, _ = hand2[i]

            distance = math.hypot(x2 - x1, y2 - y1)

            if distance < 40:
                return True

        return False
