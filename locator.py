import pyautogui
n = 0
while n<100:
    try:
        print(pyautogui.locateOnScreen('clean.png'))
    except:
        pass
    n = n + 1