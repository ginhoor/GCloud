#!/bin/bash

############################################################
#配置

dirname=$(dirname "$0")
tag=$1
if [ $tag == "" ];then
    echo 需要输入环境标识符
    exit
fi

file_name="${tag}_network_ip"
file_path=${dirname}/${file_name}
echo ${file_path}

get_network_ip_api="http://ipv4.icanhazip.com"
############################################################

network_ip=$(curl ${get_network_ip_api})
# 外网IP
echo 外网IP: ${network_ip}

need_update=0

if [ -f "${file_path}" ]; then
    # 当前存储IP
    current_network_ip=$(cat ${file_path})
    echo 当前存储IP: ${current_network_ip}
    if [ "${network_ip}" != "${current_network_ip}" ];then
        need_update=1
    fi
else
    need_update=1
fi

if [ ${need_update} -eq 1 ];then
    # 记录外网IP
    echo ${network_ip} > ${file_path}
    # 切回项目地址
    cd ${dirname}/../../
    git pull
    git add .
    git commit -m "更新外网IP"
    git push
fi