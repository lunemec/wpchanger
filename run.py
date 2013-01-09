# -*- coding: utf-8 -*-

import time
import os

from lib.common import BaseClass
from lib.environment_detector import Environment
from lib.events_handler import Event
from lib.image_finder import ImagePaths
from lib.image_merge import MergedImage
from lib.image_opener import OpenImage
from lib.image_saver import SaveImage
from lib.plugin_handler import Plugin
import settings

def main():
    # TODO add command line options
    
    while True:
        # get results from events
        to_merge = Event().handle_events()
        
        image_instances = []
        # merge individual event filters
        for single_merge in to_merge:
            img1 = OpenImage().open_image(single_merge[0])
            img2 = OpenImage().open_image(single_merge[1])
            alpha = single_merge[2]
            image_instances.append(MergedImage().merge_images(img1, img2, alpha))
            
        # merge those results 
        for i in range(len(image_instances)-1):
            took = image_instances.pop()
            image_instances[-1] = MergedImage().merge_images(took, image_instances[-1], 0.5)
            
        # set wallpaper image to image_instances[-1]
        Plugin().handle_plugins(image_instances[-1])
        
        # tick each settings.change_interval minutes to change wallpaper
        time.sleep(settings.change_interval * 60)


if __name__ == '__main__':
    
# TODO make windows part of this launcher
    if Environment().environment() != 'windows':  
        if os.fork() == 0:
            main()
