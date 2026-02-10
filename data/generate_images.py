import numpy as np
import cv2
import os

# Folder to save synthetic images
os.makedirs("data/images", exist_ok=True)

num_images = 10  # number of images to generate
img_size = 128   # image size (128x128 pixels)

for i in range(num_images):
    # create random grayscale image
    img = np.random.randint(0, 256, (img_size, img_size), dtype=np.uint8)
    
    # add a circular "feature" for demonstration
    cv2.circle(img, center=(64, 64), radius=20, color=255, thickness=-1)
    
    # save image
    cv2.imwrite(f"data/images/image_{i+1}.png", img)

print(f"Generated {num_images} synthetic images in data/images/")

