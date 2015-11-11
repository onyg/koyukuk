# -*- coding: utf-8 -*-
import platform


class Handler(object):
    key = ''

    def tags(self):
        return {}

    def values(self):
        return {}

    def handle(self, collector):
        collector.add(measurement=self.key,
                      values=self.values(),
                      tags=self.tags())


class SystemDataHandler(Handler):

    @property
    def hostname(self):
        return platform.node().split('.')[0]

    def tags(self):
        return dict(
            hostname=self.hostname
        )
