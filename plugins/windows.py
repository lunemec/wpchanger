# -*- coding: utf-8 -*-

import os

if os.name == 'nt':
    from ctypes import windll
else:
    raise Exception('Unsupported OS.')


image_alpha = False


def set_wallpaper(image_file_with_path):

    filepath = os.path.abspath(image_file_with_path)

    SPI_SETDESKWALLPAPER = 20
    setit = windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, filepath, 0)

    if setit:
        return True

    else:
        return False
