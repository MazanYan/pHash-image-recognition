import os
from __main__ import *

def test():
    random_drawing = compress(Image.open(os.path.abspath("Untitled.png")))
    parrot_image = compress(Image.open(os.path.abspath("photo_2018-12-10_22-28-40.jpg")))
    letter_ts = compress(Image.open(os.path.abspath("Ц.png")))
    comic_con_photo = compress(Image.open(os.path.abspath("kiev comic conS80922-141312.jpg")))

    save_compressed(two_colored(random_drawing), "new random.png")
    save_compressed(two_colored(parrot_image), "new parrot.png")
    save_compressed(two_colored(letter_ts), "new letter.png")
    save_compressed(two_colored(comic_con_photo), "new comic con photo.png")
