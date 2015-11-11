# -*- coding: utf-8 -*-
import os

import yaml


config_values = dict(
    influxdb=dict(
        host='127.0.0.1',
        port=8086,
        dbname='metrics',
        user=None,
        password=None
    )
)


class Config(dict):

    def __init__(self, defaults=None, **kwargs):
        super(Config, self).__init__()
        _data = defaults or config_values
        _data.update(kwargs)
        self.from_dict(_data)

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        if isinstance(value, dict):
            value = Config(value)
        super(Config, self).__setitem__(key, value)

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Config, self).__delitem__(key)
        del self[key]

    def __dir__(self):
        return sorted(set(dir(type(self)) + self.keys()))

    def default_yaml_filepath(self):
        config_file = 'koyukuk.yml'
        default_path = '~/.koyukuk/'
        abs_default_path = os.path.normpath(
            os.path.abspath(os.path.expanduser(default_path)))
        working_path = os.getcwd()
        _filepath = os.path.join(working_path, config_file)
        if os.path.exists(_filepath):
            return _filepath
        return os.path.join(abs_default_path, config_file)

    def from_yaml(self, filepath=None):
        if not filepath:
            filepath = self.default_yaml_filepath()
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = yaml.load(f)
            return self.from_dict(data)
        return False

    def from_dict(self, data):
        if isinstance(data, dict):
            for key, value in data.iteritems():
                if key in self:
                    if isinstance(value, dict):
                        if isinstance(self[key], Config):
                            self[key].from_dict(value)
                            continue
                if isinstance(value, dict):
                    self[key] = Config(value)
                else:
                    self[key] = value
            return True
        return False


config = Config()
config.from_yaml()
