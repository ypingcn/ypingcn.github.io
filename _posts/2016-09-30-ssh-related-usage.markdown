---
layout: post
title:  "初试 ssh 命令"
subtitle: "First try ssh commands"
description: "ssh 连接服务器、远程使用命令、上传文件、下载文件"
date:   2016-09-30 +0800
update: 2021-11-02 23:00 +0800
author:     "ypingcn"
header-img: "img/home-bg-Sm5ceH.webp"
header-mask: 0.3
catalog:    false
tags:
    - 技术
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

