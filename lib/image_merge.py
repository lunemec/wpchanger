# -*- coding: utf-8 -*-

import Image

from common import BaseClass

class MergedImage(BaseClass):
        
    def merge_images(self, image1, image2, alpha):
        ''' provided 2 Image.Image objects and alpha (0-1) merges images and return Image.Image object
        @param image1: Image.Image object
        @param image2: Image.Image object
        @param alpha: float
        @return Image.Image object or False on error '''

        try:
            output_img = Image.blend(image1, image2, alpha)
            return output_img
        except Exception, e:
            self.log.error('%s Error while merging images with alpha %s, error was: %r' % (self.datetime.datetime.now(), alpha, e))
            return False