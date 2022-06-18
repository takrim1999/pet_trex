import pyautogui
from PIL import Image
import sys
import numpy
clean = numpy.asarray(Image.open("clean.png").convert('RGB'))
numpy.set_printoptions(threshold=sys.maxsize)
# capturing working canvus

clean = clean < 254

# image = pyautogui.screenshot(region=(159,267,423,42))
# data = numpy.asarray(image)
# data = data < 255


while True:
    image = pyautogui.screenshot(region=(159,267,423,42))
    data = numpy.asarray(image)
    data = data < 254
    if data == clean:
        print("No obstacles")
    else:
        print("Danger")
# print(clean)
# print(data)