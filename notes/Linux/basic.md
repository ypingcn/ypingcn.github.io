---
layout: page
title:  Linux 基础命令
update: 2016-04-01 12:00 +0800
---

## 基本解释

### root@localhost:  ~#

用户名 主机名 所在位置 $为普通用户，#为超级用户

### -rw-r--r--

d 目录 l 软链接文件 - 文件

rw- r-- r--

所有者 所属组 其他人

r读 w 写 x 执行

### ls

>  list

```
ls [通配符]

ls -a 所有文件

ls -l 详细信息

ls -d 目录属性

ls -h 人性化显示（文件大小单位）

ls -i 显示inode（被用来确认文件位置的ID号）
```

### ll

是``` ls -l```命令的别名

### 常见目录作用

#### /

根目录

#### /bin  /usr/bin /sbin /usr/sbin

系统命令保存的目录 /bin  /usr/bin 保存普通用户可以执行的命令，/sbin /usr/sbin为只有超级用户可以执行的命令。

#### /boot

启动目录

#### /dev

设备文件

#### /etc

配置文件

#### /home

普通用户的家目录

#### /lib

系统库

#### /mnt

系统挂载

#### /media

挂载

#### /root

超级用户家目录

#### /tmp

临时文件

#### /proc

直接写入内存

#### /sys

#### /var

系统相关文档

#### /usr

系统软件资源





## 文件处理命令

### mkdir -p 【路径/目录名】

>  make diretory

### cd

> change diretory

绝对路径 和 相对路径 的区别

```
cd ~
cd - 进入上次目录
cd ..
cd .
```

### pwd

>  print working diretory

### rmdir

> remove empty diretory

### rm

```
rm -r 删目录
rm -f 强制
```

### cp

> copy

```
cp -r 复制目录
cp -p 连带文件属性
cp -d 源文件是链接文件 则复制链接属性
cp -a == cp -r -p -d
```

### mv 【原文件或目录】 【目标目录】

> move  (剪切或改名)
> 

### touch (2018.01-31)

touch 除了能创建一个空文件之外，还能修改文件的最后修改时间和存取时间，例子

```bash
-a   或--time=atime 　只更改存取时间。
-m   或--time=mtime 　只更改变动时间。
-r 　把指定文档或目录的日期时间，统统设成和参考文档或目录的日期时间相同。 后面的改成前面的 touch -r a b 【a改成跟b一样的时间】
```

struct stat 里有两个变量可以帮助理解 

time_t     st_atime;      //最后一次访问该文件的时间
time_t     st_mtime;      //最后一次修改该文件的时间
  
  
### ln

> link

```
ln 硬链接
ln -s 软链接
```

硬链接【不建议】

相同inode节点和存储block块

不能跨分区和不能针对目录使用

软链接

拥有自己的inode节点和block块，但数据块中只保存原文件的文件名和inode节点

权限都是 lrwxrwxrwx

## 文件搜索命令

### PATH环境变量

```
echo $PATH
```

### locate

在后台数据库搜索文件，速度快

updatedb 更新 /etc/updatedb.conf

### whereis

搜索命令的命令

```
whereis -b 只查找可执行文件
whereis -m 只查找帮助文件
```

### which

搜索命令的命令

whereis + 显示命令别名

### find 【搜索范围】【搜索条件】

```
find /home -name abc[cd]
find /home -iname abc 不区分大小写
find /home -user root 按所有者搜索
find /home -nouser 查找没所有者的文件
* 匹配任意内容
? 匹配任意一个字符
[] 匹配任意一个中括号内的字符

find /home -mtime -10
-10 以当天为标志往前10天 到 当天
10 以当天为标准往前10天  的 当天
+10 以当天为标准往前10天 的 之前
-atime [access time] 访问
-ctime [change time] 改变文件属性
-mtime [modify time] 修改文件内容

-size 按文件大小查找
-1k 小于
1k 等于
+1k 大于
k小写 M大写

-inum 查找特定inode节点的文件

find /etc -size +100k -a -size -200k -exec ls -lh {} \;
-a and
-o or
-exec ls -lh {} \; 之后同时执行 ls -lh ,  -exec 和 {} \； 配对出现[?Todo]
```

### grep

```
搜索文件里的内容

grep [选项] 字符串 文件名
-i 忽略大小写
-v 排除指定字符串
```

## 帮助命令

### man

类型分类

```
查看命令拥有哪个级别的帮助
man -f 命令 = whatis 命令
man -5 passwd
-1 命令帮助
-2 被内核调用的函数的帮助
-3 C函数库帮助
-4 设备特殊文件的帮助
-5 配置文件的帮助
-6 游戏等帮助
-7 其他帮助
-8 系统管理员可用命令帮助
-9 内核相关文件的帮助
man -k 命令 = apropos 命令 搜索关键字并且显示所有包含匹配项的man页面的简短描述
```

### --help help

用whereis 和 man 根据路径确定是否为shell内部命令

### info

```
回车进入带星号的子帮助页面
u 上层页面
n 下一个帮助小节
p 上一个帮助小节
q 退出
```

## 文件压缩命令

### zip

```
zip 文件名 源文件
zip -r 文件名 源目录
unzip 文件
```

### gz

```
gzip 源文件 （删除源文件
gzip -c 源文件 > 压缩文件 （保留源文件
gzip -r （压缩目录里的所有子文件，为每个文件创建压缩包
gzip -d 文件名（解压缩文件
gunzip 解压缩的文件名（不保留原文件
```

### bz2

```
bzip2 源文件(压缩，删除原文件)
bzip2 -k 源文件（保留原文件
bzip2 -d  文件名（解压缩，-k保留原文件
bzip2  文件名（解压缩，-k保留原文件
```

### tar

```
tar -cvf 打包文件名 源文件
-c 打包
-v 显示打包过程
-f 指定打包后的文件名
tar -xvf 文件名 （解压缩
-x 解压缩
```

### tar.gz

```
tar -zcvf 压缩名.tar.gz 源文件1 源文件2
tar -zcvf 路径/压缩名.tar.gz 源文件1 源文件2
tar -zxvf
tar -zxvf 压缩文件名.tar,gz -C /路径 （解压缩到特定路径
tar -ztvf 压缩文件名.tar,gz （查看压缩文件内容
```

### tar.bz2

```
tar -jcvf 文件名.tar.bz2 源文件
tar -jxvf
```

## 关机重启命令

### shutdown

```
shutdown 选项 时间
-c 取消上一个命令
-h 关机
-r 重启
```

### *halt poweroff init 0*

### reboot

### *init 6*

```
系统运行级别
0 关机
1 单用户
2 不包含NFS服务的多用户
3 完全多用户
4 未分配
5 图形界面
6 重启

runlevel 查看运行级别，显示之前的运行级别和当前运行级别

cat /etc/inittab
```



## 挂载命令

### mount

```
mount
mount -a （自动挂载，配置文件是/etc/fstab
mount -t 【文件系统】 -o 【特殊选项】 【设备文件名】 【挂载点】
mount -o remount,exec /home
//挂载光盘
mkdir /mnt/cdrom
mount -t iso9660 /dev/sr0 /mnt/cdrom
//卸载光盘
umount /mnt/cdrom
//挂载优盘
fdisk -l
mkmdir /mnt/usb
mount -t vfat /dev/sdb1 /mnt/usb
```

## 用户登录查看命令

### w

```
USER 用户名
TTY 登录终端，pst/0远程，tty1本地
FROM 从哪个IP地址登录
LOGIN@ 登录时间
IDLE 用户闲置时间
JCPU 当前正在运行的后台作业所占用是时间和终端连接的所有进程占用的时间
PCPU 当前进程占用的时间
WHAT 正在运行的命令
```

### who

简洁版```w```

### last

```
查看当前登录用户和过去登录用户信息
/var/log/wtmp
```

### lastlog

```
查看所有用户的最后一次登录信息
/var/log/lastlog
```



## shell基础

bourne shell & C shell

```
#!/bin/bash

echo $SHELL
vim /etc/shells 查看支持的SHELL

chmod 755 hello.sh
./hello.sh

bash hello.sh
```

### echo

```
echo -e "\n" （支持转义字符、十六进制、八进制
echo -e "\e[1; 【颜色编码】 【内容】 \e[0m" （输出内容带颜色
```

### 别名与快捷键

```
alias ls = 'ls --color=never'
vi ~/.bashrc 写入环境变量配置文件
unalias 删除别名

命令执行优先级
1、有绝对路径或者相对路径
2、别名
3、shell命令
4、$PATH

ctrl+c 终止
ctrl+l 清屏
ctrl+a 光标移到命令行首
ctrl+e 光标移到命令行尾
ctrl+u 删除光标位置到行首的内容
ctrl+z 后台
ctrl+r 在历史命令搜索
```

### 历史命令

```
history -c 【清空历史命令】
history -w 【缓存中的历史命令写入./bash_history】
!n 重复执行第N条命令
!! 重复执行上一条命令
!【字符串】重复执行最后一条以该字符串开头的命令
```

### 输出重定向

```
0	标准输入
1	标准输出的重定向
命令 > 文件 【覆盖】
命令 >> 文件 【追加】
2	标准错误的重定向
命令 2> 文件 【覆盖】
命令 2>> 文件 【追加】

正确或者错误都写入
命令 > 文件 2>&1【覆盖】
命令 >> 文件 2>&1 【追加】
命令 &> 文件 【覆盖】
命令 &>> 文件 【追加】
命令 >> 文件a 2 >> 文件b 【正确到A，错误到B】

/dev/null
```

### 输入重定向

```
wc file
-c 统计字节数
-w 统计单词数
-l 统计行数
```

## 管道符

###  多命令顺序执行

```
;  无关系
&& 第一个命令正确就执行第二个
|| 第一个命令正确就不执行第二个 第一个错误就执行第二个
ls || echo no && echo yes
```

### 管道符

```
命令a | 命令b
命令a的正确输出作为命令b的操作对象
```

### 通配符

```
? 任意一个字符
* 任意一个或多个字符
[] 括号内的任意一个字符
[-] 表示范围 [a-z]表示小写字母
[^] 不是括号内的字符 [^0-9]表示不是数字

'' 不识别特殊含义
"" 识别特殊含义
`` 反引号 同$()
$() 引用系统命令
# 注释
￥ 用于调用变量的值
\ 转义字符

```

## 磁盘管理

### df
```
磁盘使用情况
-l 本地磁盘（默认）
-a 所有文件磁盘的使用情况
-h 1024进制
-H 1000进制
-T 显示磁盘类型
-t 显示指定类型
-x 不显示指定类型
```

### du
```
统计磁盘上文件大小 无参显示当前文件夹下的文件
-b byte
-k KB
-m MB
-h 1024
-H 1000
-s 统计目标 /path *.tar.gz
```

### 分区模式

```
MBR - fdisk
主分区不超过4个，单个分区最大2TB
GPT - parted
主分区不超过128个，单个分区最大18EB（几乎没有限制）
```

### fdisk

```
主分区和拓展分区个数不超过4个，拓展分区分为逻辑分区才能使用。
fdisk /dev/sd*
```

### parted

```
select /dev/sd* 切换
mklabel /dev/sd* 指定分区类型
print 显示
print all 显示全部
unit GB (用GB为单位，默认MB)
mkpart 添加分区
mkpart [name] [start -MB] [end -MB]
rm [part num] 删除分区
```

### mkfs

```
格式化
mkfs.[file type] /dev/sd*
mkfs -t [file type] /dev/sd*
```

### swap分区
```
fdisk /dev/sd*
print
n //修改十六进制编码 swap是83
mkswap /dev/sd* 格式化交换分区
swapon /dev/sd* 启用
free 查看使用情况
swapoff /dev/sd* 关闭
```

## 用户和用户组

### 信息储存

```
/etc/group 所有用户组信息
group:x:1:user
组名称：组密码占位符号：组编号：组内用户列表
0 root
1~499 系统预留给软件
500+ 手动

/etc/gshadow 用户组的密码信息
group: * : : user
组名称：组密码：组管理员：组内用户列表


/etc/passwd 所有用户信息
user:x:123:234:xxxxxxxxxxx:/home/user:/bin/bash
用户名：密码占位符：用户编号：组编号：注释信息：主目录：shell类型

/etc/shadow
user:passwd::::
用户：密码（已经加密）
```

### 命令
```
groupadd [name]
gropuadd -g [group-id] [name]
groupmod -n [new-name] [old-name]
groupmod -g [group-id] [name]
groupdel [name]

useradd -g [group-name] [user-name]
useradd -d [home-path] [user-name]
useradd -c [note] [user-name]
useradd -l [new-name] [old-name]
userdel [-r] [user-name]

/etc/nologin 禁止除root用户以外的用户登陆

passwd -l [user-name] 锁定用户
passwd -u [user-name] 解锁用户
passwd -d [user-name] 清除密码

主要组和附属组
gpasswd -a [user-name] [group-name] 添加用户到附属组
gpasswd -d [user-name] [group-name] 删除用户从附属组
newgrp [new group-name] 切换到某个附属组
useradd -g [main-group-name] -G [extra-group-name 1],[extra-group-name 2] 添加用户时指定主要组和附属组
gpasswd [group-name] 改变组密码

su [user-name] 切换用户

whoami 显示当前用户名

id [user-name] 显示用户信息

group [user-name] 显示用户组别信息

chfn [user-name] 设置用户资料

finger [user-name] 显示用户资料
```
