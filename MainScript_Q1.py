import cv2
import numpy as np
import random
import time
import skimage.metrics
import csv

import helpers

# Get random image filename
image = helpers.getRandomFile('./images to use')

print("Working with image: " + image)

# Load image
originalImage = cv2.imread('images to use/'+image)

# Display original version of the loaded image
helpers.displayImage(originalImage, "Original", [1280, 720])
cv2.waitKey()

# Configuration for filters to use
filters = [
    {
        "name": 'Blur',
        "apply": lambda image: cv2.blur(image, (5, 5)),
        "result": None,
        "metrics": dict()
    },
    {
        "name": 'Gaussian Blur',
        "apply": lambda image: cv2.GaussianBlur(image, (5, 5), 0),
        "result": None,
        "metrics": dict()
    },
    {
        "name": 'Median Blur',
        "apply": lambda image: cv2.medianBlur(image, 5),
        "result": None,
        "metrics": dict()
    },
    {
        "name": 'Bilateral Filter',
        "apply": lambda image: cv2.bilateralFilter(image, 9, 5, 5),
        "result": None,
        "metrics": dict()
    },
]

# Configuration for metrics to calculate
metrics = [
    {
        "name": 'Mean-Squared Error',
        "apply": lambda original, filtered: skimage.metrics.mean_squared_error(originalImage, filtered)
    },
    {
        "name": 'Normalized Root Mean-Squared Error',
        "apply": lambda original, filtered: skimage.metrics.normalized_root_mse(original, filtered)
    },
    {
        "name": 'Peak Signal to Noise Ratio',
        "apply": lambda original, filtered: skimage.metrics.peak_signal_noise_ratio(originalImage, filtered)
    }
]

# Apply filters to images and display them
for filter in filters:
    filter["result"] = filter["apply"](originalImage)
    helpers.displayImage(filter["result"], filter["name"], [1280, 720])
    cv2.waitKey()

# Compute all metrics for each filter we applied to the original image
for metric in metrics:
    for filter in filters:
        filter["metrics"][metric["name"]] = metric["apply"](originalImage, filter["result"])

# Name of the CSV file to write
csv_file = "Q1_" + image + ".csv"

# Names for columns
csv_columns = ["Filter Name", "Performance Score 1 Value", "Performance Score 2 Value", "Performance Score 3 Value"]
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for filter in filters:
            data = {
                "Filter Name": filter["name"]
            }

            for i in range(1,4):
                data["Performance Score " + str(i) + " Value"] = filter["metrics"][metrics[i-1]["name"]]

            writer.writerow(data)
except IOError:
    print("I/O error")
