#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from charon_pluto.extension import cp_time
import sys,time,requests, os

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
    print(url)
    response = requests.get(url)
    print(response)
    if response.status_code == 500:
        os._exit(1)

    time.sleep(5)

def create_recently_data(day_size):
    today = cp_time.cp_now_to_timestamp("%Y-%m-%d")
    offset = 60*60*24
    day_list = []
    for index in range(day_size):
        day = today - offset*index
        day_list.append(day)
    print(len(day_list))
    for day in reversed(day_list):
        date = cp_time.cp_timestamp_to_date(day, "%Y-%m-%d")
        for service in service_list:
            start_create_request(service, date)

if __name__ == "__main__":
    create_recently_data(3000)

    # date = None
    # if len(sys.argv) > 1:
    #     date = sys.argv[1]
    # for service in service_list:
    #     start_create_request(service, date)
