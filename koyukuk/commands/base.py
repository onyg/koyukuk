# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import sys
import pkgutil
import logging
import six
import abc
import inspect
import importlib

from argparse import ArgumentParser
from clint import textui as clintui
 
logger = logging.getLogger(__name__)

if six.PY2:
    fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()


_command_registry = {}

_command_class_cache = None


def load_commands(command_dir):
    pkg_path = importlib.import_module(command_dir).__path__
    for _loader, name, is_pkg in pkgutil.walk_packages(pkg_path):
        module = importlib.import_module("{}.{}".format(command_dir, name))
        for _name, _cls in inspect.getmembers(module):
            if not inspect.isabstract(_cls) and inspect.isclass(_cls) and is_command(_cls):
                register_command(_name, _cls)


def is_command(_cls):
    from koyukuk.commands.base import Command as C
    return issubclass(_cls, C)


def register_command(name, command_cls):
    global _command_registry
    if not is_command(command_cls):
        return
    key = str(name).lower()
    if key not in _command_registry:
        _command_registry[key] = command_cls


def get_commands():
    return sorted(_command_registry.keys())


def get_command_cls(key):
    key = str(key).lower()
    if key in _command_registry:
        _cli = _command_registry[key]
        return _cli
    return None


def execute_command(key, argv):
    key = str(key).lower()
    if key in _command_registry:
        _cli = _command_registry[key](argv=argv)
        _cli.execute()


class TerminalTextUi(object):

    def __init__(self):
        self.quiet_mode = False

    def puts(self, text):
        if self.quiet_mode:
            return
        clintui.puts(text)

    def print_help(self, parser, epilog):
        if self.quiet_mode:
            return
        parser.print_help()


class CommandParser(ArgumentParser):

    def __init__(self, *args, **kwargs):
        super(CommandParser, self).__init__(*args, **kwargs)


@six.add_metaclass(abc.ABCMeta)
class Command(object):

    help_text = ''

    def __init__(self, argv=None):
        self.argv = argv
        self.output = TerminalTextUi()

    def get_ronald(self):
        return 'Ronald'

    def get_parser(self):
        parser = CommandParser(prog='koyukuk {}'.format(self.__class__.__name__.lower()), description=self.help_text, add_help=False)
        parser.add_argument('-h', '--help', action='store_true', help='show this help message and exit')
        parser.add_argument('--ronald', action='version', version=self.get_ronald())
        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser):
        pass

    def execute(self):
        parser = self.get_parser()

        options, args = parser.parse_known_args(self.argv)
        self.output.quite_mode = options.quiet
        if options.help:
            self.output.puts('-' * 80)
            self.output.print_help(parser)
            return

        self.run(**vars(options))

    @abc.abstractmethod
    def run(self, *args, **options):
        pass


class CommandManager(object):

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[1:]
        load_commands(command_dir='koyukuk.commands')
        self.parser = CommandParser(prog='koyukuk', add_help=False)
        self.output = TerminalTextUi()

    def print_app_header(self):
        from koyukuk import get_version
        self.output.puts('koyukuk version: {}'.format(get_version()))
        self.output.puts('-' * 50)

    def handle_arguments(self):
        pass

    def get_commands(self, *args):
        result = []
        for arg in args:
            if arg in get_commands():
                result.append(get_command_cls(arg))
        return result

    def print_main_help(self):
        self.parser.print_help()
        self.output.puts('Commands', '-' * 41)
        for command in get_commands():
            self.output.puts(command, get_command_cls(command).help_text)
        self.output.puts('-' * 50)
        self.output.puts("Type 'koyukuk <command> --help' for help using a specific command.")

    def execute(self):
        # self.parser.add_argument('-ip', '--help', action='store_true', help='show this help message and exit')
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument('-h', '--help', action="store_true", help='show this help message and exit')
        group.add_argument("-q", "--quiet", action="store_true")
        options, args = self.parser.parse_known_args(self.argv)
        # commands = self.get_commands(*args)
        commands = self.get_commands(*self.argv)
        self.output.quiet_mode = options.quiet
        self.print_app_header()
        if len(commands):
            if options.help:
                self.output.print_help(self.parser)
            for cli in commands:
                c = cli(self.argv)
                c.output = self.output
                c.execute()
        else:
            self.print_main_help()
        # print(commands)
        # print(vars(options))
        # print(args)
        # if options.verbose:
        #     print("verbosity turned on")


        # for a in self.argv:
        #     if a in get_commands():
        #         execute_command(a, self.argv)
