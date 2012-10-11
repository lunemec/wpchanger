# -*- coding: utf-8 -*-

import Image

from environment_detector import Environment
from common import BaseClass

class WallpaperImage(BaseClass):
        
    def convert_image(self, img, alpha=True):
        ''' converts image from RGB to RGBA or RGB to RGB
        @param img: Image.Image object
        @param alpha: boolean (default=True)
        @return Image.Image object or False on error '''
        if img.mode == 'RGB':
            # image doesn't have alpha
            return img
        else:
            try:
                if alpha:
                    # not changing, img = img
                    r, g, b, a = img.split()
                    img = Image.merge('RGBA', (r,g,b,a))
                else:
                    r, g, b, a = img.split()
                    img = Image.merge('RGB', (r,g,b))
                    
                return img
            
            except Exception, e:
                self.log.debug('%s Not converting from RGBA to RGB, error: %s' % (self.datetime.datetime.now(), e))
                return False