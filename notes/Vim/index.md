---
layout: page
title:  Vim 自用配置与快捷键
update: 2017-07-14 15:30 +0800
---

> Vim 配置（显示行号、取消显示行号、高亮搜索结果、语法高亮、自动缩进、制表符改为空格等）

```vim
set nu
set nonu
set hlsearch
syntax enable
filetype indent on
set expandtab
set tabstop=4
set shiftwidth=4
```

显示行号 set nu

取消显示行号 set nonu

高亮搜索结果 set hlsearch

语法高亮 syntax enable

不同语言的自适应缩进 filetype indent on

将制表符拓展为空格 set expandtab

编辑时制表符所占的空格数 set tabstop=4

格式化制表符所占的空格数 set shiftwidth=4

vim   ~/.vimrc

> 更多配置可参见：https://github.com/yangyangwithgnu/use_vim_as_ide

---

yy 复制一行

p 粘贴

x 剪切

xp 交换两个字符

ddp 交换相邻两行

w 下一个单词头（包含标点符号） W 下一个单词头（不包含标点符号）

e 下一个单词尾（包含标点符号） E 下一个单词尾（不包含标点符号）

u 撤销上一步

. 重复操作


Ctrl + F 向前滚一整屏

Ctrl + B 向后滚一整屏

H 屏幕顶端的行

M 屏幕中央的行

L 屏幕底端的行


/pattern  往前搜索 pattern 词

?pattern  往后搜索 pattern 词


nG 转到第n行 不带数字即为最后一行

n,ms/old/new/ge(c) n到m行的old全部替换成new（gec为替换前确认），不带行数即为当前行

r !command 将command的结果插入编辑器

vim -o3 a.txt b.txt 打开（3个水平）多窗口

:split 水平多窗口 :vsplit 竖直多窗口

`` 回到上一个位置

tabnew filename 新建分页并编辑文件

tabclose 关闭当前分页

tabonly 关闭其他分页

tabp 切换到上一个分页

tabn 切换到下一个分页


