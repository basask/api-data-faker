# -*- coding: utf-8 -*-
#
# Created: 15/11/2018 12:00:31
# Author: Basask (basask@gmail.com)

import sys
from multiprocessing import Process

from sanic import Sanic
from sanic.response import json

from factories import FactoryA, FactoryB, FactoryC

SERVICE_MAP = {
    'service_a': {'factory': FactoryA, 'port': 8881},
    'service_b': {'factory': FactoryB, 'port': 8882},
    'service_c': {'factory': FactoryC, 'port': 8883},
}


def service_runner(factory_class, port):
    app = Sanic()

    @app.route('/<key>')
    async def test(request, key):
        instance = factory_class(cpf=key)
        return json(instance.__dict__)
    app.run(host='0.0.0.0', port=port)


def run():
    services = sys.argv[1:]
    if not services:
        raise Exception(
            'At least one service must be informed. Services are: {}'.format(
                ', '.join(SERVICE_MAP.keys()
                          )
            )
        )

    for service_id in services:
        if service_id not in SERVICE_MAP:
            raise Exception(
                'Service {} no in list: {}'.format(
                    service_id, ', '.join(SERVICE_MAP.keys())
                )
            )
        service = SERVICE_MAP.get(service_id)

        factory = service.get('factory')
        port = service.get('port')

        proc = Process(target=service_runner, args=(factory, port))
        proc.start()


if __name__ == '__main__':
    run()
