---
layout: page
title: 如何在 Firefox 火狐浏览器上启用安全 DNS（DoH）
date: 2022-10-16 10:20 +0800
update: 2022-10-16 10:20 +0800
---

DNS 是指将地址栏中的地址转换成具体网络IP地址的一个协议，而安全 DNS （DNS-over-HTTPS，简称 DoH ）则是基于加密的 HTTPS 协议实现的 DNS 的功能，具有避免网络运营商劫持、有效保护个人浏览记录、去除广告保护隐私等功能。

### 一、启用或禁用 DNS-over-HTTPS

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在“常规”面板中（第一个菜单），向下滚动到“网络设置”部分，然后点击 设置 按钮。
3. 在打开的对话框中，向下滚动到底， 找到 启用 HTTPS over DNS 勾选框，需要时则勾选，反之则取消勾选。
4. 选择对应的供应商提供的地址

### 二、DoH 供应商

除了浏览器自带的供应商外，还有很多其他选择。

#### 2.1 Alidns

阿里云提供的服务，在国内效果好，但不支持广告过滤等功能。 ```https://dns.alidns.com/dns-query```

#### 2.2 DNSPod

腾讯云出品，在国内效果好，注册帐号后支持设置广告过滤等，但支持的过滤规则不多，效果弱。 ```https://dns.pub/dns-query```

#### 2.3 AdGuard

老牌广告过滤商，注册帐号后支持设置广告过滤等自定义内容。

默认 （屏蔽广告、追踪器）```https://dns.adguard.com/dns-query```

家庭保护（屏蔽广告、追踪器、成人内容，并在可能的情况下启用安全搜索和安全模式。) ```https://dns-family.adguard.com/dns-query```

无过滤 ```https://unfiltered.adguard-dns.com/dns-query```

#### 2.4 NextDNS

去广告 DNS 服务商，每月可免费查询 300,000 次，同时支持 DoH 、DoT 等方式。<a href="https://ypingcn.com/go/out?r=nextdns" target="_blank" rel="noopener nofollow" style="color: #0c82ff;" title="NextDns">【注册】</a>

支持的广告过滤规则多，过滤效果较好。但因其服务在海外，网站解析的结果大部分为海外版，一定程度上会影响网站浏览体验。

#### 2.5 Cloudflare

老牌网络服务提供商，且内置在火狐浏览器中。

默认 ```https://cloudflare-dns.com/dns-query```

火狐版 ```https://mozilla.cloudflare-dns.com/dns-query```

屏蔽病毒程序 ```https://security.cloudflare-dns.com/dns-query```

屏蔽病毒程序和成人内容 ```https://family.cloudflare-dns.com/dns-query```

#### 2.6 iQDNS

网友架设的服务，可用作备用。 ```https://a.passcloud.xyz/dns-query```

### 三、排除特定域名

1. 在 地址栏 里输入```about:config```，然后按回车访问。
2. 有时会出现警告页面。点击```我接受此风险，请继续！```接受相关修改风险并继续，以便打开```about:config```页面。
3. 搜索```network.trr.excluded-domains```，如果搜索不到则需要新建一个。
4. 点击其旁边的 修改 按钮。
5. 将域名添加到列表中，如果是多个域名则需要用逗号分割。编辑完成后点击复选保存更改，即可生效。 
