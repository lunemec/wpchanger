# -*- coding: utf-8 -*-

# absolute or relative path to resulting wallpaper image
wallpaper_image = '/root/Documents/wpchanger/wp.png'

# absolute or relative path to images folder (absolute path is better)
images_dir = 'images'

# interval for image refresh in minutes
change_interval = 5

# valid image types
image_types = ['jpg', 'png', 'bmp']

# override window manager settings with (uncomment to enable)
#window_manager_override = 'kde'

# don't change this unless you know what you're doing
# dict with window managers we can detect format is following: 'window_manager': ['string1_to_look_for', 'string2_to_look_for']
window_managers = {'gnome': ['gnome'],
                   'kde': ['kdeinit']}

# name of temporary image to save (without .bmp/.png)
tmp_image = 'tmp/tempimage'

# select on which events will resulting wallpaper depend
events = ['daytime']

# pid file
pidfile = 'wpchanger.pid'
