---
layout: post
title:  "用 Jekyll 在 Github 上搭建一个简易博客"
subtitle: "Build a simple blog using Jekyll and Github"
description: "如果你只是想简单的在 Github 上搭建一个简易的博客，生成静态网页的话，Jekyll 将是一个不错的选择。"
date:   2016-04-04 +0800
update: 2022-06-27 10:11 +0800
author:     "ypingcn"
header-img: "img/home-bg-Sm5ceH.webp"
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

遇到类似的报错就是缺少相关头文件，需要再安装一个相关的依赖``` ruby2.*-dev ```。

```
Building native extensions. This could take a while...
ERROR:  Error installing jekyll:
        ERROR: Failed to build gem native extension.

    current directory: /var/lib/gems/2.7.0/gems/http_parser.rb-0.8.0/ext/ruby_http_parser
/usr/bin/ruby2.7 -I /usr/lib/ruby/2.7.0 -r ./siteconf20220627-4252-dpxce9.rb extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

You might have to install separate package for the ruby development
environment, ruby-dev or ruby-devel for example.

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.7.0/gems/http_parser.rb-0.8.0 for inspection.
Results logged to /var/lib/gems/2.7.0/extensions/x86_64-linux/2.7.0/http_parser.rb-0.8.0/gem_make.out
```

最后一步安装的版本号要根据系统返回的已经安装 ruby 的版本号来确定，例如返回 2.1 就要安装 ```ruby2.1-dev```，版本号是2.7 就要安装 ```ruby2.7-dev```

```
ruby -v
ruby 2.1.5p273 (2014-11-13) [x86_64-linux-gnu]
sudo apt-get install ruby2.1-dev

ruby 2.7.0p0 (2019-12-25 revision 647ee6f091) [x86_64-linux-gnu]
sudo apt-get install ruby2.7-dev
```




> 参考

[Jekyll • 简单的博客、静态网站工具](http://jekyll.com.cn)
