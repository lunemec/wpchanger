#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import time
import os
import signal
import sys

from lib.common import Common
from lib.environment import environment
from lib.image import Img

from handlers.events_handler import handle_events
from handlers.plugin_handler import Plugin
import settings


# commandline arguments parsing
parser = argparse.ArgumentParser(description='''A program that computes input information (daytime, season, hw temp),
                                 picks up a image folder according to that information, merges appropriate
                                 images, so that it looks to human eye like his/hers desktop wallpaper changes
                                 fluently as the sun passes (or seasons change).''')

parser.add_argument('-d', '--daemonize', action='store_true', default=False, help='daemonize the process')
parser.add_argument('-i', '--interval', action='store', default=False, help='change interval in minutes')
parser.add_argument('-s', '--step', action='store', default=False, help='step by minutes each interval')


class Main(object):

    def __init__(self, args, env):
        '''
        runs all other functions
        '''

        self.daemon = getattr(args, 'daemonize', False)
        self.env = env

        if self.daemon:

            self.write_pidfile()

        self.common = Common(daemon=self.daemon)

        self.log = self.common.log
        self.log.debug('--- start ---')

        self.image = Img(self.common)
        self.plugin = Plugin(self.common, self.image, self.env)

        self.interval = float(getattr(args, 'interval', False) or (settings.change_interval)) * 60
        self.step = float(getattr(args, 'step', 0))
        self.step_increasing = self.step

        self.infinite_loop()

    def write_pidfile(self):
        '''
        gets pid and saves it into file for easier process management
        '''

        pid = str(os.getpid())
        pidfile = settings.pidfile

        with open(pidfile, 'w') as f:

            f.write(pid)

    def infinite_loop(self):
        '''
        runs infinite loop where it calls other functions
        '''

        while True:

            self.log.debug('handling events')

            # get results from events
            to_merge = handle_events(self.log, self.image, step=self.step_increasing)

            image_instances = []
            # merge individual event filters
            for single_merge in to_merge:

                img1 = self.image.open_image(single_merge[0])
                img2 = self.image.open_image(single_merge[1])
                alpha = single_merge[2]
                image_instances.append(self.image.merge_images(img1, img2, alpha))

            # TODO this is for seasons - try if it even works with 0.5 alpha
            # merge those results
            for i in range(len(image_instances) - 1):

                took = image_instances.pop()
                image_instances[-1] = self.image.merge_images(took, image_instances[-1], 0.5)

            self.log.debug('handling plugins')

            # set wallpaper image to image_instances[-1]
            self.plugin.handle_plugins(image_instances[-1])

            # tick each settings.change_interval minutes to change wallpaper
            time.sleep(self.interval)

            self.step_increasing += self.step
            self.log.debug('increasing step to %s' % self.step_increasing)

            self.log.debug('sleeping ... Zzz')


def exit_cleanly(signal, frame):

    sys.exit(0)


if __name__ == '__main__':

    args = parser.parse_args()

    # catch keyboard interrupt and exit gracefully
    signal.signal(signal.SIGINT, exit_cleanly)

    env = getattr(settings, 'window_manager_override', False) or environment()

    if env != 'windows':

        if args.daemonize:

            if os.fork() == 0:

                Main(args, env)

        else:

            Main(args, env)

    else:

        Main(args, env)
