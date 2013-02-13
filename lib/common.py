# -*- coding: utf-8 -*-

import logging


logging.basicConfig(filename='wpchanger.log', format='[%(levelname)s] %(asctime)s %(module)s.py %(funcName)s():%(lineno)d %(message)s', level=logging.DEBUG)

#logging.basicConfig(format='[%(levelname)s] %(asctime)s %(module)s.py %(funcName)s():%(lineno)d %(message)s', level=logging.DEBUG)

log = logging
