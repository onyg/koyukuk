# -*- coding: utf-8 -*-

from koyukuk.data import add  # noqa
from koyukuk.config import config  # noqa
from koyukuk.collectors import Collector  # noqa

__all__ = ['add', 'config', 'Collector']

__version__ = '0.1.0'


def get_version():
    return __version__
