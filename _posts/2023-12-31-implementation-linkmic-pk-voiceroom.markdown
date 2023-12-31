---
layout: post
title:  "连麦、PK和语音房的实现设计思路"
subtitle: "implementation of linkmic pk and voice room"
description: "连麦、PK和语音房的实现设计思路记录"
date:   2023-12-31 +0800
update: 2023-12-31 16:30 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    true
tags:
    - 技术
    - 后端
    - 微服务
---

> 本文意在对已有功能实现的总结和思考，对比中思考改进点

连麦 PK 是秀场直播中的一个重要核心玩法。而语音房同样包含众多的连麦操作，故在此对这三类场景总结一下相同点与不同点。