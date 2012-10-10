# -*- coding: utf-8 -*-

import time

import settings

def main():
    
    while True:
        
        # TODO call the methods from lib
        
        # tick each settings.change_interval minutes to change wallpaper
        time.sleep(settings.change_interval * 60)
        pass
    
    return True

if __name__ == '__main__':
    
    main()