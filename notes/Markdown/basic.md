---
layout: page
title:  Markdown 基础语法
description: Markdown 十二个基本语法（标题、引用、斜体、粗体、有序列表和无序列表、链接、图片、删除线、分割线、脚注、代码）
date: 2016-11-10 12:00 +0800
update: 2023-06-04 16:00 +0800
linkeddata: {"@context":"https://schema.org","@type":"NewsArticle","headline":"Markdown 十二个基本语法（标题、引用、斜体、粗体、有序列表和无序列表、链接、图片、删除线、分割线、脚注、代码）","image":["{{site.url}}/img/home-bg.webp"],"datePublished":"2016-11-10T08:00:00+08:00","dateModified":"2021-11-06 00:20 +0800","author":[{"@type":"Person","name":"ypingcn","url":"{{site.url}}/wiki/about/"}]}
---

Markdown 语法可以满足文档的基本需要，是强有力的写作工具。常见的用法如下 

## 标题

在需要作为标题的文字之前加上适当个数的井号 ``` # ```（一个代表一级目录，两个表示二级目录，以此类推，一直支持到六级目录）。

## 引用

加上 ``` > ``` 即可，引用中可以多层嵌套引用。

## 斜体

文字两旁加上``` * ``` ，要与粗体区分开。斜体是一个星号，粗体是两个。

## 粗体

文字两旁加上``` ** ```，注意是两个连续的``` ** ```

## 有序列表

数字后加点再加空格即可，软件就会显示好数字。

## 无序列表

个人比较习惯先加``` - ``` ，再加空格。``` * ``` 和 ``` + ``` 有同样的效果，但都要在后面加上空格后再书写内容

## 链接

有两种方式实现链接

第一种是

```markdown
This is a [website](http://www.google.com)
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
scan this ![QR code](https://example.com/qrcode.png) to continue
```
## 删除线

文字两侧添加``` ~~ ```（两个连续的波浪线）


## 分割线

在空白的一行添加三个连续的``` - ```


## 脚注

就是常见的注释，用法如下

```markdown
hello[^note]
[^note]: another way to say hi
```
## 代码

前后用三个连续的``` ` ```，前后两个可以在同一行，也可以单独占一行。如果是单独占一行的话可以在前一行后面紧跟编程语言名以高亮显示。

---

还有其他更多的用法，例如表格等。

可以下载一个 Typora ，支持上述所有格式，还能 <a href="/notes/Markdown/LaTex-math/" style="font-weight: bold"> 添加数学式子 </a>。


参考资料

<a href="http://wowubuntu.com/markdown/" style="color: #0c82ff;"  target="_blank" rel="noopener nofollow">Markdown 语法说明(简体中文版)</a>

---

**更多阅读**

<div class="row">
    <div class="col-lg-8 col-lg-offset-2
    col-md-10 col-md-offset-1
    post-container">
        <ul class="pager">
            <li class="previous">
                <a href="/notes/Markdown/LaTex-math/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Markdwon + LaTex 表达数学式子》">
                    下一篇<br>
                    <span>《Markdwon + LaTex 表达数学式子》</span>
                </a>
            </li>
            <li class="next">
                <a href="/notes/Markdown/basic/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Markdown 基础语法》">
                    下一篇<br>
                    <span>《Markdown 基础语法》</span>
                </a>
            </li>
        </ul>
    </div>
</div>
