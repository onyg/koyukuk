# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from koyukuk.commands import Command


class Setup(Command):

    help_text = 'Helptext for setup'

    def run(self, *args, **options):
        print('RUN SETUP')


class HU(object):
    pass


class Ron(Command):

    def run(self, *args, **options):
        print('RUN RON')
