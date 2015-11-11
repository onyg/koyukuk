# -*- coding: utf-8 -*-

import logging
import psutil

from koyukuk.handlers.base import SystemDataHandler


class CPUPercentHandler(SystemDataHandler):

    name = 'CPU percentage'
    key = 'cpu.percentage'

    def values(self):
        value = self.value_for_cpu()
        return {
            'percent': value
        }

    def value_for_cpu(self, cpu_index=None):
        """
        Stub for keeping the code to demonstrate how to access single cpu's
        """

        if cpu_index is None:
            return psutil.cpu_percent()

        try:
            return psutil.cpu_percent(percpu=True)[cpu_index]
        except IndexError:
            logging.error('Unknwown cpu index "{}"'.format(cpu_index))

        return 0
