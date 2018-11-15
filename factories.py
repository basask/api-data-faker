# -*- coding: utf-8 -*-
#
# Created: 15/11/2018 12:29:00
# Author: Basask (basask@gmail.com)

from collections import defaultdict
from random import randint, random

import factory as factory_boy
from faker import Faker

from models import GenericModel


def generate_debts():
    quantity = randint(0, 10)
    instance = Faker(locale='pt_BR')
    return [
        {
            'owner': instance.company(),
            'amount': 100 + randint(0, 100000),
        }
        for _ in range(quantity)
    ]

class FactoryA(factory_boy.Factory):
    class Meta(object):
        model = GenericModel

    name = factory_boy.Faker('name', locale='pt_BR')
    address = factory_boy.Faker('address', locale='pt_BR')
    debt_list = factory_boy.LazyFunction(generate_debts)

def generate_income():
    seed = randint(0, 100)
    quantity = 0
    if seed < 95:
        quantity = 5
    if seed < 93:
        quantity = 4
    if seed < 89:
        quantity = 3
    if seed < 82:
        quantity = 2
    if seed < 79:
        quantity = 1
    instance = Faker(locale='pt_BR')
    return [
        {
            'company': instance.company(),
            'job': instance.job(),
            'wage': 100 + randint(0, 10000),
        }
        for _ in range(quantity)
    ]


def generate_state():
    quantity = randint(0, 5)
    ctype = randint(0, 1)
    instance = Faker(locale='pt_BR')
    types = {
        'auto': instance.license_plate(),
        'iban': instance.iban()
    }

    ret = list()
    for _ in range(quantity):
        ctype = randint(0, len(types) - 1)
        t = list(types.keys())[ctype]
        ret.append({
            'type': t,
            'description': types[t],
            'value': 1000 * randint(0, 100000),
        })
    return ret


class FactoryB(factory_boy.Factory):
    class Meta(object):
        model = GenericModel

    name = factory_boy.Faker('name', locale='pt_BR')
    address = factory_boy.Faker('address', locale='pt_BR')
    birtdate = factory_boy.Faker(
        'date_between', start_date="-50y", end_date="-18y"
    )
    state_list = factory_boy.LazyFunction(generate_state)
    income_list = factory_boy.LazyFunction(generate_income)


def generate_creadit_card_move():
    cards = randint(0, 5)
    ret = defaultdict(list)
    for card in range(cards):
        faker = Faker(locale='pt_BR')
        card_number = faker.credit_card_number()
        card_balance = list()
        for _ in range(randint(0, 50)):
            card_balance.append(
                {
                    'company': faker.company(),
                    'value': round(2 + random() * 2000.0, 2)
                }
            )
        ret[card_number] = card_balance
    return ret

class FactoryC(factory_boy.Factory):
    class Meta(object):
        model = GenericModel
    name = factory_boy.Faker('name', locale='pt_BR')
    creadit_card = factory_boy.LazyFunction(generate_creadit_card_move)
