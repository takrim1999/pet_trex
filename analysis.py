import pyautogui
from PIL import Image
import sys
import numpy
# clean = numpy.asarray(Image.open("clean.png").convert('RGB'))
# numpy.set_printoptions(threshold=sys.maxsize)
# capturing working canvus

# clean = clean < 254

# image = pyautogui.screenshot(region=(159,267,423,42))
# data = numpy.asarray(image)
# data = data < 255
#Box(left=235, top=275, width=25, height=26)
while True:
    image = pyautogui.screenshot()
    image = numpy.asarray(image)
    image = image[280:305,260:285]
    image = image < 255
    if image.any() == True:
        pyautogui.press("UP")
        print("Jumping")
    else:
        print("Running")

# image = pyautogui.screenshot()
# image = numpy.asarray(image)
# image[280:305,260:285] = [255,0,0]
# image = Image.fromarray(image)
# image.save("image.png")
#     print("ok")
# else:
#     print("Not Ok")
# for i in range(280,306):
#     for j in range(260,286):
#         image[i][j] = [0,0,0]


# while True:
#     image = pyautogui.screenshot(region=(159,267,423,42))
#     data = numpy.asarray(image)
#     data = data < 254
#     if data == clean:
#         print("No obstacles")
#     else:
#         print("Danger")
# print(clean)
# print(data)