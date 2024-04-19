#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2024/4/18 16:34
# @Author  : anning
# @File    : demo.py
import json

import requests
import jsonpath

response = requests.get('http://192.168.13.178:19983/luda-config/v3/api-docs').json()

print(jsonpath.jsonpath(response, '$...requestBody.content.application/json.schema.$ref'))




