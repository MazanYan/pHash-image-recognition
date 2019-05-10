from tests.test_functions import *


if __name__ == "__main__":
    test_class = Test()
    test_class.test_compressing()
    test_class.test_saving()
    test_class.test_hashing()
    test_class.test_hash_determinance()
    test_class.test_hash_similar()
    # fails on recognising letter and random drawing not similar
    test_class.test_hash_not_similar()
