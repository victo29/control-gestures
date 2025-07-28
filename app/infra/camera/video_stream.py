import cv2

from app.infra.camera.interfaces.video_stream import VideoStream as VideoStreamInterface

class VideoStream(VideoStreamInterface):
    def __init__(self, width=1280, height=720):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def is_open(self):
        return self.cap.isOpened()

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Erro ao capturar frame da câmera")
        return frame

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
