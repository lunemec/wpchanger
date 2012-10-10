# -*- coding: utf-8 -*-

import os

from common import BaseClass
import settings

class season(BaseClass):

    def __init__(self, images_folder, current_date, reverse=False):
        super(SelectImages, self).__init__()
        self.selected = self.select_folder(images_folder, current_date, reverse)
        self.provides = 'folder'
        
    def select_folder(self, images_folder, date, reverse):
        
        folders_list = []
        
        directory_list = os.listdir(os.path.abspath(images_folder))
        
        for item in directory_list:
            if os.path.isdir(item):
                folders_list.append(item)
        
        # seasons in format MM-DD (start, end)
        seasons = {'spring': ('03-02', '05-31'),
                   'summer': ('06-01', '09-22'),
                   'autumn': ('09-23', '12-21'),
                   'winter': ('12-22', '03-01')}
        
        pass
        