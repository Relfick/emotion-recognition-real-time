from playsound import playsound


class Voice:
    emotions = ['sad', 'happy', 'angry']

    @staticmethod
    def say(sound):
        if sound in Voice.emotions:
            Voice._play_audio(f'sounds/sound_{sound}.wav')

    @staticmethod
    def _play_audio(path):
        playsound(path, block=False)

