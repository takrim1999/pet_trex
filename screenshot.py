import pyautogui
from PIL import Image
import sys
import numpy

image = pyautogui.screenshot()
image = numpy.asarray(image)
image[280:310,250:295] = [255,0,0]
print(sum(image[280,60]))
image = Image.fromarray(image)
image.save("image.png")