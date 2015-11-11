# -*- coding: utf-8 -*-
from koyukuk.data.client import Client


def add(measurement, tags, values):
    if not isinstance(values, dict):
        values = dict(value=values)
    point = dict(
        measurement=measurement,
        fields=values,
        tags=tags
    )
    client = Client()
    client.write([point])
