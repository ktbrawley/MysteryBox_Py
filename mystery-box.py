
import simpleaudio as sa
import json
import random
quitProgram = False
sfx_path = "./sound-effects"

#====HELPER METHODS=====#
def loadGunsFromJson(jsonPath):
    with open('guns.json', 'r') as f:
        data = json.load(f)
        return data['guns'];

def playSound(path):
    wave_obj = sa.WaveObject.from_wave_file(f"{path}")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def spinMysteryBox():
    index = random.randrange(0, len(guns))
    playSound(f"{sfx_path}/mystery-box.wav")
    print(guns[index]['name']);
    return guns[index]


#====MAIN=====#
playSound(f"{sfx_path}/round-begin.wav")

guns = loadGunsFromJson('./guns.json');
gun = spinMysteryBox()

if(gun['name'] == "Teddy Bear"):
    playSound(f"{sfx_path}./teddy.wav")




