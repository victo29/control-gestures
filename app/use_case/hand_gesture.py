import cv2

from app.infra.camera.interfaces.video_stream import VideoStream
from app.infra.hands.interfaces.hands_detector import HandDetector
from app.infra.hands.interfaces.gesture import GestureRecognizer
from app.infra.actions.interfaces.gesture_action import GestureActions

class HandGesture:

    def __init__(self, video_stream:VideoStream , detector:HandDetector, recognizer:GestureRecognizer, action_handler: GestureActions):
        self.__video_stream = video_stream
        self.__detector = detector
        self.__recognizer = recognizer
        self.__action_handler = action_handler

    def run(self):
        while self.__video_stream.is_open():
            frame = self.__video_stream.read()
            frame = cv2.flip(frame, 1)

            img, hands = self.__detector.find_hands(frame)
            if len(hands) == 1:
                gesture = self.__recognizer.get_gesture(hands[0])
                if gesture:
                    self.__action_handler.handle(gesture)

            cv2.imshow("Camera", img)

            if cv2.waitKey(1) == 27:
                break

        self.__video_stream.release()
