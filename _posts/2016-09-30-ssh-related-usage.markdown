---
layout: post
title:  "ssh 命令行相关"
subtitle: "Commands relating to ssh"
description: "ssh 连接服务器、远程使用命令、上传文件、下载文件"
date:   2016-09-30 +0800
update: 2016-09-30 12:00 +0800
author:     "ypingcn"
header-img: "img/bg.jpg"
header-mask: 0.3
catalog:    true
tags:
    - Tech
---

ssh 连接服务器

```
ssh username@host
```

远程使用命令( ls 为例)

```
ssh username@host command ls
```

上传文件

```
scp /local-path/file username@host:/romote-path
```

下载文件

```
scp username@host:/romote-path /local-path
```

