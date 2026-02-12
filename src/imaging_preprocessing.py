import cv2
import numpy as np
import os

def load_images(folder="data/images/"):
    images = []
    filenames = sorted(os.listdir(folder))
    for f in filenames:
        img = cv2.imread(os.path.join(folder, f), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def normalize_image(img):
    return img / 255.0

def resize_image(img, size=(128, 128)):
    return cv2.resize(img, size)
