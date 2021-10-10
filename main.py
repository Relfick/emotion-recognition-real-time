from camera import Camera
from emo_rec import EmoRec
from audio import Voice


camera = Camera()
recognizer = EmoRec()
while True:
    frame = camera.get_frame()
    emotion, score, is_stable = recognizer.recognize(frame)
    camera.show_frame()
    if not is_stable:
        Voice.say(emotion)

    print(f'{emotion}, {score}')

    if camera.wait_key():
        break

camera.stop()
