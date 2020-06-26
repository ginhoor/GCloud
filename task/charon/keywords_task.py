#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from charon_pluto.extension import cp_time
import sys
import requests

host="http://127.0.0.1:12306"
service_list=["news", "society", "economy"]

def start_create_request(service, date=None):
    if date is None:
        today = cp_time.cp_now_to_timestamp("%Y-%m-%d")
        yestoday = today - 60*60*24
        date = cp_time.cp_timestamp_to_date(yestoday, "%Y-%m-%d")
    
    path="keywords/{}/create".format(service)
    params="date={}".format(date)

    url = "{}/{}?{}".format(host, path, params)
    response = requests.get(url)
    print(response)

if __name__ == "__main__":
    date = None
    if len(sys.argv) > 1:
        date = sys.argv[1]
    for service in service_list:
        start_create_request(service, date)
