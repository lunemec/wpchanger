# -*- coding: utf-8 -*-

from importlib import import_module
import os

from lib.common import BaseClass
from lib.environment_detector import Environment
from lib.image_convertor import WallpaperImage
from lib.image_saver import SaveImage
import settings

class Plugin(BaseClass):
    
    def handle_plugins(self, image):
        ''' method that chooses plugin to use depending on environment, saves image and sets it as wallpaper
        @param image: Image.Image instance '''

        # detect our environment, either from override or env.detector
        self.env = getattr(settings, 'window_manager_override') or Environment().environment()
        
        # load corresponding plugin
        active_plugin = import_module('plugins.%s' % self.env)
        
        # determine alpha capability
        alpha_capable = eval('active_plugin.%s.image_alpha' % self.env)
        
        # convert image
        converted_image = WallpaperImage().convert_image(image, alpha_capable)
        
        # save to settings location
        if alpha_capable:
            format = 'PNG'
        else:
            format = 'BMP'
            
        save_to = os.path.abspath('%s.%s' % (settings.tmp_image, format.lower()))
        SaveImage().save(converted_image, save_to, format)
        
        # set image as wallpaper using plugin
        setimage = eval('active_plugin.%s().set_wallpaper("%s")' % (self.env, save_to))
        
        if setimage:
            # success
            self.log.debug('%s successfully set wallpaper from %s' % (self.datetime.datetime.now(), save_to))
            
        else:
            # fail
            self.log.error('%s error while setting wallpaper from %s' % (self.datetime.datetime.now(), save_to))
        
