---
layout: page
title:  Linux 命令 - find
update: 2018-02-01 15:41 +0800
---

## 基本

find 【搜索位置】 【参数】

```bash
find /home -name abc[cd]
find /home -iname abc 不区分大小写
find /home -user root 按所有者搜索
find /home -nouser 查找没所有者的文件
```
* 匹配任意内容
  ? 匹配任意一个字符
  [] 匹配任意一个中括号内的字符
  如果提示 ``` 路径必须在表达式之前 ```，那就要将表达式用引号包含起来，例如 ``` find /home -name "*.h" ```

```bash
find /home -mtime -10 -size -300k
```
-10 以当天为标志往前10天 到 当天
10 以当天为标准往前10天  的 当天
+10 以当天为标准往前10天 的 之前

-atime [access time] 访问
-ctime [change time] 改变文件属性
-mtime [modify time] 修改文件内容

``` find ./ -perm 775 ```

-perm 按照文件权限找

-follow 倘若find命令遇到符号链接文件，就跟踪至链接所指向的文件。

-size 按文件大小查找
-1k 小于
1k 等于
+1k 大于
k小写 M大写

-inum 查找特定inode节点的文件

-type 按文件类型找

| 参数   | 类型     |
| ---- | ------ |
| b    | 块设备文件  |
| d    | 目录     |
| c    | 字符设备文件 |
| p    | 管道     |
| l    | 符号链接   |
| f    | 一般文件   |

可以联合起来几个条件例如
find /etc -size +100k -a -size -200k -exec ls -lh {} \;
-a and
-o or
-exec ls -lh {} \; 之后同时执行 ls -lh ,  -exec 和 {} \； 配对出现

## 结合 wc 统计行数

> wc 【参数】【文件】

-c 统计字节数。

-l 统计行数。

-m 统计字符数。这个标志不能与 -c 标志一起使用。

> 统计符合条件的文件数

```find ./ -name "*.h" | wc -l```
直接输出答案 

> 统计符合条件的文件的行数 1

```find ./ -name "*.h" -exec wc -l {} \;```

显示文件名和行数，结果示例

```bash
101 ./a.h
80 ./b.h
20 ./c.h
118 ./d.h
91 ./e.h
```

> 统计符合条件的文件的行数 2

``` find ./ -name "*.h" -print0 | xargs -0 wc -l```

效果同上，-print0 是用"\0" 分割结果，xargs -0 是把结果分开。find 默认用 -print 输出，会换行。

可以看二进制显示的结果

```bash
yping@deepin:~/test$ find ./  -name "*.h" -print  |  xxd  -b
00000000: 00101110 00101111 01100001 00101110 01101000 00001010  ./a.h.
yping@deepin:~/test$ find ./  -name "*.h" -print0  |  xxd  -b
00000000: 00101110 00101111 01100001 00101110 01101000 00000000  ./a.h.
```

## 查找当前目录以.c结尾的文件，且文件中包含"hello world"的文件的路径 

```bash
find . -name "*.c" -exec grep "hello world" {} -L \;
```