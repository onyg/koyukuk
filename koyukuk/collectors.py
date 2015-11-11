# -*- coding: utf-8 -*-
import platform

from koyukuk.db import Client


class Collector(object):

    def __init__(self):
        self.series = []

    def add(self, measurement, values, tags=None):
        if tags is None:
            tags = {}
        if not isinstance(values, dict):
            values = dict(value=values)
        point = dict(
            measurement=measurement,
            fields=values,
            tags=tags
        )
        self.series.append(point)

    def send(self):
        client = Client()
        client.write(self.series)
        self.series = []


class SystemDataCollector(Collector):

    @property
    def hostname(self):
        return platform.node().split('.')[0]

    def tags(self):
        return dict(
            hostname=self.hostname
        )
