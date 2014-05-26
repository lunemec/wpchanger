# -*- coding: utf-8 -*-

from importlib import import_module

import os
import sys

import settings


class Plugin(object):

    def __init__(self, common, img, env):

        self.log = common.log
        self.image = img
        self.env = env

    def save_image(self, converted_image, alpha_capable):

        if alpha_capable:
            image_format = 'PNG'
        else:
            image_format = 'BMP'

        save_to = os.path.abspath('%s.%s' % (settings.tmp_image, image_format.lower()))
        self.image.save(converted_image, save_to, image_format)

        return save_to

    def handle_plugins(self, image):
        ''' method that chooses plugin to use depending on environment, saves image and sets it as wallpaper
        @param image: Image.Image instance '''

        self.log.debug('handle_plugins start, params: %s' % (image))

        # load corresponding plugin
        active_plugin = import_module('plugins.%s' % self.env)

        # determine alpha capability
        alpha_capable = getattr(active_plugin, 'image_alpha', False)
        converted_image = self.image.convert_image(image, alpha=alpha_capable)

        save_to = self.save_image(converted_image, alpha_capable)
        print save_to
        # set image as wallpaper using plugin
        setimage = active_plugin.set_wallpaper(save_to)

        if setimage:
            # success
            self.log.debug('successfully set wallpaper from %s' % (save_to))

        else:
            # fail
            self.log.error('error while setting wallpaper from %s' % (save_to))
            print 'cannot set wallpaper, check log for details. Exiting'
            sys.exit(1)
