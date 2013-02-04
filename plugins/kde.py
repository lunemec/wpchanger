# -*- coding: utf-8 -*-

import os
import shutil
from subprocess import call

import settings

from lib.common import BaseClass

class kde(BaseClass):
    image_alpha = True
    
    def set_wallpaper(self, image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
        
        # kde3 - to try
        # *dcop kdesktop KBackgroundIface setWallpaper /home/crouse/Wallpapers/skull.jpg 5
        
        # kde4
        # yep, kde does not support command which would set up wallpaper, or I didn't find it
        # so, it is going to take the image and just move it over settings.wallpaper_image
        # it cannot be directly generated image because the saving procedure from PIL
        # saves it by parts I guess, and KDE sets it too soon and result is black screen
        # this is the only way I could find

        wallpaper = os.path.abspath(settings.wallpaper_image)

        shutil.copyfile(filepath, wallpaper)

        return True
