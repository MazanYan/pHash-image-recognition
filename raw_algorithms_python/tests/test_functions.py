from main import *
import os


def test():
    get_image_path = os.path.dirname(os.path.realpath(__file__)) + "/images/"
    hashed_path =  os.path.dirname(os.path.realpath(__file__)) + "/hashed_images/"

    random_drawing = compress(Image.open(get_image_path + "Untitled.png"))
    parrot_image = compress(Image.open(os.path.abspath(get_image_path + "photo_2018-12-10_22-28-40.jpg")))
    letter_ts = compress(Image.open(os.path.abspath(get_image_path + "Ц.png")))
    comic_con_photo = compress(Image.open(os.path.abspath(get_image_path + "kiev comic conS80922-141312.jpg")))

    save_compressed(two_colored(random_drawing), hashed_path + "new random.png")
    save_compressed(two_colored(parrot_image), hashed_path + "new parrot.png")
    save_compressed(two_colored(letter_ts), hashed_path + "new letter.png")
    save_compressed(two_colored(comic_con_photo),hashed_path + "new comic con photo.png")
