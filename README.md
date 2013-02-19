Description
-------------------------------

This application is multi-platform wallpaper changer. It can change your wallpaper depending on daytime, date, (weather, cpu-temp not implemented yet).

I hope it will have gui in future, for now it works from command line only.

Main trouble is discovering how to change wallpaper on certain system or window manager, so I made it simple if someone knows how to change it,
just write a super simple plugin, that can do that, so everyone can enjoy it :)

You can use it to generate fractals or something like that using python imaging library and then use this application to set it as wallpaper, with
some conditions, there are no limits to ones imagination.


INSTALATION
--------------------------------
    Note for windows users: install 32bit version of Python, for it is difficult to get 64bit version of PIL(Python imaging library)
    
    
    1) install dependencies:
        # pip install -r REQUIREMENTS

    2) configure settings to correct paths 
        just set wallpaper_image variable in settings to correct path should be enough

    3) OPTIONAL
        find some nice wallpapers that can be used with this program 
            (only if you don't like these few that come with this program)
        set images_dir to path where these wallpapers are located in

    4) run run.py
        # ./run.py


    On some systems (window managers) you need to manually point your system to the resulting wallpaper, because there is no API 
    (I could find) for doing it programmatically (like KDE).

    That means path you set up earlier (wallpaper_image) is where the result will be saved, so point your os to it.

    Other window managers - like i3wm or gnome provide API that will do it for you, 
    you don't need to take care of anything except settings.

    --- Plugins ---
    name pluigns so they would correspond to settings.window_managers key and environment_detector ('gnome.py', 'kde.py', 'windows.py', 'macos.py')

    each plugin function set_wallpaper that takes wallpaper image file with absolute or relative path and sets it as a desktop.
    method needs to return True if success or False on error.
    image_alpha attribute describes if windowmanager can process PNG files, if not set it defaults to False, that means program will save wallpaper as BMP


Image Selection
-------------------------------------
    Folder containing images should have images that represent time of day passing - by leaves falling, sun setting, nightsky showing etc...

    Folder names should be numbers .jpg/png so it will correspond to this:

    HOURS --- 00 --- 01 --- 02 --- 03 --- 04 --- 05 --- 06 --- 07 --- 08 --- 09 --- 10 --- 11 --- 12 --- 13 --- 14 --- 15 --- 16 --- 17 --- 18 --- 19 --- 20 --- 21 --- 22 --- 23 ---
    IMAGES      0.jpg           02.jpg            03.jpg           04.jpg          05.jpg           06.jpg          07.jpg          08.jpg            09.jpg          10.jpg

    You can have more images than this of course, but note that wpchanger changes images each 5 mins, so there would be no sense in having more than 24*60*5 images
    At the end of the day, images 10 and 00 will be merged and loop starts again the other day


Command line options
-----------------------------------
I've added some command line options that should help you use this program:

    -h  --help          Displays help
    -d  --daemonize     runs program in daemon mode, using wpchanger.log as log and wpchanger.pid as file for PID
    -i  --interval      change interval for new image generation and change (default is 5 minutes)
    -s  --step          change step in minutes to do each interval - this way you can see the image change faster - entire day in 5 minutes for example.


Plugins
------------------------------------
Plugins set wallpaper for specific window managers, some wm's don't support alpha (PNG with alpha - RGBA) images. In that case set image_alpha to False and image will get saved as RGB.

function set_wallpaper must take one argument: image file with absolute path '/home/myhome/somewhere/image.bmp' and should set window manager to that wallpaper.

Some window managers do not provide methods for changing wallpapers, so you should option 'window_manager_override' in settings.py and set it to 'kde'.
This way, program calculates and creates the correct image, and saves it to path 'wallpaper_image' so just point your window manager to that image and it will reload the image (hopefully) by itself.

If you know of method how to change the wallpaper programatically, just create your own plugin, or leave a comment/message and I'll try to create it.


Example:
-------------------------------------
'mywindowmanager.py'

    # -*- coding: utf-8 -*-

    import os

    from common import BaseClass

    image_alpha = False

    def set_wallpaper(image_file_with_path):
        filepath = os.path.abspath(image_file_with_path)
        
        try:
            # try to set wallpaper
            # NOTE: this will work, but there is no way of telling if wallpaper was set or not, and also Exception below would occur only if imgfile would
            # be something horrible, so almost never
            call(['feh', '--bg-fill', imgfile])
            return True
        
        except Exception, e:
            self.log.error('%s Error while setting wallpaper image: %s, error was: %s' % (self.datetime.datetime.now(), image_file_with_path, e))
            return False


Events
------------------------------------------
name events so they would correspond to settings.events
at each time at least one event provinding 'image' must be active!

event must have provides attribute (str) that specifies what this event does 'folder' or 'image'

only one 'folder' event may be active at the same time
event must have event function that takes **kwargs with data it needs to do what it does
**kwargs is passed from lib/event_handler.py from get_event_result where are kwargs set

event that has provides set to 'folder' must return unicode string with absolute path to images folder
event that has provides set to 'image' must return (u'/abs/path/to/image1', u'/abs/path/to/image2', alpha), alpha is float

you may have active more than one event that provide 'image', the program will merge them separately and then together

Example:
-----------------------------------------
'myevent.py'

    # -*- coding: utf-8 -*-

    import os

    from lib.common import BaseClass
    import settings

        
    provides = 'folder'
            
    def event(self, **kwargs):
        
        folder = 'kwargs.get('param1')/kwargs.get('param2')'

        return folder.decode('utf-8')
