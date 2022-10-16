---
layout: post
title:  "Firefox Quantum 引发的思考"
subtitle: "Firefox Quantum and related discussion"
description: "Firefox Quantum 在 2017 年 11 月 14 日发布，最大的变化是自家的 Rust 编写 CSS 引擎，扩展仅支持 WebExtension 格式。明显感受到的打开网站的速度有所提高"
date:   2017-11-21 +0800
update: 2022-10-16 00:20 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    false
tags:
    - 火狐
    - 讨论
---

Firefox 57 (Firefox Quantum)版在2017年11月14日发布，这个版本最大的变化在于用了自家的 Rust 编写 CSS 引擎，扩展仅支持 WebExtension 格式。最近几天的使用下来，能明显感受到的变化在于速度，打开网站的速度有所提高。偶尔对于不经常访问的网站会在 HTTPS 握手部分卡住，占用较长的一段时间。至于拓展方面，影响倒不是很大，能有广告过滤（<a href="https://ypingcn.com/go/out?r=ublock-origin-firefox" rel="nofollow" style="color: #0c82ff;">uBlock Origin</a>）、切换 UA（<a href="https://ypingcn.com/go/out?r=user-agent-switcher-revived" rel="nofollow" style="color: #0c82ff;">User-Agent Switcher</a> ）、切换代理（<a href="https://ypingcn.com/go/out?r=smartproxy" rel="nofollow" style="color: #0c82ff;">SmartProxy</a>）三类拓展就足够了，主题倒不是什么核心需求，不改也罢。

新版本出来的时候在一个群聊里发了张图片和链接，算是一种推广。一如既往的安静，反倒是一句“火狐给了你多少钱”有了以下片段的想法。

小学六年级开始接触电脑（现在看来这并不是个多早的时间了），两年后家里也有了自己的台式机，那时候用的浏览器还是搜狗浏览器，冲着各种网页加速的宣传用的，效果也算明显。其他浏览器也断断续续地用过一段时间，但终究不喜欢那些所谓体贴的功能，可能是我对于这些功能的需求没有那么强烈吧。个人对于浏览器有几个小要求，一是新建标签页或者启动页不要带新闻流或者推广（所以 UC 之类的是不用的，手机也是一样的要求），二是默认安装后的链接不要带有各类推广小尾巴（自从发现搜狗浏览器访问 hao123 之类的网站会跳转到自家的网站导航之后就再也不用了）。这样看来只有 Chrome 和 Firefox比较符合了（Firefox 国内版也被加了例如微信、二维码的功能，所以现在用 Firefox 还是习惯到 Mozilla 官网或者 FTP 上下载），最终现在用 Firefox 更多是因为同步功能。Firefox 和其他浏览器一样都带有同步功能，同步浏览器设置、拓展、书签等，Chrome 也有同步功能但是不能直接访问。

还有一点的是 Chrome 背后是做搜索起家的 Google ，一家擅长收集数据的公司和一家非盈利组织，在浏览器的选择上，我选择后者。现在如果为了网络上的便利，个人总是要失去点什么，但是可以避免无谓的损失。

同时 Firefox 是开源产品，对于开源产品总想多支持一下。个人开源我想更多为了获得其他人的认可，公司组织层面开源是对自家产品的信心。

对于 Mozilla 的宣传，至少在对 Firefox 浏览器的宣传上，我是不太同意的。Mozilla 的宣传总有点政治正确的味道。之前有段时间在下载页显示“最后一款独立的浏览器”，这句话我觉得对于追求实用性的用户来说并没有多大的吸引力。 

Firefox 现在还只是新版本的第一代，还有着很多各种各样的问题，祝愿能变得越来越好用，份额再多一点吧。

> 一些断断续续的想法