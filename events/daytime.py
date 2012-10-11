# -*- coding: utf-8 -*-

from lib.common import BaseClass
import settings

class daytime(BaseClass):
    
    provides = 'image'
    params = {'imgs_list': 'image_finder.ImagePaths().get_paths(self.curr_directory)',
              'time': 'datetime.datetime.now()'}
    autoimport = {'os': 'os', 
                  'datetime': 'datetime', 
                  'image_finder': 'lib.image_finder'}
            
    def event(self, imgs_list, time):
        ''' calculates which 2 images to merge and with what alpha provided images list and time
        @param imgs_list: list unicode strings
        @param time: datetime.datetime object
        @return (string, string, float) or False on error'''
        
        try:
            # get current local time in minutes
            lctime = time.hour * 60 + time.minute
            
            # find out how many % of day it is now and where start counting
            per_cent_day = (100 / 1440.0)*lctime
            
            # get wallpaper change interval from settings
            timer = settings.change_interval
            loops = 1440 / timer
    
            # log for debug
            self.log.debug('%s STEP | lctime = %s | timer = %s | per_cent_day = %s' % 
                      (time,
                       lctime,
                       timer,
                       per_cent_day,))
            
            # calculate which 2 images need merge with what alpha, merge them, save, and set it.
            steps = (len(imgs_list) - 1) * 100
            curr_step = int(steps * per_cent_day/100)
            
            image1 = curr_step / 100
            image2 = (curr_step / 100) + 1
            
            alpha = curr_step/100.0 - image1
            
            img1 = int(image1) - 1
            img2 = int(image2) - 1
            
            self.log.debug('%s IMAGES calculated and set | steps = %s | curr_step = %s | image1 = %s | image2 = %s | alpha = %s | img1 = %s | img2 = %s' % 
                      (time,
                       steps,
                       curr_step,
                       image1,
                       image2,
                       alpha,
                       img1,
                       img2,))
            
            return (imgs_list[img1], imgs_list[img2], alpha)
        
        except Exception, e:
            self.log.error('%s Error while calculating images and alpha, imgs_list: %s, time: %s, error: %r' % (self.datetime.datetime.now(), imgs_list, time, e))
            return False