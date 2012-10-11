# -*- coding: utf-8 -*-

import time

from lib.common import BaseClass
from lib.events_handler import Event
from lib.image_finder import ImagePaths
from lib.image_merge import MergedImage
from lib.image_opener import OpenImage
from lib.image_saver import SaveImage
from lib.plugin_handler import Plugin
import settings

def main():
    
    while True:
        
        # TODO call the methods from lib
        
        # tick each settings.change_interval minutes to change wallpaper
        time.sleep(settings.change_interval * 60)
        pass
    
    return True

if __name__ == '__main__':
    
    main()