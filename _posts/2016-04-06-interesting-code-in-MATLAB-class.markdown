---
layout: post
title:  "MATLAB 选修课上的一些有趣的代码"
subtitle: "Interesting code in matlab class"
description: "Matlab 发出不同频率声音的有趣代码"
date:   2016-04-06 +0800
update: 2016-04-06 12:00 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    false
tags:
    - 课程
---

今晚的选修课并不是平时的那个老师上的课，来了一个新老师来替课。

在课堂快结束的时候他分享了一段代码，如下，说是能用 MATLAB 发出不同频率的声音，还开玩笑说能听到频率越高的人越聪明。[微笑脸]。

```
% MATLAB code

a=20000;
b=100;
fs=60000;
t=0:1/fs:1;
for index=1:100
     c=a-b*index;
     d=cos(2*pi*t*c);
     sound(d,fs);
     pause(2);
end
```
在自己的设备上能听到一点声音但是不明显，而且显示的跟上课演示的也不同。

虽然看不懂是什么意思，就暂且记录下来吧。

