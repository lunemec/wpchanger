# -*- coding: utf-8 -*-

import Image

from common import BaseClass

class MergedImage(BaseClass):
    ''' tries to merge 2 Image.Image objects together using alpha
    @param image_object_1: Image.Image object
    @param image_object_2: Image.Image object
    @param alpha: float
    
    usage: MergedImage(img1, img2, 0.5).image
    returns Image.Image object with 50% merging between images or False on error '''
    
    def __init__(self, image_object_1, image_object_2, alpha):
        super(MergedImage, self).__init__()
        self.image = self.merge_images(image_object_1, image_object_2, alpha)
        
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