from fer import FER


class EmoRec:
    def __init__(self, mtcnn=True):
        self.detector = FER(mtcnn=mtcnn)
        self.frame = None
        self.curr_emotion = None
        self.previous_emotion = None
        self.is_stable = False

    def recognize(self, frame):
        self.frame = frame
        self._process_frame()
        self.previous_emotion = self.curr_emotion

        self.curr_emotion, score = self._recognize()
        self.is_stable = self.previous_emotion == self.curr_emotion

        return self.curr_emotion, score, self.is_stable

    def _process_frame(self):
        # Stub yet
        self.frame = self.frame

    def _recognize(self):
        emotion, score = self.detector.top_emotion(self.frame)
        return emotion, score
