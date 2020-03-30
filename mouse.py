import pyautogui
import time

MOVE_INTERVAL=0.00001
INIT_X=1
MAX_X=1920-1
INIT_Y=1
MAX_Y=1080-1

x=INIT_X
y=INIT_Y

pyautogui.FAILSAFE=False

while True:
    try:
        pyautogui.moveTo(x,y)
        x+=1
        y+=1
        if x >= MAX_X:
            x=INIT_X
        if y >= MAX_Y:
            y=INIT_Y
        time.sleep(MOVE_INTERVAL)
    except KeyboardInterrupt:
        exit(0)
