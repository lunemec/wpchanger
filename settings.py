# -*- coding: utf-8 -*-
# should contain which program to call to change wallpaper in your environment

logfile = 'wpchanger.log'

# absolute or relative path to images folder
images_dir = '../../images/stars'

# interval for image refresh in minutes
change_interval = 5

# valid image types
image_types = ['.jpg', '.png', '.bmp']

# dict with window managers we can detect format is following: 'window_manager': ['string1_to_look_for', 'string2_to_look_for']
window_managers = {'gnome': ['gnome'],
                   'kde': ['kdeinit']}

# name of temporary image to save (without .bmp/.png)
tmp_image = 'tmp/tempimage'

# select on which events will resulting wallpaper depend
events = ['daytime']
