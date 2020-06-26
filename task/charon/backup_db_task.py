#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

if __name__ == "__main__":
    host = "http://127.0.0.1:12306"
    url = "{}/task/backupdb".format(host)
    response = requests.get(url)
    print(response)