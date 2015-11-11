# -*- coding: utf-8 -*-
import logging
from influxdb import InfluxDBClient

from koyukuk.config import config

logger = logging.getLogger(__name__)


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Client(object):

    def __init__(self):
        self.credentials = config.influxdb
        self._db = None

    def connect(self):
        if self._db is None:
            self._db = InfluxDBClient(self.credentials.host,
                                      self.credentials.port,
                                      self.credentials.user,
                                      self.credentials.password,
                                      self.credentials.dbname)
        return True

    def write(self, data):
        if self.connect():
            self._db.write_points(data)
