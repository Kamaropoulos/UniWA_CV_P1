import cv2
from os import listdir
from os.path import isfile, join
import random

def displayImage(image, title, size):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.imshow(title, image)
    cv2.resizeWindow(title, size[0], size[1])

def getFileNames(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]

def getRandomFile(dir):
    # Get all filenames in directory
    availableFile = getFileNames(dir)
    # Pick a random image to use
    return random.choice(availableFile)

def readImage(image):
    return cv2.imread(image)

def readImages(images):
    return [readImage(image) for image in images]