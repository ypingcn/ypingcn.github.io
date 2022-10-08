---
layout: post
title:  "用户权限服务的设计"
subtitle: "user permission service implement for microservices"
description: "简化黑名单、白名单逻辑的用户权限服务的设计"
date:   2022-07-28 +0800
update: 2022-10-08 18:30 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    true
tags:
    - 技术
    - 后端
    - 微服务
---

背景：在实际业务场景中，或多或少都有定制特殊名单的逻辑，这些名单可以用来作为活动的特邀用户，亦或者是禁止特定条件的访问权限。这些名单简单划分可以分为白名单和黑名单，按实际约束条件则是用户白名单、地区白名单等。这些名单可以是手动由特定人员添加，或者是由任务分析后生成的结果。下面以 Tars 服务来实现上述目标，简化权限判断的业务逻辑。

最后的实现如下，主要逻辑是从不同的数据源加载数据，根据配置中指定的逻辑进行组合，最后提供接口给外部系统调用。

该微服务可以简单设计为名单权限的判断，再在其上增加一个服务来满足实际应用中更为复杂的逻辑需要。

### 对外接口设计

FunctionID 是用来区分不同的应用场景。
其他字段可以根据需要拓展。

```protobuffer
struct AuthResult
{
    0 optional int iCode; // 判断的结果
    1 optional string sMessage; // 错误信息（或者其他需要用作提示的信息）
    2 optional int iPermission; // 是否有权限（已经判断了黑名单、白名单的逻辑）
    3 optional int iExpireTimestampSec; // 过期时间（秒级），非 0 则为到对应时间后权限可能发生改变。
};
struct AuthReq
{
    0 optional User tUser; // 用户信息
    1 optional vector<long> vFunctionIDs;
};
struct AuthRsp
{
    0 optional int iCode; // 返回值
    1 optional string sMessage; // 错误信息（如果有）
    2 optional map<long, AuthResult> mResult; // 结果
};
```

### 版本迭代

从头到位，服务的核心逻辑都是从数据库中加载数据到内存中，然后根据配置进行不同的判断返回结果。

#### v1 直接判断

第一版是直接把所有数据库数据从固定的一个表内按 FunctionID 区分后，加载到内存中，接口在处理请求时就上以 FunctionID 为维度的读锁，然后根据配置从请求体中取出数据，与内存中的数据进行比较。根据名单类型返回 iPermission 字段的值。

#### v1.1 从固定的表内加载数据判断

随着单个数据源的增加（某种程度上也有名单维护不合理的原因），每次更新内存中的数据都会因为 SQL 语句执行时间过长（网络传输的数据大），导致服务处理其他请求变慢甚至异常。所以针对数据源的加载问题，做了一点细节优化：

1. 增加分页查询的逻辑，默认以数据库自增 ID 为依据，每次数据库查询限制 2000 条（一个拍脑袋定一下的配置），如果需要可以自行配置 Pagination 和 PageSize 调整此处逻辑。
2. 缩小读写数据时的加锁力度，将原有的全局读写单例改为按 FunctionID 划分的不同读写锁。定时更新数据时只对需要更新的部分进行加锁，尽可能避免影响其他数据的判断逻辑。

#### v1.2 从多变的表内加载数据判断

v1.1 的版本实现里只实现了一个固定语句的查询，形如 ```select xxx from white_list where function_id = xxx``` 的语句直接从管理后台中读取手动更新的配置。随着该服务使用范围的推广，已经慢慢无法满足实际需要。

假设有一份名单是由其他部门根据某些条件定时计算出来的，按原有设计只能是每次到处名单再手动加入管理后台里，费时费力。为了更为灵活的实现数据源加载，对数据库读取的逻辑做了以下优化：

1. 支持自定义配置数据库链接，没有设置则直接使用管理后台的数据库链接。
2. 支持配置需要读取的数据库字段，留空则默认为```udbuserid```。
3. 支持配置需要读取的数据库表名，不再只是原有的 ```white_list``` 和 ```black_list```。
4. 增加开关以便关闭默认的``` function_id =  xxx ``` 查询过滤逻辑。
5. 支持配置```where``` 条件的写法。

实现完本版本后，只需要定时重新读取配置即可避免上述人工操作过程，更加方便地支持```动态+自动化变更```的需要。

#### v1.3 优化数据的管理逻辑

到目前为止，所有的数据都是存放在一个全局的 ```map[string][]string mData``` 中，key 是functionid，value 则是集合，每次请求过来则从一个```map[string]int mFunctionID2FieidID``` 中取出需要请求中的哪个字段，再与 mData 中的集合进行比较。

这种设计无法满足后续对多个字段进行判断的场景，故进行改造。

TODO
