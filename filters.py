import cv2

# Configuration for filters to be used
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
