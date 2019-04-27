from PIL import Image, ImageFilter
import numpy as np
import tests.test
import random

# Read image
#im = Image.open("Untitled.png")
#width, height = im.size

#im_array = np.array(im)


#pixels = list(im.getdata())


"""
compress image to 8x8 bitmap
:return 8x8 np.array of compressed image
"""
def compress(image: "Image"):
    width, height = image.size
    rows_to_leave = range(0, height+1, int(height/7))
    columns_to_leave = range(0, width+1, int(width/7))
    #print(rows_to_leave)
    image_array = np.array(image)
    new_image_array = np.array([np.array([image_array[i][j] if len(image_array[i][j]) == 3 else image_array[i][j][:3] for j in columns_to_leave]) for i in rows_to_leave])
    #for row in new_image_array:
    #    print(list(row))
    #test = Image.fromarray(new_image_array)
    #test.save("new " + image.filename)
    return new_image_array


def two_colored(compressed_image):
    new_array = np.array([np.array([np.array([0, 0, 0]) if np.linalg.norm(compressed_image[i][j]) < 128 else np.array([255, 255, 255]) for j in range(len(compressed_image))]) for i in range(len(compressed_image[0]))])
    return (new_array.astype(np.uint8))
    #for row in new_array:
    #    print(list(row))
    #r, g, b = np.split(compressed_image, 3, axis=2)
    #r = r.reshape(-1)
    #g = r.reshape(-1)
    #b = r.reshape(-1)

    # Standard RGB to grayscale
    #bitmap = list(map(lambda x: 0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2], zip(r, g, b)))
    #bitmap = np.array(bitmap).reshape([compressed_image.shape[0], compressed_image.shape[1]])
    #bitmap = np.dot((bitmap > 128).astype(float), 255)
    #return bitmap.astype(np.uint8)


def save_compressed(compressed_array: "np.array np.uint8) type", name_to_save):
    image = Image.fromarray(compressed_array.astype(np.uint8))
    image.save(str(name_to_save))


if __name__ == "main":
    tests.test.test()
