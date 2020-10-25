---
layout: page
title:  Linux 命令 - awk
update: 2018-03-23 15:00 +0800
---

awk 可以简单地格式化输出。

awk 将输入的每一行先按制定的分隔符分隔开（如果有），然后根据是否符合 pattern 决定执行 commands 部分，pattern 可以是正则。

## 基本

```bash
awk [option] 'BEGIN{ print "start" } pattern{ commands } END{ print "end" }' file
awk [option] -f command_file_name file
```

commands 里的```print $1"+"$2 ``` 意味着输出分隔开的第一部分和第二部分，两者用加号连接。$0 是整个部分。

## 参数

| 参数            | 含义                                  |
| ------------- | ----------------------------------- |
| -F            | 指定分隔符                               |
| -f [filename] | 从文件中加载命令``` awk -f awk_file file``` |

## 内置变量

| 名称       | 含义               |
| -------- | ---------------- |
| ARGC     | 命令行参数个数          |
| ARGV     | 命令行参数排列          |
| ENVIRON  | 支持队列中系统环境变量的使用   |
| FILENAME | awk处理的文件名        |
| NF       | 浏览记录的域的个数（理解为列数） |
| NR       | 已读的记录数（理解为行数）    |

## 其他

同样有 C 语言里的 if、if/else、if/else if/else、while、do/while、for、break、continue

## 例子

### 计数

```bash
awk 'BEGIN{cnt=0} {cnt++} END{print "count is "cnt}' filename
```

### 遍历列表

```bash
awk -F ':' 'BEGIN {count=0;} {name[count] = $1;count++;}; END{for (i = 0; i < NR; i++) print i, name[i]}' /etc/passwd
```

