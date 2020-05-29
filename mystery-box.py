# External Libs
import simpleaudio as sa
import json
import random

# Global Variables
quitProgram = False
sfx_path = "./sound-effects"
prevGun = ""
spinCount = 0
guns = []

# Helper methods
def loadGunsFromJson(jsonPath):
    with open('guns.json', 'r') as f:
        data = json.load(f)
        return data['guns']


def playSound(path):
    wave_obj = sa.WaveObject.from_wave_file(f"{path}")
    play_obj = wave_obj.play()
    play_obj.wait_done()


def spinMysteryBox(playAudio):
    index = random.randrange(0, len(guns))
    if (playAudio):
        playSound(f"{sfx_path}/mystery-box.wav")

    prevGun = guns[index]['name']
    print()
    return guns[index]


def quit():
    global quitProgram
    quitProgram = True


# Main
playSound(f"{sfx_path}/round-begin.wav")
guns = loadGunsFromJson('./guns.json')

while quitProgram == False:
    print('Would you like to spin the box?: (Y/N)')
    answer = input()
    print()

    if (answer == 'y' or answer == 'Y'):
        gun = spinMysteryBox(True)
        spinCount += 1
        while gun['name'] == prevGun:
            spinMysteryBox(False)
        print(f"You've gained the {gun['name']}")
        print()
        if (gun['name'] == "Teddy Bear"):
            playSound(f"{sfx_path}./teddy.wav")
            quit()
    else:
        quit()
