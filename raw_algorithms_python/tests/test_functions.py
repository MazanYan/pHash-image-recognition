from main import *
import os
import unittest


class Test(unittest.TestCase):

    def test_compressing(self):
        get_image_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
        hashed_path = os.path.dirname(os.path.realpath(__file__)) + "/hashed_images/"

        try:
            random_drawing = compress(Image.open(get_image_path + "Untitled.png"))
            parrot_image = compress(Image.open(os.path.abspath(get_image_path + "photo_2018-12-10_22-28-40.jpg")))
            letter_ts = compress(Image.open(os.path.abspath(get_image_path + "Ц.png")))
            comic_con_photo = compress(Image.open(os.path.abspath(get_image_path + "kiev comic conS80922-141312.jpg")))
            print("Images compress")
        except:
            self.assertTrue(False)

    def test_saving(self):
        get_image_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
        hashed_path =  os.path.dirname(os.path.realpath(__file__)) + "/hashed_images/"

        random_drawing = compress(Image.open(get_image_path + "Untitled.png"))
        parrot_image = compress(Image.open(os.path.abspath(get_image_path + "photo_2018-12-10_22-28-40.jpg")))
        letter_ts = compress(Image.open(os.path.abspath(get_image_path + "Ц.png")))
        comic_con_photo = compress(Image.open(os.path.abspath(get_image_path + "kiev comic conS80922-141312.jpg")))

        try:
            save_compressed(two_colored(random_drawing), hashed_path + "new random.png")
            save_compressed(two_colored(parrot_image), hashed_path + "new parrot.png")
            save_compressed(two_colored(letter_ts), hashed_path + "new letter.png")
            save_compressed(two_colored(comic_con_photo),hashed_path + "new comic con photo.png")
            save_compressed(two_colored(random_drawing), hashed_path + "new random.png")
            print("Compressed images save")
        except Exception:
            self.assertTrue(False)

    def test_encoding(self):
        get_image_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
        hashed_path = os.path.dirname(os.path.realpath(__file__)) + "/hashed_images/"

        random_drawing = compress(Image.open(get_image_path + "Untitled.png"))
        parrot_image = compress(Image.open(os.path.abspath(get_image_path + "photo_2018-12-10_22-28-40.jpg")))
        letter_ts = compress(Image.open(os.path.abspath(get_image_path + "Ц.png")))
        comic_con_photo = compress(Image.open(os.path.abspath(get_image_path + "kiev comic conS80922-141312.jpg")))

        try:
            self.assertIsInstance(build_hash(random_drawing), bytes)
            self.assertIsInstance(build_hash(parrot_image), bytes)
            self.assertIsInstance(build_hash(letter_ts), bytes)
            self.assertIsInstance(build_hash(comic_con_photo), bytes)
        except:
            raise AssertionError
