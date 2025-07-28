class GestureRecognizer:

    def get_gesture(self, hand):
        coords = hand["coords"]
        fingers = [
            coords[8][1] < coords[6][1],
            coords[12][1] < coords[10][1],
            coords[16][1] < coords[14][1],
            coords[20][1] < coords[18][1],
        ]

        if fingers == [True, False, False, True]:
            return "EXIT"
        elif fingers == [True, False, False, False]:
            return "OPEN_NOTEPAD"
        return None
