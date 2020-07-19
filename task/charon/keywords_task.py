#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from charon_pluto.extension import cp_time
import sys,time,requests, os

# host = "http://127.0.0.1:12306"
host = "http://172.66.1.10:12306"

def start_create_request(service, date=None):
    if date is None:
        today = cp_time.cp_now_to_timestamp("%Y-%m-%d")
        yestoday = today - 60*60*24
        date = cp_time.cp_timestamp_to_date(yestoday, "%Y-%m-%d")
    
    if service == 'analyze':
        path = "keywords/{}/frequency".format(service)
        params = "date={}".format(date)
    else:
        path = "keywords/{}/create".format(service)
        params = "date={}".format(date)

    url = "{}/{}?{}".format(host, path, params)
    print(url)
    response = requests.get(url)
    print(response)
    if response.status_code == 500:
        os._exit(1)
    time.sleep(1.5)

def create_recently_data(day_size, service_list):
    today = cp_time.cp_now_to_timestamp("%Y-%m-%d")
    offset = 60*60*24
    day_list = []
    for index in range(day_size):
        day = today - offset*index
        day_list.append(day)
    for day in reversed(day_list):
        date = cp_time.cp_timestamp_to_date(day, "%Y-%m-%d")
        for service in service_list:
            start_create_request(service, date)

def create_range_data(start_date, day_size, service_list):
    start = cp_time.cp_date_to_timestamp(start_date,"%Y-%m-%d")
    offset = 60*60*24
    for index in range(day_size):
        day = start + offset*index
        date = cp_time.cp_timestamp_to_date(day, "%Y-%m-%d")
        for service in service_list:
            start_create_request(service, date)

if __name__ == "__main__":
    fetch_type = int(sys.argv[1])
    if fetch_type == 1:
        # 分析昨天关键字
        service_list = ["news", "economy", "analyze"]
        for service in service_list:
            start_create_request(service)

    elif fetch_type == 2:
        # 分析当天关键字
        service_list = ["news", "economy", "analyze"]
        for service in service_list:
            today = cp_time.cp_now_to_timestamp("%Y-%m-%d")
            start_create_request(service, today)

    elif fetch_type == 3:
        day_size = int(sys.argv[2])
        # 分析截止今天的x天时间，专业新闻
        service_list = ["news", "economy", "analyze"]
        create_recently_data(day_size, service_list)

    elif fetch_type == 4:
        start_date = sys.argv[2]
        day_size = int(sys.argv[3])
        # 分析一段时间，社会新闻
        service_list = ["news", "economy", "analyze"]
        create_range_data(start_date, day_size, service_list)

    elif fetch_type == 5:
        start_date = sys.argv[2]
        day_size = int(sys.argv[3])
        # 分析一段时间关键字词频
        service_list = ["analyze"]
        create_range_data(start_date, day_size, service_list)