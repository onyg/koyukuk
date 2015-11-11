# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from koyukuk.commands import Command


class Help(Command):

    def run(self, *args, **options):
        print('RUN Help')
