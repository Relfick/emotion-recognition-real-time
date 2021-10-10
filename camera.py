from cv2 import cv2


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self._check_camera()
        self.frame = None

    def _check_camera(self):
        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

    def get_frame(self, fx=1, fy=1):
        ret, self.frame = self.cap.read()
        if not ret:
            raise AttributeError('Frame is None')

        self.frame = cv2.resize(self.frame, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA)
        return self.frame

    def show_frame(self):
        cv2.imshow('Face', self.frame)

    def wait_key(self):
        c = cv2.waitKey(1)
        if c == 27:  # Esc
            return True
        return False

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()
