# -*- coding: utf-8 -*-

import Image

import os
import re
import sys

import settings


class Img(object):

    def __init__(self, common):

        self.log = common.log
        self.filetypes = settings.image_types

    def get_paths(self, path):
        ''' method for returning sorted list of directory

        @param string: path to image folder
        @ return list'''

        return self.sort_images(self.get_images(path))

    def image_control(self, image):
        '''
        helper method for use with map()
        '''

        if image != 'tmp.bmp':

            if image.split('.')[1] in self.filetypes:

                return image

    def get_images(self, path):
        ''' returns list of unicode strings containing absolute paths to images

        @param path: unicode string (default=os.cwd())
        @return list unicode strings

        usage: get_images('path/to/images')
        returns [u'/path/to/img/img2.jpg', u'/path/to/img/img1.jpg']
        '''

        path = os.path.abspath(path)
        curr_dir = os.listdir(path)

        imgnames = map(self.image_control, curr_dir)

        result = ['%s/%s' % (path, i) for i in imgnames if i]

        return result

    def sort_images(self, input_list):
        ''' sorts retrieved list of images

        @param input_list: list unicode strings
        @return list unicode strings

        usage: sort_images([u'/path/to/img/img2.jpg', u'/path/to/img/img1.jpg'])
        returns [u'/path/to/img/img1.jpg', u'/path/to/img/img2.jpg']'''

        sort_dict = {}
        output_list = []
        num = re.compile(r'(\d+)')

        for img in input_list:
            sort_dict[int(num.search(img).groups()[0])] = img

        for i in sorted(sort_dict):
            output_list.append(sort_dict[i])

        return output_list

    def merge_images(self, image1, image2, alpha):
        ''' provided 2 Image.Image objects and alpha (0-1) merges images and return Image.Image object
        @param image1: Image.Image object
        @param image2: Image.Image object
        @param alpha: float
        @return Image.Image object or False on error '''

        try:

            output_img = Image.blend(image1, image2, alpha)
            return output_img

        except Exception as e:

            self.log.error('Error while merging images with alpha %s, error was: %r' % (alpha, e))
            self.log.exception('Exception on image merger')

            return False

    def open_image(self, image_file):
        ''' opens image and returns Image.Image object or None on error
        @param image_file: string
        @return Image.Image object or None on error

        image_file can be absolute or relative path

        usage: open_image('path/to/image/imgfile.jpg')
        returns Image.Image object or False on error '''

        path = os.path.abspath(image_file)

        try:

            image = Image.open(path)
            return image

        except Exception as e:

            self.log.error('Error while opening file %s, error was: %r' % (image_file, e))
            self.log.exception('Exception on image opener')

            return False

    def save(self, image_object, image_file, img_format='PNG'):
        ''' tries to save image object as file
        @param image_object: Image.Image object
        @param image_file: string
        @param img_format: string (default='PNG')
        @return boolean

        image_file can be absolute or relative path

        usage: save(image_object, '/where/to/save/image/img')
        returns True or False on error'''

        path = os.path.abspath(image_file)

        try:
            image_object.save(path, format=img_format)

            return True

        except Exception as e:

            self.log.error('Error while saving image file: %s, error was: %r' % (path, e))
            self.log.exception('Exception on image saver')

            return False

    def convert_image(self, img, alpha=True):
        ''' converts image from RGB to RGBA or RGB to RGB
        @param img: Image.Image object
        @param alpha: boolean (default=True)
        @return Image.Image object or False on error '''

        self.log.debug('Image convertor start, params: %s, alpha=%s' % (img, alpha))

        try:
            if img.mode == 'RGB':
                # image doesn't have alpha
                return img

            else:

                if alpha:
                    # not changing, img = img
                    r, g, b, a = img.split()
                    img = Image.merge('RGBA', (r, g, b, a))
                else:
                    r, g, b, a = img.split()
                    img = Image.merge('RGB', (r, g, b))

                return img

        except AttributeError as e:

            self.log.debug('Not converting from RGBA to RGB, error: %s' % (e))
            self.log.exception('Exception on image convertor')
            self.log.error('cannot convert image, check if image is in correct dir, converted_image = %s' % (img))

            print 'Image conversion error, check log for details. Exiting'

            sys.exit(1)
