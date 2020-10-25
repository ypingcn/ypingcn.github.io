---
layout: page
title:  【转】redis.conf 配置文件
update: 2017-09-17 11:22 +0800 
---

Redis配置文件redis.conf 详解

1.基本配置

内存单位的表示

```
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
```

单位中不区分大小写1GB 1Gb 1gB是一样的

后台运行，yes是后台运行，no前台运行，将输出，输出到终端（默认）

daemonize yes

如果daemonize参数为yes的话就会产生pid文件，一下是pid文件的定义

pidfile /usr/local/redis-master/run/redis.pid

监听的端口

port 6379

绑定监听的IP地址

bind 127.0.0.1

如果在本地调用redis可以直接用sock文件

unixsocket /tmp/redis.sock  //sock文件的位置

unixsocketperm 755            //sock文件的权限

如果一个链接在N秒内是空闲的，就将其关闭

timeout 0

如果对方down了或者中间网络断了发送ACK到客户端在指定的时间内没有收到对方的回应就断开TCP链接（时间单位秒记），此参数会受到内核参数的影响，推荐配置60。

tcp-keepalive 0

指定输出消息的级别

```
# debug (调试级别，详细信息，信息量大)
# verbose (详细信息，信息量较大)
# notice (通知，生产环境推荐)
# warning (错误信息警告信息)
```

loglevel notice

日志输出文件，默认在前端运行的时候此key的默认值是stdout输出到终端，如果用守护进程运行此key的stdout的时候将日志输入到/dev/null，如果想记录日志，就必须为其指定logfile位置

logfile /var/log/redis.log

将日志记录的哦syslog

syslog-enabled no

指定syslog的身份

syslog-ident redis

指定syslog的级别，必须是LOCAL0-LOCAL7之间

syslog-facility local0

设置数据库的数量

databases 16

设置数据库的数量。默认数据库DB 0，你可以选择一个不同的per-connection的使用SELECT<dbid>这儿的DBID是一个介于0和'databases'-1

databases 16

2.快照配置

将DB保存到磁盘的规则定义（快照）

格式：save <seconds> <changes>

例子：save 900 1  //在900秒（15分钟）内如果至少有1个键值发生变化  就保存

save 300 10  //在300秒（6分钟）内如果至少有10个键值发生变化  就保存 
save 900 1                      //每一条表示一个存盘点
save 300 10
save 60 10000

如果启用如上的快照（RDB），在一个存盘点之后，可能磁盘会坏掉或者权限问题，redis将依然能正常工作

stop-writes-on-bgsave-error yes

是否将字符串用LZF压缩到.rdb 数据库中，如果想节省CPU资源可以将其设置成no，但是字符串存储在磁盘上占用空间会很大，默认是yes

rdbcompression yes

rdb文件的校验，如果校验将避免文件格式坏掉，如果不校验将在每次操作文件时要付出校验过程的资源新能，将此参数设置为no，将跳过校验

rdbchecksum yes

转储数据的文件名

dbfilename dump.rdb

redis的工作目录，它会将转储文件存储到这个目录下，并生成一个附加文件

dir /usr/local/redis-master/db

3.主从参数
如果本地是salve服务器那么配置该项

```
# slaveof <masterip> <masterport>
```
slaveof 127.0.0.1 65532

master的验证密码

masterauth <master-password>

当从主机脱离主的链接时，如果此值为yes当客户端查询从时，回响应客户端，如果是第一次同步回返回一个日期数据或这空值，如果设置为no，则返回“SYNC with master in progress”到INFO and SLAVEOF

slave-serve-stale-data yes

从服务器只读（默认）

slave-read-only yes

从发送ping到主的时间间隔(单位：秒)

repl-ping-slave-period 10

批量传输I / O超时和主数据或ping响应超时 默认60s 必须大于repl-ping-slave-period值

repl-timeout 60

此选项如果是“yes”那么Redis的使用数量较少的TCP数据包和更少的带宽将数据发送到，在从主机上延迟40毫秒（linux kernel中的40毫秒）出现。如果是no将在slave中减少延迟，但是流量使用回相对多一些，如果用多个从主机，此处建议设置成yes

repl-disable-tcp-nodelay no

从主机的优先级，如果当主主机挂了的时候，将从从主机中选取一个作为其他从机的主，首先优先级的数字最低的将成为主，0是一个特殊的级别，0将永远不会成为主。默认值是100.

slave-priority 100

4.安全配置
密码本机，如果别人要求链接需要其验证

requirepass password

 

命令重命名，如果更改命令可能在从服务器上出现问题

例如：rename-command CONFIG b840fc02d524045429941cc15f59e41cb7be6c52 //将config命令命名成b840fc02d524045429941cc15f59e41cb7be6c52

rename-command CONFIG "" //默认是空的

 

5.极限
客户端链接的最大数量

maxclients 10000

 

最大内存的使用 如果是主从的话，此值应该设置更低

maxmemory <bytes>

 

redias达到maxmemory时，如何删除k&y

volatile-lru -> 用lru算法删除过期的键值

allkeys-lru -> 用lru算法删除所有键值

volatile-random -> 随机删除过期的键值

allkeys-random -> 随机删除任何键值

volatile-ttl -> 删除最近要到期的键值（监控TTL）

noeviction -> 不会写操作，返回一个错误

At the date of writing this commands are: set setnx setex append incr decr rpush lpush rpushx lpushx linsert lset rpoplpush sadd sinter sinterstore sunion sunionstore sdiff sdiffstore zadd zincrby zunionstore zinterstore hset hsetnx hmset hincrby incrby decrby getset mset msetnx exec sort

默认值例子如下：

maxmemory-policy volatile-lru

 


LRU和最小的TTL算法是不准确，在几个中挑几个来检查近期用的最少的键值删除，为了节约内存可以设置小点。

maxmemory-samples 3

 


6.append only

启用AOF和RDB持久性，如果又一个或者多个写入点时，在写入点和写入点之间的时间里所有add的键值回丢失，如果启用此特性，redis会将add的值先写入到附加文件中，此参数默认就是启用这个特性。

appendonly no

 

OAF文件的文件名

appendfilename appendonly.aof

 

 

append only文件名是由 appendfilename appendonly.aof项来定义的，redias将数据立刻些如到AOF文件中时，有三种方式：

no: 让OS来刷新数据 快

always:每次写入后调用函数FSYNC进行写入 最安全的

everysec: 每一秒进行调用FSYNC进行写入

默认值：appendfsync everysec

 


如果磁盘性能问题比较慢，将其设置为yes，磁盘I/O比较宽裕则设置为no数据比较安全。

no-appendfsync-on-rewrite no

 


OAF文件的写规则

如下：如果达到64M的百分之百就停止写入

auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

 


7.LUA SCRIPTING
执行一个LUA脚本时的最大时间，防止死循环等等，设置为0是没有限制，单位为秒

lua-time-limit 5000

 


8.redias的慢查询记录
如果大于如下值的执行命令进行记录，默认是10000，单位是微妙（1000000微秒 == 1秒），设置为一个负数时，警用此记录，设置为0时，记录任何执行命令

slowlog-log-slower-than 10000

 


此值的大小会影响内存的大小，回收内存可以用SLOWLOGRESET

slowlog-max-len 128

 


9.高级配置
Hash编码使用高速内存数据结构的条目阈值

如果redisObject的type 成员值是 REDIS_LIST 类型的,则当该list 的 elem数小于配置值: hash-max-ziplist-entries 或者elem_value字符串的长度小于 hash-max-ziplist-value, 则可以编码成 REDIS_ENCODING_ZIPLIST 类型存储,以节约内存. 否则采用 Dict 来存储.


hash-max-ziplist-entries 512
hash-max-ziplist-value 64

 

 

 

相同哈希值的列表可以用特殊的表示方式存储，以节约空间，阈值设置如下

如 type 是 REDIS_LIST 类型的,如果其 entry 小于配置值: list-max-ziplist-entries 或 value字符串的长度小于 list-max-ziplist-value，则可以编码成 REDIS_ENCODING_ZIPLIST 类型存储,以节约内存; 否则采用 REDIS_ENCODING_LINKEDLIST 来存储


list-max-ziplist-entries 512
list-max-ziplist-value 64

```
# Sets have a special encoding in just one case: when a set is composed
# of just strings that happens to be integers in radix 10 in the range
# of 64 bit signed integers.
# The following configuration setting sets the limit in the size of the
# set in order to use this special memory saving encoding.
```

如 type 是 REDIS_SET 类型的,如果其值可以表示成数字类型且 entry 小于配置值set-max-intset-entries, 则可以编码成 REDIS_ENCODING_INTSET 类型存储,以节约内存; 否则采用 Dict类型来存储
set-max-intset-entries 512

相同的hash列表中，排序列表的元素和长度都不能高于如下值

zset-max-ziplist-entries 128
zset-max-ziplist-value 64

 


重建hash表的时候如果内存不足 如果此值设置为no则延时，如果为yes则尽快释放内存。

activerehashing yes

 


客户端buffer限制，如果达到硬限制则立刻断开

三种客户端
```
# normal -> 正常客户端
# slave -> 从客户端或者监控客户端
# pubsub -> 订阅或者发布客户端
```

客户端限制的语法如下

client-output-buffer-limit <class> <hard limit> <soft limit> <soft seconds>

默认如下

client-output-buffer-limit normal 0 0 0
client-output-buffer-limit slave 256mb 64mb 60 //slave客户端 buffer硬限制为256M，软限制为64MB/60秒 就断开连接
client-output-buffer-limit pubsub 32mb 8mb 60

 

 

一个任务可以使用的cpu数目

hz 10

 


10.配置文件include
例子：
```
# include /path/to/local.conf
# include /path/to/other.conf
```