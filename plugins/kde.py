# -*- coding: utf-8 -*-

import os
from subprocess import call

from common import BaseClass

class kde(BaseClass):
    image_alpha = True
    
    def set_wallpaper(image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
        
        # kde3
        # *dcop kdesktop KBackgroundIface setWallpaper /home/crouse/Wallpapers/skull.jpg 5
        
        # kde4
        # unknown, some crazy dbus call which is not available nowhere on the internet
        # I'm starting to hate KDE4 ... 
        
        # TODO fill code here
        
        return True