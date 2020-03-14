import cv2
from os import listdir
from os.path import isfile, join
import random

def displayImage(image, title, size):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image)
    cv2.resizeWindow(title, size[0], size[1])

def getRandomFile(dir):
    # Get all filenames in directory
    availableFile = [f for f in listdir(dir) if isfile(join(dir, f))]
    # Pick a random image to use
    return random.choice(availableFile)
