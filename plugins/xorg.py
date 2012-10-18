# -*- coding: utf-8 -*-

import os
from subprocess import call

from lib.common import BaseClass

class xorg(BaseClass):
    image_alpha = True
    
    def set_wallpaper(self, image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
                
        call(['feh', '--bg-fill', '%s/%s' % (filepath, imgfile)])
        
        return True