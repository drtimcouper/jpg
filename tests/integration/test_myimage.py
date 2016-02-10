import os

from nose.tools import assert_true

from jpg.myimage import MyImage, are_images_equal

this_dir =  os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(this_dir, 'data')
IMAGE_FILE = os.path.join(DATA_DIR, 'stirling.jpg')
IMAGE_FILE2 = os.path.join(DATA_DIR, 'stirling-picture.jpg')
PIXELS = [(1,1), (40,40)]

def test_equal_ok():
    im = MyImage(IMAGE_FILE)
    im2 = MyImage(IMAGE_FILE)
    assert_true(are_images_equal(im,im2, PIXELS))

