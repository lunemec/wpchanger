# -*- coding: utf-8 -*-

import Image

from lib.common import log


def merge_images(image1, image2, alpha):
    ''' provided 2 Image.Image objects and alpha (0-1) merges images and return Image.Image object
    @param image1: Image.Image object
    @param image2: Image.Image object
    @param alpha: float
    @return Image.Image object or False on error '''

    try:

        output_img = Image.blend(image1, image2, alpha)
        return output_img

    except Exception, e:
        log.error('Error while merging images with alpha %s, error was: %r' % (alpha, e))
        return False
