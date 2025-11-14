---
layout: page
title:  后端日常开发/问题排查常用 Linux 命令
date: 2020-10-25 00:00 +0800
update: 2022-11-13 12:00 +0800
---

记录后端开发过程中开发/问题排查中常用到的 Linux 命令。

## 开发调试

### 文本编辑 - vim

简单入门学习可以在 <a href="https://coolshell.cn/articles/5426.html"   target="_blank" rel="noopener nofollow">《简明 Vim 练级攻略 | 酷 壳 - CoolShell》</a> 学习。

学习完以后可以在 <a href="https://vim-adventures.com/"   target="_blank" rel="noopener nofollow">vim-adventures</a> 上加以练习，这个网站将 vim 操作融入游戏中，寓教于乐。

博客中笔记 <a href="/notes/Vim/config"   target="_blank">《Vim 配置与快捷键》</a> 也提到了 Vim 编辑器的配置和快捷键相关的知识拓展。

### 编译器 - gcc/g++

> 编译器处理源代码的过程是 ```预处理 -> 编译 -> 汇编 -> 链接```

- 总体参数

-E 激活预处理（需重定向到文件）

-S 激活预处理和编译，获得汇编代码 ```.s```

-c 激活预处理、编译和汇编 ```.o```

-C 预处理时不删除注释

-M 生成文件关联信息，所依赖的源代码。

-MM 同上，但忽略由 #include 造成的依赖关系

- 目录参数

-ldir 指定头文件位置，没有就在当前文件夹找，再没有就在默认文件夹找

-include 相当于 #include

- 调试参数

-g 产生调试信息

- 连接方式

-static 禁止使用动态链接库

-shared -G 使用动态链接库

- 错误告警参数

-Wall 显示所有警告

-werror 将警告转换成错误，发送警告时终止编译

-w 关闭所有警告，不推荐

- 编译参数

-o 修改默认的文件名

-O0 -O1 -O2 -O3 编译优化选项，0为无优化，默认为1

-fPIC 生成位置无关代码，用于共享库和动态链接

-v 显示详细的编译、汇编、连接命令

> 更多参见 http://www.cnblogs.com/lidan/archive/2011/05/25/2239517.html

### 调试 - gdb

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/gdb.html

info threads

当前所有线程信息

set args -c

调试加 -c 参数 需要其他也可以直接加

(gdb) thread apply all bt

看所有线程的调用

print &a // 打印变量地址
x 0xbffff543  // 查看内存内的变量
x /4xb 0xbffff543 // 单字节查看内存内变量

### 查看依赖库 - ldd

ldd [可执行文件名]

第一列为程序依赖什么库，第二列为系统提供的与程序需要的库所对应的库，第三列为库加载的开始地址

### 二进制文件分析 - objdump

http://man.linuxde.net/objdump

### ELF - readelf

ELF文件(ELF(Executable and Linking Format)是一种对象文件的格式)各段内容，分析链接、符号表

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/readelf.html

### 跟踪进程中的系统调用 - strace

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/strace.html

### 跟踪进程栈 - pstack

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/pstack.html

### 内存映射 - pmap 

```pmap -x [pid]```

Kbytes: 占用内存的字节数
RSS: 保留内存的字节数
Dirty: 脏页的字节数（包括共享和私有的）
Mode: 内存的权限：read、write、execute、shared、private
Mapping: 占用内存的文件、或[anon]（分配的内存）、或[stack]（堆栈）
Device: 设备名 (major:minor)

## 性能分析

### CPU 硬件信息

查看物理cpu个数

``` grep 'physical id' /proc/cpuinfo | sort -u ```

查看核心数量

``` grep 'core id' /proc/cpuinfo | sort -u | wc -l ```

查看线程数

``` grep 'processor' /proc/cpuinfo | sort -u | wc -l ```

主频

``` cat /proc/cpuinfo | grep MHz |uniq ```

型号 

``` cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c ```

### 进程查询 - ps

http://man.linuxde.net/ps

### 进程监控 - top

http://man.linuxde.net/top

显示所有线程 -H


部分指标解释 [https://segmentfault.com/a/1190000008322093](https://segmentfault.com/a/1190000008322093)

### 打开文件查询  - lsof

-i [条件]：列出符合条件的进程。（4、6、协议、:端口、 @ip ）
-p [进程号]：列出指定进程号所打开的文件；
-u [用户名]：列出特定用户名的进程详情
+d<目录>：列出目录下被打开的文件；

http://man.linuxde.net/lsof

```bash
lsof /data|grep delete
```
### 内存使用量 - free

### 监控性能指标 网络吞吐 - sar

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/sar.html

### 虚拟内存统计 - vmstat 

http://man.linuxde.net/vmstat

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/vmstat.html

> Procs（进程）:

r: 运行队列中进程数量
b: 等待IO的进程数量

> Memory（内存）:

swpd: 使用虚拟内存大小
free: 可用内存大小
buff: 用作缓冲的内存大小
cache: 用作缓存的内存大小

> Swap（交换空间）:

si: 每秒从交换区写到内存的大小
so: 每秒写入交换区的内存大小

> IO：（现在的Linux版本块的大小为1024bytes）

bi: 每秒读取的块数
bo: 每秒写入的块数

> system：

in: 每秒中断数，包括时钟中断
cs: 每秒上下文切换数

> CPU（以百分比表示）

us: 用户进程执行时间(user time)
sy: 系统进程执行时间(system time)
id: 空闲时间(包括IO等待时间)
wa: 等待IO时间

### 单个CPU 使用情况 - mpstat

该命令可以显示每个CPU的占用情况，如果有一个CPU占用率特别高，那么有可能是一个单线程应用程序引起的。

### 输出进程的CPU占用率 - pidstat


### IO 使用情况 - iostat

http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/iostat.html

http://man.linuxde.net/iostat

如果%iowait的值过高，表示硬盘存在I/O瓶颈。

%idle值高，表示CPU较空闲。

如果%idle值高但系统响应慢时，有可能是CPU等待分配内存，此时应加大内存容量。

%idle值如果持续低于10，那么系统的CPU处理能力相对较低，表明系统中最需要解决的资源是CPU。

### 程序运行时间 - time

七层测试信息
```bash
time curl "https://www.google.com" -x 1.2.3.4:80 -s
```
显示如下：

real	2m26.351s
user	0m3.456s
sys	0m3.576s

## 网络分析

### AB (apache benchmark)

https://httpd.apache.org/docs/2.0/programs/ab.html

```bash
ab -c 1 -n 100 -p test.txt -k http://127.0.0.1:1234/
```

-c 并发数 -n 总数 -p POST 的内容 -k keepalive

### 网卡配置  - ifconfig

http://man.linuxde.net/ifconfig

### 网络连接 - netstat

http://man.linuxde.net/netstat

-a或--all：显示所有连线中的Socket；
-t或--tcp：显示 TCP 传输协议的状况；
-u或--udp：显示 UDP 传输协议的状况；
-x或--unix：显示 Unix 套接字情况

分类统计脚本

``` netstat -an | awk '/^tcp/ {++state[$6]} END   {for (key in state) print key,"\t",state[key]}' ```

LISTEN 	 3
ESTABLISHED 	 19
TIME_WAIT 	 4

### 网络实时连接速度 - nicstat iftop

[https://linux.cn/article-1588-1.html](https://linux.cn/article-1588-1.html)

### 转发路径（网络层ICMP协议）- traceroute

http://man.linuxde.net/traceroute

### 命令行抓包（网络层/传输层）：tcpdump

http://man.linuxde.net/tcpdump

tcpdump可以将网络中传送的数据包的“头”完全截获下来提供分析

### 抓包（网络层/传输层）筛选：wireshark

[http://blog.51cto.com/laoyinga/1767613](http://blog.51cto.com/laoyinga/1767613)

```
eth.dst==20:dc:e6:f3:78:cc
ip.addr==192.168.1.122                 //根据IP地址筛选，包括源ip或者目的IP
ip.src==192.168.1.122                 //根据源IP地址筛选
ip.dst==192.168.1.122                //根据目的IP地址筛选
tcp.port==80                  //根据TCP端口筛选数据包，包括源端口或者目的端口
tcp.dstport==80               //根据目的TCP端口筛选数据包。
tcp.srcport==80               //根据源TCP端口筛选数据包。
udp.port==4010              //根据UDP端口筛选数据包，包括源端口或者目的端口
udp.srcport==4010            //根据源UDP端口筛选数据包。
udp.dstport==4010           //根据目的UDP端口筛选数据包。
udp

tcp arp icmp smtp pop dns ip ssl http ftp telnet ssh rdp rip ospf

http.request.method==GET http.request.method==POST

||  //逻辑或
&&  //逻辑与
!   //逻辑非
```

### 网络延迟 - mtr

mtr -n https://www.google.com

### DNS 分析 - dig

http://man.linuxde.net/dig

### 网络请求 -  curl

http://man.linuxde.net/curl

```bash
curl -w "\nnamelookup=%{time_namelookup}, connect=%{time_connect}, starttransfer=%{time_starttransfer}, total=%{time_total}, speed=%{speed_download}\n" https://www.google.com
```

https://blog.cloudflare.com/a-question-of-timing/

### SSL 本机性能测试

命令 ``` openssl speed ``` 

### HTTPS 证书及其相关工具

证书链完整性检查 [https://www.sslshopper.com/ssl-checker.html](https://www.sslshopper.com/ssl-checker.html)

证书等级评价 [https://www.ssllabs.com/ssltest/index.html](https://www.ssllabs.com/ssltest/index.html)

证书发布查询 [https://crt.sh/?q=*.google.com](https://crt.sh/?q=*.google.com)

openssl、x509、crt、cer、key、csr、ssl、tls 这些都是什么鬼?

[https://www.cnblogs.com/yjmyzz/p/openssl-tutorial.html](https://www.cnblogs.com/yjmyzz/p/openssl-tutorial.html)

自己用 openssl 生成 CA 证书

[https://blog.csdn.net/fhqsse220/article/details/45918829](https://blog.csdn.net/fhqsse220/article/details/45918829)

SSL证书(HTTPS)背后的加密算法

[https://www.cnblogs.com/TIlifeng/p/5488301.html](https://www.cnblogs.com/TIlifeng/p/5488301.html)


各种HTTPS站点的SSL证书 ,扩展SSL证书,密钥交换和身份验证机制汇总-自由，平等，共享，互助-51CTO博客

[http://blog.51cto.com/shayi1983/1640723](http://blog.51cto.com/shayi1983/1640723)

自签名证书
[https://www.appinn.com/mkcert/](https://www.appinn.com/mkcert/) 
[https://github.com/FiloSottile/mkcert](https://github.com/FiloSottile/mkcert)

```bash
#依赖
sudo apt install libnss3-tools
sudo yum install nss-tools
#运行
mkcert -install
```

### 网页加载分析

工具推荐文章 [https://www.globaldots.com/7-website-speed-test-tools-analyzing-web-performance/](https://www.globaldots.com/7-website-speed-test-tools-analyzing-web-performance/)

瀑布图分析（内容较少） - [https://www.webpagetest.org](https://www.webpagetest.org)

瀑布图分析（试用一次后需要注册账号，内容较多） - [https://www.dareboost.com/en](https://www.dareboost.com/en)

### 公共 DNS（不同国家）

按国家划分的 DNS  [https://www.publicdns.xyz/country/](https://www.publicdns.xyz/country/)

### DNS AAAA ipv6

[https://centralops.net/co/NsLookup.aspx](https://centralops.net/co/NsLookup.aspx)

## 日志分析

### 分割 awk 

awk -F '|' '{print $2}' 

#### 判断大小后再输出

[https://linux.cn/article-7602-1.html](https://linux.cn/article-7602-1.html)

```
No      Item_Name               Quantity        Price
1       Mangoes                    45           $3.45
2       Apples                     25           $2.45
3       Pineapples                 5            $4.45
4       Tomatoes                   25           $3.45
5       Onions                     15           $1.45
6       Bananas                    30           $3.45
```

```bash
cat data  | awk -F '|' '{print $8}' | awk -F ':' '$2 > 14400' | wc -l
```

大于 14400 的行数

按 | 分割的第二个字段

```bash
awk '$3 <= 20 { printf "%s\t%s\n", $0,"TRUE" ; } $3 > 20  { print $0 ;} ' food_list.txt 
```

长度大于 8

```bash
awk '$3 <= 20 && length($2) > 8 { printf "%s\t%s\n", $0,"TRUE" ; } ' food_list.txt 
```

### 排序 sort

### 计数 wc(word count)

-l 计算行数

-c 字节数

-m 字符数

-w 单词数

### uniq 去重

-c 统计出现的次数，要排序

-d 只打印重复的部分

-u 只打印不重复的部分

-i 忽略大小写

### grep 过滤特定关键词

#### grep 文件夹范围内搜索

grep -rn "content" .

grep -a "xxx" a.log // grep认为a.log是二进制文件

## 服务器管理

### tar 文件压缩与解压缩

tar -zcvf 压缩名.tar.gz 源文件1 源文件2
tar -zcvf 路径/压缩名.tar.gz 源文件1 源文件2
tar -zxvf
tar -zxvf 压缩文件名.tar,gz -C /路径 （解压缩到特定路径
tar -ztvf 压缩文件名.tar,gz （查看压缩文件内容

### zcat 查看压缩文件里的内容

### sz

将选定的文件发送（send）到本地机器

### rz

在弹出的框中选择文件，上传文件的用户和组是当前登录的用户


### 快速查看机器负载 uptime

### 系统日志 dmesg

### 日志重定向

＆>file、2>&1、1>&2
