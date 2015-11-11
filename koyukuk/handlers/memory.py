# -*- coding: utf-8 -*-
import psutil

from koyukuk.handlers.base import SystemDataHandler


class VirtualMemoryHandler(SystemDataHandler):

    name = 'Virtual memory usage'
    key = 'memory.virtual.usage'

    def values(self):
        values = psutil.virtual_memory()
        return {
            'total': values.total,
            'available': values.available,
            'percent': values.percent,
            'used': values.used,
            'free': values.free,
            'active': values.active,
            'inactive': values.inactive
        }


class SwapMemoryHandler(SystemDataHandler):

    name = 'Swap memory usage'
    key = 'memory.swap.usage'

    def values(self):
        values = psutil.swap_memory()
        return {
            'total': values.total,
            'used': values.used,
            'free': values.free,
            'percent': values.percent,
            'sin': values.sin,
            'sout': values.sout
        }
