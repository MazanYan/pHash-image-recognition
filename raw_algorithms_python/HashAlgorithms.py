from functools import reduce

from PIL import Image
import numpy as np


# Class to get images from some folder and hash them with simple pHash algorithm
class HashBuilder:
    def __init__(self, path):
        self.images_path = path

    """
    Compresses image object into 8x8 square array to be used in saving as a new file or recoloring as two-colored image
    for further hash building
    The method saves initial colors with saving only each 7th row/column of image array
    :param (image) an object of Image class
    :return 8x8 numpy image array of uint8 type
    """
    @staticmethod
    def __compress__(image: "Image"):
        width, height = image.size
        rows_to_leave = range(0, height + 1, int(height / 7))
        columns_to_leave = range(0, width + 1, int(width / 7))
        image_array = np.array(image)
        new_image_array = np.array(
            [np.array([image_array[i][j] if len(image_array[i][j]) == 3 else image_array[i][j][:3]
                       for j in columns_to_leave])
             for i in rows_to_leave])
        return new_image_array.astype(np.uint8)

    """
    Rewrites compressed image 8x8 array making him have only two colors - black and white
    Finds average brightness of image and discretizes all other colors,
        making each point with smaller brightness black
        and making each point with greater brightness white
    :param (compressed_image) 8x8 numpy image array of uint8 type that is already compressed by __compress__ method
    :return two-colored 8x8 numpy image array of uint8 type
    """
    @staticmethod
    def __two_colored__(compressed_image):
        all_array_points = np.array(reduce(lambda res_array, row: res_array + list(row), compressed_image, []))
        average_brightness = np.linalg.norm(sum(all_array_points))
        new_array = np.array([np.array(
            [np.array([0, 0, 0]) if np.linalg.norm(compressed_image[i][j]) < average_brightness else np.array([255, 255, 255])
             for j in range(len(compressed_image))])
                              for i in range(len(compressed_image[0]))])
        return new_array.astype(np.uint8)

    """
    Saves compressed image as image file. Is used for tests only
    :param (compressed_array) 8x8 numpy image array of uint8 type
    :param (name_to_save) image name with path to be saved in
    :return None
    """
    @staticmethod
    def __save_compressed__(compressed_array: "np.array np.uint8 type", name_to_save):
        image = Image.fromarray(compressed_array.astype(np.uint8))
        image.save(str(name_to_save))

    """
    Builds hash of compressed two colored 8x8 numpy image array
    Hashes each point into bytearray depending of its' color:
        black point gets hashed into \0 symbol,
        white point gets hashed into \1 symbol
    :param (compressed_array) 8x8 numpy image array of uint8 type
    :return bytearray sequence of \0 and \1 symbols
    """
    @staticmethod
    def __build_hash__(compressed_array: "two colors image array"):
        all_array_points = np.array(reduce(lambda res_array, row: res_array + list(row), compressed_array, []))
        bytearr = "".join(["\0" if (el - np.array([255, 255, 255])).any() else "\1" for el in all_array_points])
        return bytearr.encode()

    """
    Composition of "private" class methods used to create image hash
    Opens image in class folder firstly, then compresses it,
    then discretizes colors array making him hav only two colors, then builds hash
    :param (image_name) name of image file to be imported from class image folder
    :return tuple of image name with path and hash of input image
    """
    def hash_image(self, image_name: "str"):
        return self.images_path + image_name, self.__build_hash__(self.__two_colored__(self.__compress__(Image.open(self.images_path + image_name))))


# Checking how similar two hashes are
class CheckHash:

    # def __init__(self):
    #     self.

    """
    Calculates Hemming distance over two hashes and outputs difference percent
    :param (dict_hash1) the first single-element dict with file name key and hash value as value
    :param (dict_hash2) the second single-element dict with file name key and hash value as value
    :return hemming distance
    """
    @staticmethod
    def similarity_percent(hash1, hash2):
        hemming_distance = reduce(lambda accum, element: accum+1 if element[0]!=element[1] else accum, zip(list(hash1), list(hash2)), 0)
        # 8x8 numpy array
        image_size = 64
        return 1 - hemming_distance/image_size
