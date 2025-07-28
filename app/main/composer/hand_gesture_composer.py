from app.infra.camera.video_stream import VideoStream
from app.infra.hands.gesture import GestureRecognizer
from app.infra.hands.hands_detector import HandDetector
from app.infra.actions.gesture_action import GestureActions
from app.use_case.hand_gesture import HandGesture

def hand_gesture_composer():
    video_stream = VideoStream()
    detector = HandDetector()
    recognizer = GestureRecognizer()
    action_handler = GestureActions()

    use_case = HandGesture(
        video_stream= video_stream,
        detector= detector,
        recognizer = recognizer,
        action_handler = action_handler
    )

    return use_case.run
