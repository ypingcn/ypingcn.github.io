---
layout: page
title: 如何在 Firefox 火狐浏览器上设置并启用基于 HTTPS 的安全 DNS（DoH）
date: 2022-10-16 10:20 +0800
update: 2023-10-02 12:00 +0800
---

**快速下载**：下载 <a href="https://ypingcn.com/go/out?r=firefox-lastest-zhcn" rel="nofollow" style="color: #0c82ff;"> 最新Firefox火狐浏览器国际版（简体中文） </a>

**快速下载**：【Firefox Setup 115.3.1esr】BT(bittorrent)迅雷下载地址 <a href="magnet:?xt=urn:btih:afc0936d7b424d2fa3f5c42e1bf9496366262a09&dn=Firefox%20Setup%20115.3.1esr.exe&tr=udp%3a%2f%2ftracker.openbittorrent.com%3a6969%2fannounce&tr=https%3a%2f%2ftracker.tamersunion.org%3a443%2fannounce&tr=http%3a%2f%2ftracker.openbittorrent.com%3a80%2fannounce&ws=https%3a%2f%2farchive.mozilla.org%2fpub%2ffirefox%2freleases%2f115.3.1esr%2fwin64%2fzh-CN%2fFirefox%2520Setup%2520115.3.1esr.exe" rel="nofollow" style="color: #0c82ff;">点击下载</a>

---

每个网站都需要知道IP地址才能正确访问，但是 IP 地址太多不可能每个都记录下来，需要有一个方式来给用户使用，这就是域名系统 DNS（Domain Name System）的来由。DNS 是指将地址栏中的地址转换成具体网络IP地址的一个协议，但因其设计没有考虑相关的安全性导致其容易被第三方劫持进而修改结果。

而安全 DNS （DNS-over-HTTPS，简称 DoH ）DoH 代表“DNS over HTTPS”，是一种通过 HTTPS 协议进行 DNS 请求和响应的加密通信方式。传统的 DNS 通信使用的是明文UDP协议，易受到窃听、篡改等攻击，而 DoH 可以加密 DNS 流量，从而提高了安全性和隐私保护。使用 DoH 还可以避免某些网络中间人（例如公共 Wi-Fi）对 DNS 流量进行劫持和污染，从而提高了访问互联网服务的可靠性。越来越多的浏览器和操作系统开始支持DoH，以提高用户的在线安全和隐私保护。

下面是在 Firefox 火狐浏览器使用 DoH 的一些设置教程和注意事项。

------

### 一、启用或禁用 DNS-over-HTTPS

设置入口在 v114.0 版本后有所改动，需要根据版本的不同进行设置。

#### 1.1 版本号 114 以下的版本

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在```常规```面板中（第一个菜单，```about:preferences#general```），向下滚动到```网络设置```部分，然后点击```设置```按钮。
3. 在打开的对话框中，向下滚动到底， 找到```启用 HTTPS over DNS```勾选框，需要时则勾选，反之则取消勾选。
4. 选择对应的供应商提供的地址，或者自行输入需要的地址（本文下一章有推荐整理）。

#### 1.2 版本号 114 以及以上的版本

> v114.0 版本已经于 2023-06-06 发布

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在```隐私与安全```面板中（第四个菜单，```about:preferences#privacy```），向下滚动到```基于 HTTPS 的 DNS```部分。
3. 在```安全 DNS 使用策略```部分，选择增强保护（DoH 失败后尝试使用系统 DNS ）或者最大保护（仅使用 DoH ）。
4. 选择对应的供应商提供的地址，或者自行输入需要的地址（本文下一章有推荐整理）。

------

### 二、DoH 供应商

除了浏览器自带的供应商外，还有很多其他选择。

#### 2.1 Alidns

阿里云提供的服务，在国内效果好，但不支持广告过滤等功能。 

地址：```https://dns.alidns.com/dns-query```

#### 2.2 DNSPod

腾讯云出品，在国内效果好，注册帐号后支持设置广告过滤等，但支持的过滤规则不多，效果弱。 

地址：```https://dns.pub/dns-query```

#### 2.3 OneDNS

OneDNS 是北京微步在线科技有限公司提供的具备安全防护能力的 DNS 递归解析服务，能有效防护恶意软件、勒索病毒等威胁，并且屏蔽各类广告骚扰和欺诈类网站，净化网络环境，保护数据安全。

地址：【拦截版】 ```doh.onedns.net/dns-query``` 【纯净版】 ```doh-pure.onedns.net/dns-query```

#### 2.4 Cloudflare

老牌网络服务提供商，且内置在火狐浏览器中。

默认 ```https://cloudflare-dns.com/dns-query```

火狐版 ```https://mozilla.cloudflare-dns.com/dns-query```

屏蔽病毒程序 ```https://security.cloudflare-dns.com/dns-query```

屏蔽病毒程序和成人内容 ```https://family.cloudflare-dns.com/dns-query```

#### 2.5 AdGuard

>（网络原因不太推荐在国内网络条件下使用）

老牌广告过滤商，注册帐号后支持设置广告过滤等自定义内容。

默认 （屏蔽广告、追踪器）```https://dns.adguard.com/dns-query```

家庭保护（屏蔽广告、追踪器、成人内容，并在可能的情况下启用安全搜索和安全模式。) ```https://dns-family.adguard.com/dns-query```

无过滤 ```https://unfiltered.adguard-dns.com/dns-query```

#### 2.6 NextDNS

>（网络原因，不太推荐在国内网络条件下使用）

去广告 DNS 服务商，每月可免费查询 300,000 次，同时支持 DoH 、DoT 等方式。

支持的广告过滤规则多，过滤效果较好。但因其服务在海外，网站解析的结果大部分为海外版，一定程度上会影响网站浏览体验。

------

### 三、排除特定域名

排除特定域名后，所配置的域名就不会走 DoH 解析而是保持与系统方式一致，适合内网域名或者其他有特殊需要的域名配置。

设置方法同样在 v114.0 版本后有所改动，需要根据版本的不同进行设置。

#### 1.1 版本号 114 以下的版本

1. 在 地址栏 里输入```about:config```，然后按回车访问。
2. 有时会出现警告页面。点击```我接受此风险，请继续！```接受相关修改风险并继续，以便打开```about:config```页面。
3. 搜索```network.trr.excluded-domains```，如果搜索不到则需要新建一个。
4. 点击其旁边的 修改 按钮。
5. 将域名添加到列表中，如果是多个域名则需要用逗号分割。编辑完成后点击复选保存更改，即可生效。 

#### 1.2 版本号 114 以及以上的版本

> v114.0 版本已经于 2023-06-06 发布

1. 点击浏览器汉堡菜单按钮（浏览器的右上角），并选择设置。
2. 在```隐私与安全```面板中（第四个菜单，```about:preferences#privacy```），向下滚动到```基于 HTTPS 的 DNS```部分。
3. 点击```管理例外```按钮后，输入需要添加的域名，保存即可。

---

**更多阅读**

<div class="row">
    <div class="col-lg-8 col-lg-offset-2
    col-md-10 col-md-offset-1
    post-container">
        <ul class="pager">
            <li class="previous">
                <a href="/special/firefox/resource/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Librewolf 浏览器资源汇总》">
                    下一篇<br>
                    <span>《Firefox 火狐浏览器资源汇总》</span>
                </a>
            </li>
            <li class="next">
                <a href="/special/firefox/addons/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Firefox 火狐浏览器插件推荐》">
                    下一篇<br>
                    <span>《Firefox 火狐浏览器插件推荐》</span>
                </a>
            </li>
        </ul>
    </div>
</div>