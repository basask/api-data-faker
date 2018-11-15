# -*- coding: utf-8 -*-
#
# Created: 15/11/2018 12:29:45
# Author: Basask (basask@gmail.com)


class GenericModel(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
