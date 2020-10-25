---
layout: post
title:  "用 Jekyll 在 Github 上搭建一个简易博客"
subtitle: "Build a simple blog using Jekyll and Github"
description: "如果你只是想简单的在 Github 上搭建一个简易的博客，生成静态网页的话，Jekyll 将是一个不错的选择。"
date:   2016-04-04 +0800
update: 2016-10-24 09:36 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    false
tags:
    - 技术
---

如果你只是想简单的在 Github 上搭建一个简易的博客，生成静态网页的话，Jekyll 将是一个不错的选择。

### 安装Jekyll

```shell
sudo apt-get update
```

更新软件包列表。在这一步可以试着把更新源切换到 ubuntu 的官方主服务器，毕竟国内的更新源有延时（不知道这句说的对不对，不对还希望能指出错误）。

```
sudo apt-get install ruby
```

Jekyll 的依赖之一就是 ruby。

```
sudo apt-get install gem
```

官网上的命令是 gem install jekyll ，先安装 gem。

```
gem sources -l
gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
gem sources -u
```

以上几步是更改 gem 的源，使得速度更快。

```
sudo gem install jekyll
```

最后一步，安装成功的话会有下面的提示。

```
Successfully installed jekyll-3.1.2
Parsing documentation for jekyll-3.1.2
Done installing documentation for jekyll after 1 seconds
1 gem installed
```

如果提示缺少什么头文件的话不妨试试一下的操作。

```
ruby -v
ruby 2.1.5p273 (2014-11-13) [x86_64-linux-gnu]
sudo apt-get install ruby2.1-dev
```

最后一步安装的版本号要根据系统返回的已经安装 ruby 的版本号来确定


> 参考

[Jekyll • 简单的博客、静态网站工具](http://jekyll.com.cn)
