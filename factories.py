# -*- coding: utf-8 -*-
#
# Created: 15/11/2018 12:29:00
# Author: Basask (basask@gmail.com)

import factory as factory_boy

from models import GenericModel


class FactoryA(factory_boy.Factory):
    class Meta(object):
        model = GenericModel

    name = factory_boy.Faker('name')


class FactoryB(factory_boy.Factory):
    class Meta(object):
        model = GenericModel

    name = factory_boy.Faker('name')


class FactoryC(factory_boy.Factory):
    class Meta(object):
        model = GenericModel

    name = factory_boy.Faker('name')
