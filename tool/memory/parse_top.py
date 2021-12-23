#!/usr/bin/env python3
# coding: utf-8

import math

def convertBytes(bytes, lst=None):
    if lst is None:
        lst=['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = int(math.floor( # 舍弃小数点，取小
             math.log(bytes, 1024) # 求对数(对数：若 a**b = N 则 b 叫做以 a 为底 N 的对数)
            ))

    if i >= len(lst):
        i = len(lst) - 1
    return ('%.2f' + " " + lst[i]) % (bytes/math.pow(1024, i))

if __name__ == '__main__':
    with open('memory_log.txt', encoding='utf-8') as f:
        for i in f:
            i = i.strip()
            cut_row = i.split()
            # print(cut_row)
            #   PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
            VSZ = cut_row[4]
            VSZ = convertBytes(int(VSZ)*1024)
            VSZ1 = cut_row[5]
            CPU = cut_row[6]
            CPU1 = cut_row[7]
            COMMAND = cut_row[8]
            # print("{}  CPU[{}/{}%] ".format(COMMAND, CPU, CPU1 ))
            print("{}  MEM[{}/{}%] ".format(COMMAND, VSZ, VSZ1))

            # JAR_NAME = cut_row[-1]
            # if JAR_NAME != 'java':
                # print(RSS)
                # print(JAR_NAME,'    ',convertBytes(int(RSS)*1024))