from HashBuilder import *
import os
import unittest


class Test(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.get_image_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
        self.hashed_path = os.path.dirname(os.path.realpath(__file__)) + "/hashed_images/"
        self.test_class = HashBuilder(self.get_image_path)

    def test_compressing(self):
        try:
            self.test_class.__compress__(Image.open(self.get_image_path + "Untitled.png"))
            self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "photo_2018-12-10_22-28-40.jpg")))
            self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "Ц.png")))
            self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "kiev comic conS80922-141312.jpg")))
            print("Images compress")
        except:
            self.assertTrue(False)

    def test_saving(self):
        random_drawing = self.test_class.__compress__(Image.open(self.get_image_path + "Untitled.png"))
        parrot_image = self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "photo_2018-12-10_22-28-40.jpg")))
        new_parrot_image = self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "edited photo_2018-12-10_22-28-40.jpg")))
        letter_ts = self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "Ц.png")))
        comic_con_photo = self.test_class.__compress__(Image.open(os.path.abspath(self.get_image_path + "kiev comic conS80922-141312.jpg")))

        try:
            self.test_class.__save_compressed__(self.test_class.__two_colored__(random_drawing), self.hashed_path + "new random.png")
            self.test_class.__save_compressed__(self.test_class.__two_colored__(parrot_image), self.hashed_path + "new parrot.png")
            self.test_class.__save_compressed__(self.test_class.__two_colored__(new_parrot_image), self.hashed_path + "new edited parrot.png")
            self.test_class.__save_compressed__(self.test_class.__two_colored__(letter_ts), self.hashed_path + "new letter.png")
            self.test_class.__save_compressed__(self.test_class.__two_colored__(comic_con_photo), self.hashed_path + "new comic con photo.png")
            print("Compressed images save")
        except Exception:
            self.assertTrue(False)

    def test_hashing(self):
        random_drawing = "Untitled.png"
        parrot_image = "photo_2018-12-10_22-28-40.jpg"
        new_parrot_image = "edited photo_2018-12-10_22-28-40.jpg"
        letter_ts = "Ц.png"
        comic_con_photo = "kiev comic conS80922-141312.jpg"

        try:
            self.assertIsInstance(self.test_class.hash_image(random_drawing)[1], bytes)
            self.assertIsInstance(self.test_class.hash_image(parrot_image)[1], bytes)
            self.assertIsInstance(self.test_class.hash_image(letter_ts)[1], bytes)
            self.assertIsInstance(self.test_class.hash_image(comic_con_photo)[1], bytes)
            self.assertIsInstance(self.test_class.hash_image(new_parrot_image)[1], bytes)
            print("Images get hashed")
        except:
            raise AssertionError
