import pyautogui
from PIL import Image
import sys
import numpy

while True:
    image = pyautogui.screenshot()
    image = numpy.asarray(image)
    col = int(sum(image[280,60]/3))
    image = image[280:310,270:320]
    image = image != col  
    if image.any() == True:
        pyautogui.press("UP")
        print("Jumping")
    else:
        print("Running")