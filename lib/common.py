# -*- coding: utf-8 -*-

import logging

import settings

logging.basicConfig(filename=settings.logfile, format='[%(levelname)s] %(asctime)s %(module)s.py %(funcName)s():%(lineno)d %(message)s', level=logging.DEBUG)
log = logging
