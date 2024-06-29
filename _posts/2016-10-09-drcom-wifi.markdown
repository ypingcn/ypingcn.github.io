---
layout: post
title:  "Dr.com 认证的校园网里使用 WiFi"
subtitle: "Solution for Dr.com,Wifi users in Campus Network"
description: "在 Openwrt 进行相关配置，以便在 Dr.com 认证的校园网里使用 WiFi"
date:   2016-10-09 +0800
update: 2021-11-02 22:39 +0800
author:     "ypingcn"
header-img: "img/home-bg-Sm5ceH.webp"
header-mask: 0.3
catalog:    true
tags:
    - 教程
    - 技术
---

昨天校园网改造，从 inode 的认证换成 Dr.com 的认证，无线路由器又是要重新折腾一番了。手头上有的是淘来的 TP-Link TL-WR740N v5 的硬件，已经安装了带有 LuCI 的 OpenWrt Barrier Breaker r36195 ，自带锐捷认证和 H3C 认证。



## 连接网络

用浏览器登录192.168.1.1（管理路由器的IP地址），点击选项卡里的 网络 -> 无线 -> 搜索 选项，将路由器加入可以使用的网络。



## 更改软件源

点击 系统–>>软件包–>>配置 选项，将路由器的openwrt的软件源修改为相应版本。

```
src/gz barrier_breaker_base http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/base  
src/gz barrier_breaker_luci http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/luci  
src/gz barrier_breaker_packages http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/packages  
src/gz barrier_breaker_routing http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/routing  
src/gz barrier_breaker_telephony http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/telephony  
src/gz barrier_breaker_management http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/management  
src/gz barrier_breaker_oldpackages http://downloads.openwrt.org/barrier_breaker/14.07/ar71xx/generic/packages/oldpackages
```

14.07是 openwrt 的版本号，ar71xx 是硬件分类，可以尝试```opkg update```命令查看报错信息大致确认。



## 安装Python环境

ssh 连接进路由器（ Windows 用 putty ，Linux 可以直接在终端执行```ssh root@192.168.1.1```，用户名和IP地址大同小异），执行以下命令安装Python运行环境。

```
opkg update
opkg install python-mini
```



## 处理错误

终端里运行在 <a href="https://github.com/drcoms/drcom-generic/wiki/%E5%85%B3%E4%BA%8EP%E7%89%88%E7%9A%84PPPoE%E6%8B%A8%E5%8F%B7%E9%97%AE%E9%A2%98" rel="nofollow">关于P版的PPPoE拨号问题</a> 的HighLight部分运行所提供的命令

```
#!/bin/sh
cp /lib/netifd/proto/ppp.sh /lib/netifd/proto/ppp.sh_bak
sed -i '/proto_run_command/i username=`echo -e "$username"`' /lib/netifd/proto/ppp.sh
sed -i '/proto_run_command/i password=`echo -e "$password"`' /lib/netifd/proto/ppp.sh
```



## 登录抓包

按照 <a href="https://github.com/drcoms/drcom-generic/wiki/%E5%85%B3%E4%BA%8EP%E7%89%88%E7%9A%84PPPoE%E6%8B%A8%E5%8F%B7%E9%97%AE%E9%A2%98" rel="nofollow">关于P版的PPPoE拨号问题</a> 用 wireshark 抓包生成 config.txt，相同学校内容应该相同，内容类似于

```
server = '1.1.1.1'
pppoe_flag = '\x1d'
keep_alive2_flag = '\xd8'
```



## 上传文件

Windows 用户应使用支持 **Unix换行符** 的文件编辑器，如 *Editplus, notepad2, notepad++* ,sublime text 编辑以下文件。

Linux 用```scp``` ，Windows 下用 WinSCP 将本地修改的文件替换（或增添/修改）路由器里的文件

```
/usr/bin/drcom
/usr/bin/pppoe.sh
/etc/drcom.conf
```

```/usr/bin/drcom``` : 自己学校可用的心跳认证 python 脚本，<a href="https://github.com/drcoms/drcom-generic/issues/116#issuecomment-250953770" rel="nofollow">drcom5.2.0 p心跳不对。#82的也不能用 #116</a> 这个反馈中提供的脚本代码可在自家学校的环境中使用。

```/etc/drcom.conf``` : 使用登录抓包获取到的config.txt文件。

```/usr/bin/pppoe.sh``` : 使用 <a href="https://github.com/drcoms/drcom-generic/wiki/p%E7%89%88%E7%AE%80%E7%95%A5%E4%BD%BF%E7%94%A8%E5%92%8C%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E" rel="nofollow">p版简略使用和配置说明</a> 提到的  <a href="https://github.com/drcoms/drcom-generic/raw/master/custom/pppoe.sh" rel="nofollow">地址</a> 替换，最后一行的```exec python /usr/bin/drcom-pppoe.py``` 改为 ```exec python /usr/bin/drcom```

上传后赋予脚本可执行权限：
```
chmod +x /usr/bin/drcom
chmod +x /usr/bin/pppoe.sh
```

## 调整开机启动

在 系统–>>启动项 中先禁用 ```H3C_Client``` 和```mentohust``` ，在本地启动脚本（即```/etc/rc.local``` ）的```exit 0``` 前添加

```
sleep 15
pppoe.sh
```

## 配置上网账号

根据登录抓包获得的文件，在 网络–>>接口–>>WAN–>>修改 里的 PAP/CHAP 用户名和 PAP/CHAP 密码填写相对应的上网账号，抓包得到的文件里账号信息要完全填写，包括 ```/r/n``` 等转义字符。


## 完成

尽情享受上网的乐趣吧！


>  参考

Github wiki 

<a href="https://github.com/drcoms/drcom-generic/wiki/p%E7%89%88%E7%AE%80%E7%95%A5%E4%BD%BF%E7%94%A8%E5%92%8C%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E" rel="nofollow">p版简略使用和配置说明</a>

<a href="https://github.com/drcoms/drcom-generic/wiki/%E5%85%B3%E4%BA%8EP%E7%89%88%E7%9A%84PPPoE%E6%8B%A8%E5%8F%B7%E9%97%AE%E9%A2%98" rel="nofollow">关于P版的PPPoE拨号问题</a> 
