# -*- coding: utf-8 -*-

import os
import settings

from common import BaseClass

class Environment(BaseClass):
    ''' detects system environment and returns env string
    usage: Environment().env
    returns: 'windows' or "gnome" or "kde" or "mac" '''
    
    def __init__(self):
        if os.name == 'nt':
            self.env = 'windows'
        elif os.name == 'posix':
            if os.uname[0] == 'Linux':
                self.env = self.detect_wm()
            elif os.uname[0] == 'Darwin':
                self.env = 'mac'
    
    def detect_wm(self):
        ''' tries to detect user's window manager on linux, if fail, reverts to using regular Xserver
        @return string 
        
        usage: detect_wm()
        returns "xorg" or "kde"'''
        ps = []
        
        # detect running processes
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

        for pid in pids:
            try:
                ps.append(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read().strip())
            except Exception:
                # since we don't mind that some processes might not be in list, do nothing on error
                pass
        
        # now compare running processes to known window managers
        prepared_dict = {}
        for wm_key in settings.window_managers:
            for wm_string in settings.window_managers[wm_key]:
                prepared_dict[wm_string] = wm_key
        
        for proc in ps:
            for key in prepared_dict:
                if key in proc:
                    return prepared_dict[key]
                    
        # all loops ended and no match, revert to Xserver
        return 'xorg'

        