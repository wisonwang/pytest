# -*- coding: utf-8 -*-

import json


def jsonToString(jsonObj):
    try:
        str = json.dumps(jsonObj, indent = 4)
    except Exception:
        str = '{}'
    return str

def stringToJson(jsonString):
    try:
        obj = json.loads(jsonString)
    except Exception:
        obj = {}
    return obj

