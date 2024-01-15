#!/bin/bash

############################################################
#配置

dirname=$(dirname "$0")
tag=$1
if [ "$tag" == "" ];then
    echo 需要输入环境标识符
    exit
fi

file_name="${tag}_network_ip"
file_path=${dirname}/${file_name}
echo ${file_path}

get_network_ip_api="ifconfig.me"
############################################################

network_ip_result=$(curl ${get_network_ip_api})
if test -z "${network_ip_result}"; then
    echo 请求IP API失败
    exit
fi
# 外网IP
echo ${network_ip_result}

network_ip=$(echo ${network_ip_result}| sed -nr "s#[^0-9]*((1[0-9]{2}|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[1-9])(\.(1[0-9]{2}|2[0-4][0-9]|25[0-5]|[1-9][0-9]|[0-9])){3}).*#\1#p")
echo 当前外网IP：${network_ip}

if test -z "${network_ip}"; then
    echo 解析IP失败
    exit
fi

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
    echo 监测到IP变更
    # 记录外网IP
    echo ${network_ip} > ${file_path}
    # 切回项目地址
    cd ${dirname}/../../
    export https_proxy=http://127.0.0.1:7890;export http_proxy=http://127.0.0.1:7890;export all_proxy=socks5://127.0.0.1:7890
    git pull
    git add .
    git commit -m "更新外网IP"
    git push
fi