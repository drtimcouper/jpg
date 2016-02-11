import os

from nose.tools import assert_true, assert_false

from jpg.myimage import MyImage, are_images_equal

this_dir =  os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(this_dir, 'data')
IMAGE_FILE = os.path.join(DATA_DIR, 'stirling.jpg')
IMAGE_FILE2 = os.path.join(DATA_DIR, 'stirling-picture.jpg')
PIXELS = [(1,1), (40,40)]


def test_load_from_file():
    im = MyImage()
    im.load_from_file(IMAGE_FILE)
    assert_true(im.image is not None)



def test_equal_same():
    im = MyImage()
    im.load_from_file(IMAGE_FILE)
    im2 = MyImage()
    im.load_from_file(IMAGE_FILE)
    assert_true(are_images_equal(im,im2, PIXELS))



def xtest_equal_different():
    im = MyImage()
    im.load_from_file(IMAGE_FILE)
    im2 = MyImage()
    im.load_from_file(IMAGE_FILE2)
    assert_false(are_images_equal(im,im2, PIXELS))

