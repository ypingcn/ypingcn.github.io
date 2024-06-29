---
layout: post
title:  "简化开发逻辑的用户属性服务设计"
subtitle: "User attribute service implement for microservices"
description: "简化开发逻辑的用户属性服务设计，支持快速迭代上线减少编写重复代码"
date:   2022-10-14 +0800
update: 2022-11-03 20:30 +0800
author:     "ypingcn"
header-img: "img/home-bg-Sm5ceH.webp"
header-mask: 0.3
catalog:    true
tags:
    - 技术
    - 后端
    - 微服务
---

## 一、背景

在实际业务场景中，有很多功能是支持用户自行设置决定开启关闭的。针对每个单独的设置分别编写代码是一种重复的劳动，可以把这部分的逻辑抽象出来减少重复开发。

同样的服务端针对不同用户也会有不同的业务属性，如果每个属性只会有单一的KV逻辑的话，单独的数据操作代码也可以抽象出来提前封装好。

## 二、接口设计

数据管理上用 UID+Biz 为主键，用户传入的 KEY 为二级主键进行数据管理。

最终的接口设计如下，主要是实现增删改查接口，增和改接口合并为 SET 接口支持同时处理两类。所有接口支持弱条件过滤，SET 接口支持判断旧值符合要求后再更新。

设计对内接口和对外接口，以便对用户权限进行约束管理。

```protobuffer
    // 划分场景
    struct UserAttributeBiz
    {
        kTEST = 1,
    };
    // 操作类似
    struct UserAttributeOpType
    {
        kSTRING = 1,     // 简单处理字符串类型（直接覆盖）
        kNUMBER = 2,     // 简单处理数字类型（直接覆盖）
        kNUMBER_ADD = 3, // 数字类型累加（负数为减）
    };
    // 属性值
    struct UserAttribute
    {
        0 optional string sKey;
        1 optional string sStrValue;   // 字符串类型值，默认为空
        2 optional long lNumValue;     // 数字类型值，默认为0
        3 optional long lTimestampSec; // 最后更新时间，设置时都不填
        // 如无必要，客户端调用设置接口时不支持、不设置以下后续字段
        4 optional int iOpType = 0;             // see alse @UserAttributeOpType
        5 optional int iHasOldStrValue = false; // 是否有旧值，SET/DEL 的时候填值将作为条件，GET 暂时用不到
        6 optional string sOldStrValue;
        7 optional long lExpireTimestamp = 0; // 失效时间（时间戳），设置时都不填
    };
    // 获取接口
    struct GetUserAttributeReq
    {
        0 optional User tUser;
        1 optional int iBiz = 0;
        2 optional vector<string> vKeys; // 服务端留空则为获取全部。客户端禁止留空
    };
    struct GetUserAttributeRsp
    {
        0 optional int iCode;
        1 optional string sMessage;
        2 optional vector<UserAttribute> vItems;
    };
    // 设置接口
    struct SetUserAttributeReq
    {
        0 optional User tUser;
        1 optional int iBiz = 0;
        2 optional vector<UserAttribute> vItems;
        3 optional int iCheckKey = 1; // 检查 key 是否符合配置的内容。服务端有效，客户端必须开启。
        4 optional int iFetchNew = 0; // 返回更新后的最新值
    };

    struct SetUserAttributeRsp
    {
        0 optional int iCode;
        1 optional string sMessage;
        2 optional vector<UserAttribute> vItems;
    };
    // 删除接口
    struct DelUserAttributeReq
    {
        0 optional User tUser;
        1 optional int iBiz = 0;
        2 optional vector<UserAttribute> vItems; // 留空则删除全部
        3 optional int iCheckKey = 1;            // 检查 key 是否符合配置的内容
    };
    struct DelUserAttributeRsp
    {
        0 optional int iCode;
        1 optional string sMessage;
        // TODO 返回删除条数??
    };
```

同样结合之前博客提到的缓存应用，对于一致性要求不高的场景可以再封装一层合并查询+缓存的中间组件，提供给业务进行调用。组件实现的缓存 KEY 可以定义为 UID+BIZ+KEY 三个维度，多个 KEY 则拆分为不同缓存对象。

实际应用上，直播及其相关场景中缓存组件能有 15% 到 60% 不等的命中率，削峰效果良好。

## 三、优化点

1. 力度更小的限制，目前实现的逻辑只实现了哪些业务 ID 的值对外开放 + 限制 KEY 的取值，没有约束 VALUE 的取值。
2. 支持更多灵活的 KV 取值判断逻辑，例如正则等。
3. 支持配置 KEY 在没有设置的时候返回默认值，不再默认返回空值。
4. 底层数据存储支持按不同的业务 ID 存储到不同的地方，实现底层数据隔离与安全，也方便在不同业务中的快速部署和迁移。
