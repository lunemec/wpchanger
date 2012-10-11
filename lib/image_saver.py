# -*- coding: utf-8 -*-

import Image
import os

from common import BaseClass
from environment_detector import Environment

class SaveImage(BaseClass):
        
    def save(self, image_object, image_file, img_format='PNG'):
        ''' tries to save image object as file
        @param image_object: Image.Image object
        @param image_file: string
        @return boolean
        
        image_file can be absolute or relative path
        
        usage: save(image_object, '/where/to/save/image/img') 
        returns True or False on error'''
        path = os.path.abspath(image_file)
        
        try:
            image_object.save(path, format=img_format)
            return True
        except Exception, e:
            self.log.error('%s Error while saving image file: %s, error was: %r' % (self.datetime.datetime.now(), path, e))
            return False