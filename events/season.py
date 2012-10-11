# -*- coding: utf-8 -*-

import os

from lib.common import BaseClass
import settings

class season(BaseClass):
    
    provides = 'folder'
    params = {'images_folder': 'settings.images_dir',
              'date': 'datetime.date.today()'}
    autoimport = {'settings': 'settings', 
                  'datetime': 'datetime'}
            
    def event(self, images_folder, date, reverse=False):
        ''' returns folder corresponding to current season
        @param images_folder: unicode string
        @param date: datetime.date object
        @param reverse: boolean
        @return unicode string '''
        
        folders_list = []
        abs_path = os.path.abspath(images_folder)
        
        directory_list = os.listdir(abs_path)
        
        for item in directory_list:
            item = os.path.join(abs_path, item)
            if os.path.isdir(item):
                folders_list.append(item)
        
        # get current date and season
        season = self.current_season(date)
        
        if not reverse:
            for folder in folders_list:
                if season in folder:
                    return folder

        # reverse binding            
        else:
            seasons = {'spring': 'autumn', 'summer': 'winter', 'winter': 'summer', 'autumn': 'spring'}
            
            for folder in folders_list:
                if seasons[season] in folder:
                    return folder
        
        return False
        
    def current_season(self, today):
        ''' returns current season or False
        @param today: datetime.date object 
        @return string'''
        
        # seasons in format (MM, DD) (start, end) WITHOUT LEADING ZERO!
        seasons = {'spring': ((3, 2), (5, 31)), 
                   'summer': ((6, 1), (9, 22)), 
                   'autumn': ((9, 23), (12, 21)), 
                   'winter': ((12, 22), (12, 31)),
                   'winter2': ((1, 1), (3, 1))}
                
        for i in seasons:
            this_year = today.year
            
            if self.datetime.date(this_year, seasons[i][0][0], seasons[i][0][1]) <= today <= self.datetime.date(this_year, seasons[i][1][0], seasons[i][1][1]):
                self.log.debug('%s %s <= %s <= %s' % (self.datetime.datetime.now(), self.datetime.date(this_year, seasons[i][0][0], seasons[i][0][1]), today, self.datetime.date(this_year, seasons[i][1][0], seasons[i][1][1])))
                
                if i == 'winter2':
                    return 'winter'                
                return i
                            
        return False