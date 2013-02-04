# -*- coding: utf-8 -*-

import datetime

from lib.common import log
from lib.image_finder import get_paths

import settings


provides = 'image'


def event(**kwargs):
    ''' calculates which 2 images to merge and with what alpha provided images list and time
    @param imgs_list: list unicode strings
    @param time: datetime.datetime object
    @return (string, string, float) or False on error'''

    imgs_list = get_paths(kwargs['dir'])
    time = datetime.datetime.now()

    try:
        # get current local time in minutes
        lctime = time.hour * 60 + time.minute

        # find out how many % of day it is now and where start counting
        per_cent_day = (100 / 1440.0) * lctime

        # get wallpaper change interval from settings
        timer = settings.change_interval

        # log for debug
        log.debug('STEP | lctime = %s | timer = %s | per_cent_day = %s' % (lctime, timer, per_cent_day))

        # calculate which 2 images need merge with what alpha, merge them, save, and set it.
        steps = (len(imgs_list) - 1) * 100
        curr_step = int(steps * per_cent_day / 100)

        image1 = curr_step / 100
        image2 = (curr_step / 100) + 1

        alpha = curr_step / 100.0 - image1

        img1 = int(image1) - 1
        img2 = int(image2) - 1

        log.debug('IMAGES calculated and set | steps = %s | curr_step = %s | image1 = %s | image2 = %s | alpha = %s | img1 = %s | img2 = %s' %
                  (steps,
                   curr_step,
                   image1,
                   image2,
                   alpha,
                   img1,
                   img2,))

        return (imgs_list[img1], imgs_list[img2], alpha)

    except Exception, e:
        log.error('Error while calculating images and alpha, imgs_list: %s, time: %s, error: %r' % (imgs_list, time, e))
        return False
