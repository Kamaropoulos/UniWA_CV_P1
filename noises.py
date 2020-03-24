import skimage
import numpy as np
import random

def sp(image, param=None):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - param
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < param:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def gauss(image, param=None):
    row,col,ch= image.shape
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy

def poisson(image, param=None):
    vals = len(np.unique(image))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(image * vals) / float(vals)
    return noisy

def speckle(image, param=None):
    row,col,ch = image.shape
    gauss = np.random.randn(row,col,ch)
    gauss = gauss.reshape(row,col,ch)        
    noisy = image + image * gauss
    return noisy

# Configuration for noise types to use
noises = [
    {
        "name": 'Salt and Pepper',
        "apply": lambda image, param: (255*skimage.util.random_noise(image, mode="s&p")).astype(np.uint8)
    },
    {
        "name": 'Gaussian',
        "apply": lambda image, param: (255*skimage.util.random_noise(image, mode="gaussian")).astype(np.uint8)
    },
    {
        "name": 'Poisson',
        "apply": lambda image, param: (255*skimage.util.random_noise(image, mode="poisson")).astype(np.uint8)
    },
    {
        "name": 'Speckle',
        "apply": lambda image, param: (255*skimage.util.random_noise(image, mode="speckle")).astype(np.uint8)
    }
]
