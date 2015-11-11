# -*- coding: utf-8 -*-
import psutil

from koyukuk.handlers.base import SystemDataHandler


class DiskUsageHandler(SystemDataHandler):

    name = 'Disk usage'
    key = 'disk.usage'
    mount_point = '/'

    def values(self):
        values = psutil.disk_usage(self.mount_point)
        return {
            'total': values[0],
            'used': values[1],
            'free': values[2],
            'percent': values[3],
        }
