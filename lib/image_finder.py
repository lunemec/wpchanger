# -*- coding: utf-8 -*-

import os
import re
import settings

from common import BaseClass

class ImagePaths(BaseClass):
        
    def get_paths(self, path):
        ''' method for returning sorted list of directory 
        @param string: path to image folder
        @ return list'''
        self.paths = []
        self.paths = self.sort_images(self.get_images(path))
        return self.paths
    
    def get_images(self, path):
        ''' returns list o funicode strings containing absolute paths to images
        @param path: unicode string (default=os.cwd())
        @return list unicode strings
        
        usage: get_images('path/to/images')
        returns [u'/path/to/img/img2.jpg', u'/path/to/img/img1.jpg']
        '''
        filetypes = settings.image_types
        path = os.path.abspath(path)
        curr_dir = os.listdir(path)
    
        imgnames = []
        for itm in curr_dir:
            if itm != 'tmp.bmp':
                for imgtype in filetypes:
                    if imgtype in itm:
                        imgnames.append(u'%s%s' % (path, itm))
                        
        return imgnames
        
    def sort_images(self, input_list):
        ''' sorts retrieved list of images
        @param input_list: list unicode strings 
        @return list unicode strings
        
        usage: sort_images([u'/path/to/img/img2.jpg', u'/path/to/img/img1.jpg'])
        returns [u'/path/to/img/img1.jpg', u'/path/to/img/img2.jpg']'''
        sort_dict = {}
        output_list = []
        num = re.compile(r'^.*?(\d+).*?')
        
        for img in input_list:
            sort_dict[int(num.search(img).groups()[0])] = img
            
        for i in sorted(sort_dict):
            output_list.append(sort_dict[i])
            
        return output_list