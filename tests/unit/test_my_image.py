from nose.tools import (assert_raises, assert_true,
    assert_false, assert_equal)
from unittest.mock import Mock

from jpg.myimage import MyImage, NoImageLoadedError


def test_rgb_im_rgb_and_image_none():
    im = MyImage()
    with assert_raises(NoImageLoadedError):
        im.rgb_im


def test_rgb_im_None_and_image_not_none():
    im = MyImage()
    im.image = Mock()
    assert_true(im._rgb_im  is None)
    im.rgb_im
    assert_true(im._rgb_im  is not None)
    assert_true(im.image.convert.called)


def test_rgb_im_not_none_and_image_none():
    # this is the case where the image has been set previously
    # and has now been unset
    im = MyImage()
    im.image = Mock()
    im.rgb_im
    im.image=None
    with assert_raises(NoImageLoadedError):
        im.rgb_im


def test_rgb_im_not_none_and_image_not_none():
    # this is the case where the image has been set previously
    # and has now been unset
    im = MyImage()
    im.image = Mock()
    im.rgb_im
    assert_equal(im.image.convert.call_count, 1)
    im.rgb_im
    # call count hasn't changed
    assert_equal(im.image.convert.call_count, 1)
