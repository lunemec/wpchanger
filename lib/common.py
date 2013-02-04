# -*- coding: utf-8 -*-

import datetime
import logging 

import settings

class BaseClass(object):
    ''' provides access to common methods for all other classes '''
    
    def __init__(self):   
        logging.basicConfig(filename=settings.logfile, format='[%(levelname)s]%(message)s', level=logging.DEBUG)
        self.log = logging
        self.datetime = datetime

log = BaseClass().log
