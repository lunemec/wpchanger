# -*- coding: utf-8 -*-

from importlib import import_module
import os

from common import BaseClass
import settings

class Event(BaseClass):
    
    def handle_events(self):
        ''' loads active events from settings, activates them and result is used for image merging
        @return [(img1, img2, alpha), (img1, img2, alpha)] '''
        # first get active events
        self.events = settings.events[:]
        self.curr_directory = settings.images_dir[:]
                
        # import those    
        for event in self.events:
            setattr(self, event, import_module('events.%s' % event))
            
        # get their provide, only once can be 'folder'
        folder_count = 0
        have_first = False
        for loaded_ev in self.events:
            if eval('self.%s.%s.provides' % (loaded_ev, loaded_ev)) == 'folder':
                # set it so 'folder' providing event goes fist
                have_first = True
                self.goes_first = loaded_ev
                folder_count += 1
        
        if folder_count > 1:
            self.log.error('%s Error while event loading, more than one event provides folder' % self.datetime.datetime.now())
            raise Exception('Active events can have only one that provides "folder", check settings.')
        
        # service goes_first, first is always 'folder'
        if have_first and self.goes_first:
            self.curr_directory = self.__get_event_result(self.goes_first)
        
            # remove so it is not loaded again
            self.events.remove(self.goes_first)
        
        to_return = []
        # call other events
        for c_event in self.events:
            to_return.append(self.__get_event_result(c_event))
            
        return to_return
        
        
    def __get_event_result(self, event):    
        ''' calls specified event and returns its result
        @param event: string
        @return event result '''    
        # autoimport from event
        to_import = eval('self.%s.%s().autoimport' % (event, event))
        for importme in to_import:
            globals()[importme] = import_module(to_import[importme])
        
        # get params and prepare them as funcion call parameters
        params = eval('self.%s.%s.params' % (event, event))
        
        tmp_list = []
        for param in params:
            tmp_list.append('%s=%s' % (param, params[param]))
            
        call_params = ', '.join(tmp_list)
        
        # call the method
        result = eval('self.%s.%s().event(%s)' % (event, event, call_params))
        
        return result