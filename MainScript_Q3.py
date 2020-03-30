import mnist
import random
import numpy as np
import helpers
import cv2

images = mnist.train_images()
labels = mnist.train_labels()

all3 = [i for i, x in enumerate(labels) if x == 3]
all5 = [i for i, x in enumerate(labels) if x == 5]
all8 = [i for i, x in enumerate(labels) if x == 8]
all9 = [i for i, x in enumerate(labels) if x == 9]

threes = [images[x] for i, x in enumerate(random.choices(all3, k=5))]
fives = [images[x] for i, x in enumerate(random.choices(all5, k=5))]
eights = [images[x] for i, x in enumerate(random.choices(all8, k=5))]
nines = [images[x] for i, x in enumerate(random.choices(all9, k=5))]

all = threes + fives + eights + nines

for i, x in enumerate(all):
    helpers.displayImage(x, str(i+1), [500, 500])
cv2.waitKey()
    