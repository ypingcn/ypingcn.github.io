---
layout: page
title:  Librewolf 浏览器（基于火狐浏览器）的资源汇总（2022年）
date: 2022-04-24 13:40 +0800
update: 2022-04-24 13:40 +0800
---

Librewolf，字面意思即【自由之狼】。Librewolf 浏览器是一款基于 Mozilla Firefox 浏览器定制，旨在为普通用户提供安全和隐私相关设置调整、开箱即用的优秀浏览器。它同样支持 Windows、MacOS、Linux 等多个平台

它有以下的几个特点适合普通用户使用：

1. 默认内置安装 uBlock Origin 以阻止脚本/广告，保护隐私和安全。
2. 没有 “添加到 Pocket” 按钮，减少了被推广的机会。
3. 默认不启用火狐账户进行云同步，但需要时可以手动开启。

对于在意上网安全的用户，它做了以下几点的改动：

1. 移除浏览器内置的遥测功能，不会再与 ```*.telemetry.mozilla.org``` 等相关域名交互上报用户行为数据。
2. 追踪保护默认设置为“严格”模式，默认就是屏蔽【社交媒体跟踪器、所有窗口中的跨网站 Cookie（包括跟踪性 Cookie）、所有窗口中的跟踪性内容、加密货币挖矿程序和数字指纹跟踪程序】
3. 默认启用 HTTPS-only 模式。在访问非 HTTPS 的网站时会提醒用户，不会直接默认展示。
4. 默认内置私密搜索供应商，如 Searx、Qwant（DuckDuckGo 被设置为默认搜索引擎）。但对于普通用户而已这几个搜索引擎访问没有日常使用的百度谷歌好，所以在需要时候，需要访问相关地址，在搜索栏或地址栏里手动添加回去。
5. 支持伪造虚假的屏幕分辨率、时区、语言等，使得网站更难获取用户的环境参数。更多浏览器的隐私保护效果测评，可以访问 <a href="https://privacytests.org/" rel="nofollow" style="color: #0c82ff;">https://privacytests.org/ </a> 获取更多测评细节。

## 安装

Librewolf 浏览器官网是 <a href="https://librewolf.net/" rel="nofollow" style="color: #0c82ff;">https://librewolf.net/</a>，点击首页 Installation 的蓝色按钮即可跳转到对应平台的下载页面

Librewolf 浏览器 Windows 安装包下载地址：<a href="https://librewolf.net/installation/windows/" rel="nofollow" style="color: #0c82ff;">https://librewolf.net/installation/windows/</a>

Librewolf 浏览器 MacOS 安装包下载地址：<a href="https://librewolf.net/installation/macos/" rel="nofollow" style="color: #0c82ff;">https://librewolf.net/installation/macos/</a>