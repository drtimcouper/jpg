from PIL import Image

def are_images_equal(one, other, pixels):
    for pixel in pixels:
        if one.get_rgb(pixel) != other.get_rgb(pixel):
            return False
    else:
        return True

class MyImage:

    def __init__(self, fp):
        self.im = Image.open(fp)
        self.rgb_im = self.im.convert('RGB')

    def get_rgb(self, apoint):
        return self.rgb_im.getpixel(apoint)


