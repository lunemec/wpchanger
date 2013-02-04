# -*- coding: utf-8 -*-

import os
from subprocess import call


image_alpha = True

def set_wallpaper(image_file_with_path):
    filepath = os.path.abspath(image_file_with_path)

    # TODO fill code here, make it use mac python binding
    #tell application "Finder"set desktop picture to {"Your HD:Users:YourUserName:desktops:" & situation & ".jpg"} as alias
    #end tell
    return True
