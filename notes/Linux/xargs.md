---
layout: page
title:  Linux 命令 - xargs
update: 2018-03-25 00:05 +0800
---

## 基本

xargs [option]

## 例子

> cat example.txt | xargs

多行输入单行输出

> cat example.txt | xargs -n3

多行输入多行输出

> echo "test/test/test" | xargs -d/
> test test test

自定义分隔符

> find -mtime -7 | xargs -I {} cp {} ~/test

自定义替换符号(把七天内修改的文件复制到 ~/test 里)

