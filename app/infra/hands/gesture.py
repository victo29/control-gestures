class GestureRecognizer:
    def __init__(self):
        self.gesture_buffer = {}
        self.required_frames = 20

    def get_gestures(self, hands_data):
        gestures = []

        for hand in hands_data:
            coords = hand["coords"]
            side = hand["side"]

            fingers = [
                coords[8][1] < coords[6][1],
                coords[12][1] < coords[10][1],
                coords[16][1] < coords[14][1],
                coords[20][1] < coords[18][1],
            ]

            gesture = None
            if fingers == [False, False, False, True]:
                gesture = "EXIT"
            elif fingers == [True, False, False, False]:
                gesture = "OPEN_NOTEPAD"
            elif fingers == [False, False, True, True]:
                gesture = "OPEN_CALC"
            elif fingers == [False, False, False, False]:
                gesture = "CLOSE_ALL"

            key = f"{gesture}_{side}"

            if gesture:
                self.gesture_buffer[key] = self.gesture_buffer.get(key, 0) + 1
                if self.gesture_buffer[key] >= self.required_frames:
                    gestures.append((gesture, side))
                    self.gesture_buffer[key] = 0  # reseta para evitar repetição
            else:
                # limpa buffer se gesto não continuar
                for g in list(self.gesture_buffer.keys()):
                    if side in g:
                        self.gesture_buffer[g] = 0

        return gestures
