# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 18:21:53 2016
@author: juliojaavier
"""

class helloWorld(object):
    def __init__(self, name = 'juliojaavier', **kwargs):
        self.name = name
    def __str__(self):
        return 'Hello World - @%s' % self.name
        
if __name__ == '__main__':
    print(helloWorld())

