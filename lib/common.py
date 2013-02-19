# -*- coding: utf-8 -*-

import logging
import inspect


class Common(object):

    def __init__(self, daemon=False):

        logfile = 'wpchanger.log'

        self.log = logging.getLogger('wpchanger')
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(module)s.py %(funcName)s():%(lineno)d %(message)s')

        if daemon:

            handler = logging.FileHandler(logfile)

        else:

            handler = logging.StreamHandler()

        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.log.setLevel(logging.DEBUG)
