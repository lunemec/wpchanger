# -*- coding: utf-8 -*-

import os
from subprocess import call

from lib.common import BaseClass

class gnome(BaseClass):
    image_alpha = True
    
    def set_wallpaper(self, image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
        
        # TODO figure out how to test if wallpaper was set
        call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 'file://%s/%s' % (filepath, imgfile),])
        
        return True