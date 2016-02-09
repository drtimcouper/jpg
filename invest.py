import os

from PIL import Image

this_dir =  os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(this_dir, 'data')
IMAGE = os.path.join(DATA_DIR, 'stirling.jpg')
IMAGE2 = os.path.join(DATA_DIR, 'stirling-picture.jpg')

def main():
     print(assert_images_equal(IMAGE, IMAGE, [(1,1), (40,40)]))
     print(assert_images_equal(IMAGE, IMAGE2, [(1,1), (40,40)]))


def basic():
    im = Image.open(IMAGE)

    rgb_im = im.convert('RGB')
    rgb = rgb_im.getpixel((1, 1))
    print(rgb)


class MyImage:

    def __init__(self, fp):
        self.im = Image.open(fp)
        self.rgb_im = self.im.convert('RGB')

    def get_rgb(self, apoint):
        return self.rgb_im.getpixel(apoint)


def assert_images_equal(fp1, fp2, pixels):
    im1 = MyImage(fp1)
    im2 = MyImage(fp2)
    for pixel in pixels:
        if im1.get_rgb(pixel) != im2.get_rgb(pixel):
            return False
    else:
        return True




if __name__ == '__main__':
    main()
