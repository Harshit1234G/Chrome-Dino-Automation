import pyautogui as pg
from PIL import ImageGrab
from time import sleep


def isColliding(data):
    #for cactus
    for i in range(220, 270):
        for j in range(430, 480):
            if data[i, j] == 172:
                return 1
    #for bird 
    for i in range(220, 270):
        for j in range(380, 405):
            if data[i, j] == 172:
                return 2
            

if __name__ == "__main__":
    print('Starting in 3 seconds switch to Chrome Dino tab.')
    sleep(3)
    pg.press('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()

        # #for cactus
        # for i in range(220, 270):
        #     for j in range(430, 480):
        #         data[i, j] = 255

        # #for bird
        # for i in range(220, 270):
        #     for j in range(380, 405):
        #         data[i, j] = 200

        match isColliding(data):
            case 1:
                pg.press('up')
            case 2: 
                pg.keyDown('down')
                sleep(.3)
                pg.keyUp('down')

        # image.show()
        # break