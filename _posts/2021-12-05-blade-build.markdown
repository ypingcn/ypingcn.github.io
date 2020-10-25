---
layout: post
title:  "blade build 在微服务开发中的应用"
subtitle: "blade build in microservice's development"
description: ""
date:   2021-12-05 +0800
update: 2022-01-16 15:17 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    true
tags:
    - 技术
    - 后端
    - 微服务
---

> 本文是对 blade build 结合微服务开发的一篇总结。拖了比较久趁今年年底简单总结下。

## 一 背景

之前的开发流程中的背景如下

1. 微服务开发是使用 C++ 编写，代码编译使用 makefile 组织依赖。
2. 每个服务提供使用``` JCE ```类似于``` Protocol Buffers ```的``` IDL ```（Interface Description Language 接口描述语言）文件来定义接口。编译过程中，makefile 的逻辑中会有一步将该 IDL 转换成框架的调用代码客户端，其他微服务使用该客户端来调用接口。
3. 对外（指提供给非本身的其他微服务）提供调用的时候，需要操作一次 ```make release``` 将 2 中提到的调用客户端发布到开发机的特定公共目录下，如```/home/tafjce/ ```。其他微服务在本服务的 makefile 下引用 ```/home/tafjce``` 的 mk 文件，进行后续的开发。
4. 有些``` IDL ``` 中定义的公共结构体也需要使用 ``` make release ``` 将最新的改动对外发布。
5. 采用``` 主干开发 + 主干发布模式 ```的代码管理模式。


<img src="/img/post/20211205-dev-main-release-main.png" style="width:auto;height:auto;max-width:100%;max-height:100%;" alt="主干开发 + 主干发布模式">

<center><font color="#bfbfbf"> --- 主干开发 + 主干发布模式 --- </font></center>

## 二 弊端

这种流程，在日常开发中的弊端十分明显，特别是在功能迭代频繁，涉及人员众多的情况下。

假设当前服务的拓补图（箭头指向上游）有 A->B->C ， D->B->C。

### 2.1 冲突严重解决路径长

在开发协作的过程中，可能他人的无心之举就能打断你当前的开发。


在当前 ```/home/tafjce/ ``` 目录+``` 主干开发 + 主干发布模式 ```的代码管理模式下，如果有一个人在针对 B 服务的 IDL 进行修改，将无法编译通过的 IDL 发布出去了（```make release``` 不进行实际的编译检查），那么其下游的 A 和 D 服务开发者将无法编译自身服务，链路越长，排查难度越大。且定位到具体的操作人难度大，只能通过文件最后修改人的信息判断。如果是使用管理员权限执行的命令，那么这种定位方法将被直接锁死无法使用。

而且在不恰当的```JCE``` 引用顺序下，有可能导致循环依赖。可能需要一个个到正确的服务下 ``` make release ```。调用方需要处理上游服务的编译依赖问题，实属不合理。

### 2.2 编译频繁

因为 makefile 是以文件名加时间戳来判断文件是否发生变化的。这种情况下，如果上游的 B 服务进行了改动，那么下游的 A、D 服务的调用客户端都会经常发生变动。还会间接影响到下游。

## 三 处理方法

上述的弊端已经严重影响到日常的开发效率，急需改善。

### 3.1 改变代码管理模式

改为```分支开发 + 主干发布模式```模式，将原有的 ``` /home/tafjce ``` 目录移动到版本管理里，做到每次操作可溯源。

<img src="/img/post/20211205-dev-branch-release-main.png" style="width:auto;height:auto;max-width:100%;max-height:100%;" alt="分支开发 + 主干发布模式">

<center><font color="#bfbfbf"> --- 分支开发 + 主干发布模式 --- </font></center>

### 3.2 使用 blade build 处理依赖关系

C++ 的构建和依赖设计一直是饱受诟病的地方，搭配使用 makefile 等方法依旧体验不佳。

blade build 的引入，最明显的效果是依赖管理更加清晰了。遇到循环依赖的情况时，也能很好处理无需人工介入。

## 四 了解 blade build

<a href="https://github.com/chen3feng/blade-build/" target="_blank" rel="noopener nofollow" title="blade build 官方代码仓库">blade build 官方代码仓库</a>
 
blade build （原名 typhoon blade）是腾讯基于 SCons 开源的一套构建系统，主要为 C/C++ 编译设计的。设计思路与谷歌 blaze 有异曲同工之妙，谷歌博客也曾在 <a href="http://google-engtools.blogspot.com/2011/08/build-in-cloud-how-build-system-works.html" target="_blank" rel="noopener nofollow" title="Build in the Cloud: How the Build System works">《Build in the Cloud: How the Build System works》</a>介绍过其中的设计。

> 中文翻译 <a href="https://www.cnblogs.com/Jack47/p/build-in-the-cloud.html" target="_blank" rel="noopener nofollow" title="Google软件构建工具Bazel原理及使用方法介绍">《Google软件构建工具Bazel原理及使用方法介绍》</a>

SCons 是读取目录下的 SConstruct 文件执行构建的。SCons 为构建提供了一系列函数，一个 SConstruct 对应一个 Python 脚本。而在 blade build 中，BUILD 文件就对应 SCons 中的 SConstruct 文件，BUILD 文件同样支持定义构建中的不同函数。

> 2021年7月，新版 blade v2 已经使用 ninja 作为构建后端， SCons 已经不再支持。

横向对比理解 blade 和 scons 两者函数的异同

| SCons | Blade | 备注 |
| :---: | :---: | :---: |
| Command | gen_rule | 自定义需要执行的命令 |
| Depends | deps = [] | 指定依赖关系 |
| Enviroment | 使用 BLADE_ROOT 或者单独 bld 文件定义，需要引入 | 定义需要的参数和环境变量 | 
| Library - SharedLibrary | cc_library + dynamic_link | 动态库，生成 .so |
| Library - StaticLibrar | cc_library + prebuilt = True 或者 prebuilt_cc_library | 静态库，生成 .a |
| Program | cc_binary | 生成可执行文件 |

C++ 的编译流程是预处理，编译和汇编，链接。对于构建系统而言，需要处理好这几点问题，

1. 需要编译的文件范围及其位置。
2. 编译相关参数的设置。
3. 链接相关参数的设置。
4. 依赖关系。

blade build 对于这三点，分别对应

1. 使用 srcs 指定包含的文件，使用 BLADE_ROOT 判断相对位置进而确定具体位置。
2. 搭配 cc_config 中的 cppflags 等设置，详见文档 <a href="https://github.com/chen3feng/blade-build/blob/master/doc/zh_CN/config.md" target="_blank" rel="noopener nofollow" title="blade build 文档  /blade-build/doc/zh_CN/config.md">blade build 文档  /blade-build/doc/zh_CN/config.md</a> 
3. 搭配 cc_config 中的 linkflags 等设置，详见文档 <a href="https://github.com/chen3feng/blade-build/blob/master/doc/zh_CN/config.md" target="_blank" rel="noopener nofollow" title="blade build 文档  /blade-build/doc/zh_CN/config.md">blade build 文档  /blade-build/doc/zh_CN/config.md</a>
4. deps 参数指定依赖的模块。