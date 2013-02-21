# -*- coding: utf-8 -*-

import os
from subprocess import call


image_alpha = True


def set_wallpaper(image_file_with_path):

    filepath = os.path.abspath(image_file_with_path)

    # works on Gnome3
    call(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', 'file://%s' % (filepath)])

    return True
