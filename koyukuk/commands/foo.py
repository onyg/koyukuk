# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import sys
import os

sys.path.insert(0, os.path.abspath('..'))

from clint.textui import puts, indent, colored, prompt, validators
from clint.textui import columns
from time import sleep
from random import random
from clint.textui import progress
from clint import piped_in

from koyukuk.commands import Command


lorem = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'


class Foo(Command):

    def run(self):
        for i in progress.bar(range(100)):
            sleep(random() * 0.2)

        with progress.Bar(label="nonlinear", expected_size=10) as bar:
            last_val = 0
            for val in (1, 2, 3, 9, 10):
                sleep(2 * (val - last_val))
                bar.show(val)
                last_val = val

        for i in progress.dots(range(100)):
            sleep(random() * 0.2)

        for i in progress.mill(range(100)):
            sleep(random() * 0.2)

        # Override the expected_size, for iterables that don't support len()
        D = dict(zip(range(100), range(100)))
        for k, v in progress.bar(D.items(), expected_size=len(D)):
            sleep(random() * 0.2)


class FooTwo(Command):

    def add_arguments(self, parser):
        parser.add_argument('--foo', action="store_true")

    def run(self, **options):
        print('FOOTWO')
        if options.get('foo', False):
            print('FOOARGS')
        # # Standard non-empty input
        # name = prompt.query("What's your name?")

        # # Set validators to an empty list for an optional input
        # language = prompt.query("Your favorite tool (optional)?", validators=[])

        # # Shows a list of options to select from
        # inst_options = [{'selector':'1','prompt':'Full','return':'full'},
        #                 {'selector':'2','prompt':'Partial','return':'partial'},
        #                 {'selector':'3','prompt':'None','return':'no install'}]
        # inst = prompt.options("Full or Partial Install", inst_options)

        # # Use a default value and a validator
        # path = prompt.query('Installation Path', default='/usr/local/bin/', validators=[validators.PathValidator()])

        # puts(colored.blue('Hi {0}. Install {1} {2} to {3}'.format(name, inst, language or 'nothing', path)))


class FooThree(Command):

    def add_arguments(self, parser):
        parser.add_argument('--foo', action="store_true")

    def run(self, **options):
        print('FOOTHREE')
        # # Standard non-empty input
        # name = prompt.query("What's your name?")

        # # Set validators to an empty list for an optional input
        # language = prompt.query("Your favorite tool (optional)?", validators=[])

        # # Shows a list of options to select from
        # inst_options = [{'selector':'1','prompt':'Full','return':'full'},
        #                 {'selector':'2','prompt':'Partial','return':'partial'},
        #                 {'selector':'3','prompt':'None','return':'no install'}]
        # inst = prompt.options("Full or Partial Install", inst_options)

        # # Use a default value and a validator
        # path = prompt.query('Installation Path', default='/usr/local/bin/', validators=[validators.PathValidator()])

        # puts(colored.blue('Hi {0}. Install {1} {2} to {3}'.format(name, inst, language or 'nothing', path)))
