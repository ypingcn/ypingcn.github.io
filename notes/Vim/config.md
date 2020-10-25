---
layout: page
title:  Vim 配置与快捷键
date: 2017-07-14 15:30 +0800
update: 2022-03-11 20:00 +0800
---

> Vim 配置（显示行号、取消显示行号、高亮搜索结果、语法高亮、自动缩进、制表符改为空格等）


## 配置

这几个都是对应效果的配置，编辑 ```~/.vimrc``` (或者检查下 ```/etc/vim/vimrc``` 或 ```/etc/vimrc``` )文件并保存后，后续打开的文件即可生效。更多进阶级配置可参见：<a href="https://github.com/yangyangwithgnu/use_vim_as_ide" rel="nofollow" style="color: #0c82ff;">https://github.com/yangyangwithgnu/use_vim_as_ide</a> ，该处详细介绍了如何将 vim 配置成 IDE 使用（一般人可能用不到）。

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

参数对应效果解释

 - 显示行号 set nu
 - 取消显示行号 set nonu
 - 高亮搜索结果 set hlsearch
 - 语法高亮 syntax enable
 - 不同语言的自适应缩进 filetype indent on
 - 将制表符拓展为空格 set expandtab
 - 编辑时制表符所占的空格数 set tabstop=4
 - 格式化制表符所占的空格数 set shiftwidth=4

------

## 操作快捷键

几个常用的操作快捷键，如果对基础的操作不熟悉，可以 https://vim-adventures.com/ 上加以练习，这个网站将 vim 操作融入游戏中，寓教于乐。

 - ```yy``` 复制一行
 - ```p``` 粘贴
 - ```x``` 剪切
 - ```xp``` 交换两个字符
 - ```ddp``` 交换相邻两行
 - ```w``` 下一个单词头（包含标点符号） ```W``` 下一个单词头（不包含标点符号）
 - ```e```下一个单词尾（包含标点符号） ```E``` 下一个单词尾（不包含标点符号）
 - ```u```撤销上一步
 - ```.```重复操作

 - ```Ctrl + F``` 向前滚一整屏
 - ```Ctrl + B``` 向后滚一整屏
 - ```H``` 屏幕顶端的行
 - ```M``` 屏幕中央的行
 - ```L``` 屏幕底端的行

 - ```/pattern```往前搜索 pattern 词
 - ```?pattern```往后搜索 pattern 词

 - ```nG``` 转到第n行 不带数字即为最后一行
 - ```n,ms/old/new/ge(c)``` n到m行的old全部替换成new（gec为替换前确认），不带行数即为当前行
 - ```r !command``` 将command的结果插入编辑器

 - ```vim -o3 a.txt b.txt``` 打开（3个水平）多窗口
 - ```:split ```水平多窗口 ```:vsplit``` 竖直多窗口
 - ```tabnew filename``` 新建分页并编辑文件
 - ```tabclose``` 关闭当前分页
 - ```tabonly``` 关闭其他分页
 - ```tabp```切换到上一个分页
 - ```tabn``` 切换到下一个分页
