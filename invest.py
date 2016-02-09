import os

from PIL import image

this_dir =  os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(this_dir, 'data')
IMAGE = os.path.join(DATA_DIR, 'stirling.jpg')

def main():
    im = image.open(IMAGE)
    image.show(im)


if __name__ == '__main__':
    main()
