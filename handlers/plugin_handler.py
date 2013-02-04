# -*- coding: utf-8 -*-

from importlib import import_module

import os
import sys

from lib.common import log
from lib.environment_detector import environment
from lib.image_convertor import convert_image
from lib.image_saver import save

import settings


def get_window_manager():

    return getattr(settings, 'window_manager_override', False) or environment()


def prepare_image(image, alpha_capable):

    converted_image = convert_image(image, alpha=alpha_capable)

    if not converted_image:
        log.error('cannot convert image, check if image is in correct dir, converted_image = %s' % (converted_image))
        print 'Image conversion error, check log for details. Exiting'
        sys.exit(1)

    return converted_image


def save_image(converted_image, alpha_capable):

    if alpha_capable:
        image_format = 'PNG'
    else:
        image_format = 'BMP'

    save_to = os.path.abspath('%s.%s' % (settings.tmp_image, image_format.lower()))
    save(converted_image, save_to, image_format)

    return save_to


def handle_plugins(image):
    ''' method that chooses plugin to use depending on environment, saves image and sets it as wallpaper
    @param image: Image.Image instance '''

    log.debug('handle_plugins start, params: %s' % (image))

    env = get_window_manager()

    # load corresponding plugin
    active_plugin = import_module('plugins.%s' % env)

    # determine alpha capability
    alpha_capable = getattr(active_plugin, 'image_alpha', False)
    converted_image = prepare_image(image, alpha_capable)

    save_to = save_image(converted_image, alpha_capable)

    # set image as wallpaper using plugin
    setimage = active_plugin.set_wallpaper(save_to)

    if setimage:
        # success
        log.debug('successfully set wallpaper from %s' % (save_to))

    else:
        # fail
        log.error('error while setting wallpaper from %s' % (save_to))
        print 'cannot set wallpaper, check log for details. Exiting'
        sys.exit(1)
