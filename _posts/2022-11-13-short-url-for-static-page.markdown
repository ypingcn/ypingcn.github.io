---
layout: post
title:  "静态页面也能实现短链接 | 个人博客历史（二）"
subtitle: "Short URL in static page for personal blog"
description: "不用服务器也能实现短链接跳转的功能"
date:   2022-11-13 +0800
update: 2022-11-13 18:00 +0800
author:     "ypingcn"
header-img: "img/home-bg-Sm5ceH.webp"
header-mask: 0.3
catalog:    true
tags:
    - 博客历史
---

本站点是使用 Jekyll 搭建起来的，所有的页面都是静态页面，在部署的时候页面的就已经确认了，并没有实现服务端的逻辑。但有些链接地址太长，直接分享出去会占用太多字数也不好更新。

例如专题里的<a href="/special/firefox/resource/">《最新版 Firefox 火狐浏览器下载》</a> <a href="/special/firefox/librewolf/">《最新版 Librewolf 浏览器下载》</a> <a href="/special/firefox/floorp/">《最新版 Floorp 浏览器下载》</a> 这三个页面，我都增加了「最新版本快速下载」的按钮，原本是直接加上原始下载链接的。但是随着版本更新，每次更新最新版本的地址都需要在三个地方更新三个地址的信息，不仅麻烦，而且会多次触发页面的构建增加不必要的提交历史，于是萌生了实现短链接的逻辑。

## 实现

实现这个功能主要想好两个问题

1. “短地址”到“实际地址”的对应关系如何管理
2. 最终地址如何跳转

### 如何管理

数据管理的话，主要考虑到部署在 ```Github Page```/```Gitee Page```/```COding Page``` 这类第三方服务上的 Jekyll 都不能调用数据库，而且这个短链功能主要是给博客使用，不会大规模对外，使用数据库来管理就太“重”了。所以可以直接把数据存在一个``` routes.json ```文件里，在地址里传进短地址，实际的跳转地址从这个配置文件里获取。 

一个例子——

```markdown
{
    "floorp-windows-lastest": "https://github.com/Floorp-Projects/Floorp/releases/download/v10.7.0/floorp-win64.installer.exe"
}
```

### 如何跳转

静态页面跳转的话就没法返回不同的```HTTP 301（永久重定向）```/``` 302（临时重定向） ```返回码了。但是在功能体验上来说可以尽可能地让用户的等待时间缩短，且逻辑只能在前端实现。

上网搜索了一下，发现一篇博客给了我启发。可以设置 ``` window.location.href ``` 属性来实现跳转，如果有延时的需要则设置定时器后延迟更新属性。

因为静态页面里获取``` routes.json ```时可能会拿到一个带缓存的非最新页面，所以可以在获取的时候加一个``` ?t=[时间戳] ```的小尾巴，这也是很多网站的常规操作了。

非前端开发者，东拼西凑的代码，贴一下自己的实现。主要逻辑是从地址里的```r```参数里获取短地址。如 ```https://example.com/?r=blog``` 这个地址，``` blog ``` 就是我们想要的短地址，不存在的短地址则跳转到``` error.html ``` 上。

```js
function goUrl(config, timeoutMs) {
    fetch(config + `?t=${Date.now()}`)
        .then(response => response.json())
        .then(routes => {
            var queries = parseQueryString(location.search.substring(1))
            var key = queries['r']
            var url = routes[key];
            if (!url)
                url = '/error.html';
            console.log(`${key} redirecting to ${url}`);
            setTimeout(function () {
                window.location.href = url
            }, timeoutMs)
        })
        .catch(error => {
            console.log(error);
        });
}
```
## 最终效果

来看看最终效果吧，逻辑不复杂，虽然并不完美但也是实现了需要的功能。

<button style="background-color:#e7e7e7;"><a target="_blank" rel="noreferrer nofollow" href="https://ypingcn.com/go/out?r=firefox-official">Firefox 火狐浏览器官网</a></button>
<button style="background-color:#e7e7e7;"><a target="_blank" rel="noreferrer nofollow" href="https://ypingcn.com/go/out?r=floorp-official">Floorp 浏览器官网</a></button>
<button style="background-color:#e7e7e7;"><a target="_blank" rel="noreferrer nofollow" href="https://ypingcn.com/go/out?r=librewolf-official">Librewolf 浏览器官网</a></button>


#### 参考网页

1. <a href="https://apqx.me/post/original/2022/05/17/%E4%B8%8D%E5%BF%85%E5%A4%8D%E6%9D%82-%E9%9D%99%E6%80%81%E5%8D%9A%E5%AE%A2%E4%B9%9F%E5%8F%AF%E4%BB%A5%E5%81%9A%E7%9F%AD%E9%93%BE.html" rel="nofollow" style="color: #0c82ff;">《不必复杂，静态博客也可以做短链》</a>