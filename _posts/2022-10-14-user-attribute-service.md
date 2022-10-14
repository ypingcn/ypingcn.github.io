---
layout: post
title:  "简化开发逻辑的用户属性服务设计"
subtitle: "user attribute service implement for microservices"
description: "简化开发逻辑的用户属性服务设计，支持快速迭代上线减少编写重复代码"
date:   2022-10-14 +0800
update: 2022-10-14 12:00 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    true
tags:
    - 技术
    - 后端
    - 微服务
---

背景：在实际业务场景中，有很多功能是支持用户自行设置决定开启关闭的。针对每个单独的设置分别编写代码是一种重复的劳动，可以把这部分的逻辑抽象出来减少重复开发。同样的服务端针对不同用户也会有不同的业务属性，如果每个属性只会有单一的KV逻辑的话，单独的数据操作代码也可以抽象出来提前封装好。

```protobuffer
// 划分场景
struct UserAttributeBiz
{
    kTEST = 1,
};
struct UserAttributeOpType
{
    kSTRING = 1,// 简单处理字符串类型（直接覆盖）
    kNUMBER = 2,// 简单处理数字类型（直接覆盖）
    kNUMBER_ADD = 3, // 数字类型累加（负数为减）
};
struct UserAttribute
{
    0 optional string sKey;
    1 optional string sStrValue;   // 字符串类型值，默认为空
    2 optional long lNumValue;              // 数字类型值，默认为0
    3 optional long lTimestampSec; // 最后更新时间，设置时都不填
    // 如无必要，客户端调用设置接口时不支持、不设置以下后续字段
    4 optional int iOpType = 0;           // see alse @UserAttributeOpType
    5 optional int iHasOldStrValue = false; // 是否有旧值，SET/DEL 的时候填值将作为条件，GET 暂时用不到
    6 optional string sOldStrValue;
    7 optional long lExpireTimestamp = 0; // 失效时间（时间戳），设置时都不填
};
```

TODO
