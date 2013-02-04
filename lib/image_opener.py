# -*- coding: utf-8 -*-

import Image
import os

from lib.common import log


def open_image(image_file):
    ''' opens image and returns Image.Image object or None on error
    @param image_file: string
    @return Image.Image object or None on error

    image_file can be absolute or relative path

    usage: open_image('path/to/image/imgfile.jpg')
    returns Image.Image object or False on error '''

    path = os.path.abspath(image_file)

    try:
        image = Image.open(path)
        return image

    except Exception, e:
        log.error('Error while opening file %s, error was: %r' % (image_file, e))
        return False
