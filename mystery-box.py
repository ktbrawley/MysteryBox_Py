# External Libs
import simpleaudio as sa
import simpleaudio.functionchecks as fc
import json
import random
import serial
import time
import sys
import os

# Global Variables
quitProgram = False
sfx_path = f"{os.getcwd()}/sound-effects"
prevGun = ""
spinCount = 0
guns = []
serialPort = None

# Helper methods


def readButtonState(serialPort):
    serialPort.flush()  # it is buffering. required to get the data out *now*
    input = serialPort.readline(100)
    inputStr = input.decode()
    inputStr = inputStr.rstrip()
    inputStr.replace("\\x0", "")
    if (inputStr != ''):
        buttonState = int(inputStr)
        return buttonState


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
    global prevGun
    prevGun = guns[index]['name']
    print()
    return guns[index]


def spinLimit():
    return random.randrange(4, 9)


def readAvailableSerialPorts():
    import serial.tools.list_ports
    myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    port: tuple
    try:
        port = [port for port in myports if 'ttyACM0' or 'COM4' or 'COM6' in port][1]
        print(port)
    except Exception:
        print('No available connections were detected')
        port = None
    return port


def writeBoxGunResultToSerialBuffer(gunName):
    encoded = gunName.encode()
    serialPort.write(encoded)
    time.sleep(2)


def init(availableConnection):
    global serialPort
    serialPort = serial.Serial(availableConnection[0], 9600, timeout=1)
    time.sleep(2)
    print('====Welcome to Mystery Box Generator=====')
    print()
    global guns
    guns = loadGunsFromJson('./guns.json')
    print('Would you like to spin the box?: (Press button to continue)')


def checkSoundConfig():
    fc.LeftRightCheck.run()


def quit():
    global quitProgram
    quitProgram = True


# Main
availableConnection = readAvailableSerialPorts()
if (availableConnection == None):
    sys.exit(0)

init(availableConnection)
spinLimit = spinLimit()
gunName = ""
try:
    while quitProgram == False:
        buttonPressed = readButtonState(serialPort)
        if (buttonPressed == 0):
            if (spinCount >= spinLimit):
                gunName = "Teddy Bear"
                playSound(f"{sfx_path}/teddy.wav")
                writeBoxGunResultToSerialBuffer(gunName)

                spinLimit = random.randrange(4, 9)
                spinCount = 0
                gunName = ""
                print('Would you like to spin the box?: (Press button to continue)')

            else:
                gun = spinMysteryBox(True)
                gunName = gun['name']
                spinCount += 1
                while gunName == prevGun:
                    spinMysteryBox(False)
                writeBoxGunResultToSerialBuffer(gunName)
                print('Would you like to spin the box?: (Press button to continue)')
except:
    print("Something borked...")
    quit()
