---
layout: page
title:  Markdown 基础语法
update: 2016-11-10 12:00 +0800
---

Markdown 十二个基本语法（标题、引用、斜体、粗体、有序列表和无序列表、链接、图片、删除线、分割线、脚注、代码）

参考资料

[Markdown 语法说明(简体中文版)](http://wowubuntu.com/markdown/)

## 标题

在需要作为标题的文字之前加上适当个数的``` # ```（一个代表一级目录，以此类推，到六级目录

## 引用

加上 ``` > ``` 即可，引用中可以多层嵌套引用

## 斜体

文字两旁加上``` * ``` ，要与粗体区分开

## 粗体

文字两旁加上``` ** ```，注意是两个连续的``` ** ```

## 有序列表

数字后加点再加空格即可

## 无序列表

个人比较习惯先加``` - ``` ，再加空格。``` * ``` 和 ``` + ``` 有同样的效果，但都要在后面加上空格后再书写内容

## 链接

有两种方式实现链接

第一种是

```markdown
This is a [website](http://www.baidu.com)
```

第二种是

```markdown
I like [Firefox][1] and [Chromium][2]

[1]:[https://www.mozilla.org/zh-CN/firefox/]
[2]:[https://www.chromium.org]
```

第一种便于撰写，但第二种明显方便管理链接

## 图片

图片跟链接很像，而且都有两种形式，区别是要在最前面加感叹号

例如

```markdown
scan this ![QR code](https://img3.doubanio.com/f/sns/1cad523e614ec4ecb6bf91b054436bb79098a958/pics/sns/anony_home/doubanapp_qrcode.png) to continue
```
## 删除线

文字两侧添加``` ~~ ```（两个连续的波浪线）


## 分割线

在空白的一行添加三个连续的``` - ```


## 脚注

```markdown
hello[^note]
[^note]: another way to say hi
```
## 代码

前后用三个连续的``` ` ```，前后两个可以在同一行，也可以单独占一行。如果是单独占一行的话可以在前一行后面紧跟编程语言名以高亮显示。

---

还有其他更多的用法，例如表格等。

可以下载一个 Typora ，支持以上的所有格式，还能添加数学式子。
