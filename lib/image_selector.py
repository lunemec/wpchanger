# -*- coding: utf-8 -*-

from common import BaseClass
import settings

class SelectImages(BaseClass):
    ''' provided images list, current time returns 2 images from list and alpha for merging 
    @param images_list: list unicode strings
    @param current_time: datetime.datetime object
    
    usage: SelectImages(['img1', 'img2'], datetime.datetime(2012, 10, 9, 15, 40, 9, 279565)).selected
    returns ('img1', 'img2', 0.5) or False on error'''
    
    def __init__(self, images_list, current_time):
        super(SelectImages, self).__init__()
        self.selected = self.select_images(images_list, current_time)
        
    def select_images(self, imgs_list, time):
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