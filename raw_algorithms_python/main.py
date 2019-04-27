from PIL import Image
import numpy as np
from tests.test_functions import *


"""
compress image to 8x8 bitmap
:return 8x8 np.array of compressed image
"""


def compress(image: "Image"):
    width, height = image.size
    rows_to_leave = range(0, height+1, int(height/7))
    columns_to_leave = range(0, width+1, int(width/7))
    image_array = np.array(image)
    new_image_array = np.array([np.array([image_array[i][j] if len(image_array[i][j]) == 3 else image_array[i][j][:3] for j in columns_to_leave]) for i in rows_to_leave])
    return new_image_array


def two_colored(compressed_image):
    new_array = np.array([np.array([np.array([0, 0, 0]) if np.linalg.norm(compressed_image[i][j]) < 128 else np.array([255, 255, 255]) for j in range(len(compressed_image))]) for i in range(len(compressed_image[0]))])
    return (new_array.astype(np.uint8))


def save_compressed(compressed_array: "np.array np.uint8 type", name_to_save):
    image = Image.fromarray(compressed_array.astype(np.uint8))
    image.save(str(name_to_save))


print(__name__)
if __name__ == "__main__":
    test()
