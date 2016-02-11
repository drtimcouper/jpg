from PIL import Image

def are_images_equal_for_pixels(one, other, pixels):
    for pixel in pixels:
        if one.get_rgb(pixel) != other.get_rgb(pixel):
            return False
    else:
        return True


class NoImageLoadedError(Exception):
    pass


class MyImage:
    _image = None
    _rgb_im = None

    @property
    def rgb_im(self):
        if self._rgb_im is None:
            if self.image is None:
                raise NoImageLoadedError
            self._rgb_im = self.image.convert('RGB')
        return self._rgb_im

    @property
    def image(self):
        return self._image

    @ image.setter
    def image(self, value):
        self._image = value
       # unset what was in _rgb_im
        self._rgb_im = None


    def load_from_file(self, fp):
        self.image = Image.open(fp)

    def get_rgb(self, apoint):
        return self.rgb_im.getpixel(apoint)


