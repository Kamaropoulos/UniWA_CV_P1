import helpers
import random
import cv2

from filters import filters
from noises import noises
from metrics import metrics
import csv

# Load all images
images = helpers.readImages(['./images to use/' + filename for filename in helpers.getFileNames('./images to use')])

appliedNoise = dict()

# For every loaded images
for i, image in enumerate(images):
    helpers.displayImage(image, "Original " + str(i+1), [1280, 720])
    cv2.waitKey()
        
    # Pick a random noise generator and apply it
    appliedNoise[i] = random.choice(noises)
    imageWithNoise = appliedNoise[i]["apply"](image, 0.13)

    helpers.displayImage(imageWithNoise, appliedNoise[i]["name"] + " " + str(i+1), [1280, 720])
    cv2.waitKey()

    # Apply filters to images and display them
    for filter in filters:
        # Initialize result type if this is the first time we use the filter
        if filter["result"] == None:
            filter["result"] = dict()
        filter["result"][i] = filter["apply"](imageWithNoise)

        # Get and apply the last 2 metrics we have
        for metric in metrics[-2:]:
            if not i in filter["metrics"]:
                filter["metrics"][i] = dict()
            filter["metrics"][i][metric["name"]] = metric["apply"](image, filter["result"][i])
            print(filter["metrics"][i][metric["name"]])
            
        helpers.displayImage(filter["result"][i], filter["name"] + " " + str(i+1), [1280, 720])
        cv2.waitKey()

    
# Name of the CSV file to write
csv_file = "Q2.csv"

# Names for columns
csv_columns = ["Image ID", "Noise Type", "Filter Name", "Performance Score 1 Value", "Performance Score 2 Value"]
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for i, image in enumerate(images):
            data = {
                "Image ID": i+1,
                "Noise Type": appliedNoise[i]["name"]
            }
            for filter in filters:
                data["Filter Name"] = filter["name"]

                for k, metric in enumerate(metrics[-2:]):
                    k = k+1
                    data["Performance Score " + str(k) + " Value"] = filter["metrics"][i][metrics[k]["name"]]

                writer.writerow(data)
except IOError:
    print("I/O error")
