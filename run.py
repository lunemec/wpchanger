#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os

from lib.common import log
from lib.environment_detector import environment
from lib.image_merge import merge_images
from lib.image_opener import open_image

from handlers.events_handler import handle_events
from handlers.plugin_handler import handle_plugins

import settings


def write_pidfile():
    '''
    gets pid and saves it into file for easier process management
    '''

    pid = str(os.getpid())
    pidfile = settings.pidfile

    with open(pidfile, 'w') as f:
        f.write(pid)


def main():
    # TODO add command line options

    log.debug('--- start ---')

    write_pidfile()

    while True:

        log.debug('handling events')

        # get results from events
        to_merge = handle_events()

        image_instances = []
        # merge individual event filters
        for single_merge in to_merge:

            img1 = open_image(single_merge[0])
            img2 = open_image(single_merge[1])
            alpha = single_merge[2]
            image_instances.append(merge_images(img1, img2, alpha))

        # TODO this is for seasons - try if it even works with 0.5 alpha
        # merge those results
        for i in range(len(image_instances) - 1):

            took = image_instances.pop()
            image_instances[-1] = merge_images(took, image_instances[-1], 0.5)

        log.debug('handling plugins')

        # set wallpaper image to image_instances[-1]
        handle_plugins(image_instances[-1])

        # tick each settings.change_interval minutes to change wallpaper
        time.sleep(settings.change_interval * 60)

        log.debug('sleeping ... Zzz')


if __name__ == '__main__':

# TODO make windows part of this launcher
    if environment() != 'windows':
        if os.fork() == 0:
            main()
