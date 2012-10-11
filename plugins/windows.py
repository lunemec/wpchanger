# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    from ctypes import windll

from lib.common import BaseClass

class windows(BaseClass):
    image_alpha = False
    
    def set_wallpaper(self, image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
        
        SPI_SETDESKWALLPAPER = 20
        setit = windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filepath, 0)
        
        if setit:
            return True
        
        else:
            self.log.error('%s Error while setting wallpaper image: %s, error was: %s' % (self.datetime.datetime.now(), image_file_with_path, e))
            return False
            
    