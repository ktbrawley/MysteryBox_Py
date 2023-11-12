from pygame import mixer


def init():
    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
    mixer.init()
    print()


def play(sound, volume=0.4, loop=False):
    queuedSound = mixer.Sound(sound)
    channel = mixer.find_channel()
    if channel:
        channel.set_volume(volume)
        channel.play(queuedSound, loops=-1 if loop else 0)


def stop():
    mixer.stop()


def fadeout():
    mixer.fadeout(1000)
