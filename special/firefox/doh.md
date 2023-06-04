---
layout: page
title: 如何在 Firefox 火狐浏览器上设置并启用基于 HTTPS 的安全 DNS（DoH）
date: 2022-10-16 10:20 +0800
update: 2023-06-04 14:50 +0800
---

每个网站都需要知道IP地址才能正确访问，但是 IP 地址太多不可能每个都记录下来，需要有一个方式来给用户使用，这就是域名系统 DNS（Domain Name System）的来由。DNS 是指将地址栏中的地址转换成具体网络IP地址的一个协议，但因其设计没有考虑相关的安全性导致其容易被第三方劫持进而修改结果。

而安全 DNS （DNS-over-HTTPS，简称 DoH ）DoH 代表“DNS over HTTPS”，是一种通过 HTTPS 协议进行 DNS 请求和响应的加密通信方式。传统的 DNS 通信使用的是明文UDP协议，易受到窃听、篡改等攻击，而 DoH 可以加密 DNS 流量，从而提高了安全性和隐私保护。使用 DoH 还可以避免某些网络中间人（例如公共 Wi-Fi）对 DNS 流量进行劫持和污染，从而提高了访问互联网服务的可靠性。越来越多的浏览器和操作系统开始支持DoH，以提高用户的在线安全和隐私保护。

下面是在 Firefox 火狐浏览器使用 DoH 的一些设置教程和注意事项。

------

### 一、启用或禁用 DNS-over-HTTPS

#### 版本号 115 以下的版本

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在“常规”面板中（第一个菜单，about:preferences#general），向下滚动到“网络设置”部分，然后点击 设置 按钮。
3. 在打开的对话框中，向下滚动到底， 找到 启用 HTTPS over DNS 勾选框，需要时则勾选，反之则取消勾选。
4. 选择对应的供应商提供的地址，或者自行输入需要的地址（本文下一章有推荐整理）。

#### 版本号 115 以及以上的版本

> 115版本计划预期在 2023-07-04 发布

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在“隐私与安全”面板中（第四个菜单，about:preferences#privacy），向下滚动到“基于 HTTPS 的 DNS”部分。
3. 在“安全 DNS 使用策略”部分，选择增强保护（DoH失败后尝试使用系统DNS）或者最大保护（仅使用DoH）。
4. 选择对应的供应商提供的地址，或者自行输入需要的地址（本文下一章有推荐整理）。

------

### 二、DoH 供应商

除了浏览器自带的供应商外，还有很多其他选择。

#### 2.1 Alidns

阿里云提供的服务，在国内效果好，但不支持广告过滤等功能。 ```https://dns.alidns.com/dns-query```

#### 2.2 DNSPod

腾讯云出品，在国内效果好，注册帐号后支持设置广告过滤等，但支持的过滤规则不多，效果弱。 ```https://dns.pub/dns-query```

#### 2.3 AdGuard

>（网络原因不太推荐在国内网络条件下使用）

老牌广告过滤商，注册帐号后支持设置广告过滤等自定义内容。

默认 （屏蔽广告、追踪器）```https://dns.adguard.com/dns-query```

家庭保护（屏蔽广告、追踪器、成人内容，并在可能的情况下启用安全搜索和安全模式。) ```https://dns-family.adguard.com/dns-query```

无过滤 ```https://unfiltered.adguard-dns.com/dns-query```

#### 2.4 NextDNS

>（网络原因，不太推荐在国内网络条件下使用）

去广告 DNS 服务商，每月可免费查询 300,000 次，同时支持 DoH 、DoT 等方式。<a href="https://ypingcn.com/go/out?r=nextdns" target="_blank" rel="noopener nofollow" style="color: #0c82ff;" title="NextDns">【注册】</a>

支持的广告过滤规则多，过滤效果较好。但因其服务在海外，网站解析的结果大部分为海外版，一定程度上会影响网站浏览体验。

#### 2.5 Cloudflare

老牌网络服务提供商，且内置在火狐浏览器中。

默认 ```https://cloudflare-dns.com/dns-query```

火狐版 ```https://mozilla.cloudflare-dns.com/dns-query```

屏蔽病毒程序 ```https://security.cloudflare-dns.com/dns-query```

屏蔽病毒程序和成人内容 ```https://family.cloudflare-dns.com/dns-query```

------

### 三、排除特定域名

1. 在 地址栏 里输入```about:config```，然后按回车访问。
2. 有时会出现警告页面。点击```我接受此风险，请继续！```接受相关修改风险并继续，以便打开```about:config```页面。
3. 搜索```network.trr.excluded-domains```，如果搜索不到则需要新建一个。
4. 点击其旁边的 修改 按钮。
5. 将域名添加到列表中，如果是多个域名则需要用逗号分割。编辑完成后点击复选保存更改，即可生效。 
