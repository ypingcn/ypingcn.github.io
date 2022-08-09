---
layout: post
title:  "个人博客推广记录总结"
subtitle: "how to promote personal blog"
description: ""
date:   2022-06-02 +0800
update: 2022-08-09 11:20 +0800
author:     "ypingcn"
header-img: "img/bg.webp"
header-mask: 0.3
catalog:    true
tags:
    - 分享
    - 教程
---
> 这是一篇对本博客推广的记录总结。也希望能成为其他有缘人推广自己个人博客的借鉴吧。

博客是用 GitHub Page + Jekyll 搭建的。早期是没有用独立域名，一直是挂靠在 ```github.io```的二级域名下，也没有做任何的推广，只是提交了 sitemap 随缘让搜索引擎收录，也没有在任何地方推广。所以一年前的访问量都很低——Search console 里显示的最高一天曝光是60，点击是5。曝光量最高的关键词是 ``` latex 偏导数```，估计是因为这篇文章[《Markdwon + LaTex 表达数学式子》](/notes/Markdown/LaTex-math/)意外地得到青睐，要不然这样子随缘根本不可能有访问。虽然博客是在2016年开始的，但是早期的博客内容也是在校期间零碎的记录，感兴趣的人有限，再加上没有给原有的独立域名续费，所以博客是一直在一种【低频+二级站点】状态下运行的，默默无闻的透明站。

从去年中下旬（大概是2021年10月底）就打算重新将博客运营起来，主要做了这些事情——

1. 2021年11月购入本站域名并绑定使用。将原有的 ```github.io``` 域名迁移到新域名下。
2. 在 Bing Webmaster Tools 和 Google Search Console 进行相关设置，通知博客已经绑定了独立域名，需要进行相关迁移。
3. 明确博客定位。因为早期的博客内容主题都比较凌乱没有相对统一话题倾向，所以趁这次迁移独立域名的机会，重新明确写作目标。将专注在【技术、生活、分享、火狐、投资】五类上。
4. 因为本人是火狐浏览器的用户，从这点入手更容易做，所以结合自己地使用经验，断断续续地更新了 [《火狐浏览器资源汇总》](/special/firefox/resource/) [《火狐浏览器主题美化》](/special/firefox/theme/) [《火狐浏览器插件推荐》](/special/firefox/addons/) 等几篇内容。
5. 优化对搜索引擎地可见性。因为写的博客需要被搜索引擎收录后才能被更多的人用关键词访问到。所以对搜索引擎友好能有助于推广。除去提交 sitemap 外，同时完善了网页 meta 信息，包括将写作目标写进 keyswords、完善 Open Graph Meta Tags 让在社交网站分享时更为友好、提供  JSON-LD 结构化数据信息（不过这点现在看来作用有限因为搜索结果展示没有特殊变化）。
6. 同时也做了对用户访问体验更好地改动，包括压缩相关图片的大小、调整加载资源的设置。资源加载改动不大毕竟不是专业的前端开发大佬，只是把 cloudflare 换到 jsdelivr 上和顺手更新 jquery 和 bootstrap 版本避免漏洞。优化可以借助 Lighthouse 的得分有针对性的看。目前本站的得分是【性能100、无障碍-86、最佳做法-92、SEO-100】
7. 申请加入【中文独立博客列表】【开往-友链接力】和【十年之约】。其实这次对博客的推广优化是源于想加入【开往】项目的，但无奈管理员半年后才审批通过，所以博客的优化工作已经在期间完成的。加入【十年之约】更多是想要有个目标，迫使自己不断更。我挺喜欢他们的口号的——“一个人的寂寞，一群人的狂欢。”

做了这些后博客的访问量显著上升，最高曝光每天已经有600了，特别是“火狐插件”这个关键词已经能到相关结果的前五！这无疑是一种激励！详见  [《火狐浏览器插件推荐》](/special/firefox/addons/)

希望后续能借博客沉淀下更多属于自己的知识，帮助到更多的人。

---

2022.07.07 更新

本站博客内容索引无故被必应删除，使用'site'命令搜索都提示```Some results have been removed```/```部分搜尋結果已被移除```/```部分搜索结果未予显示。有关详细信息，请参阅此处。```，以必应为基础的例如 DuckDuckGo 等均无法搜索到本站，谷歌索引暂时正常。但必应站长里也没有相关的版权投诉问题，后台显示每天爬虫都有爬取，申述无果。网上也有类似的博主反馈被删除，暂时无能为力。

记录一下其他博主的类似问题，以便有空的时候尝试解决问题。

2022-03-25 <a href="https://www.jessesquires.com/blog/2022/03/25/my-website-disappeared-from-bing-and-duckduckgo/" rel="nofollow" style="color: #0c82ff;">《My website disappeared from Bing and DuckDuckGo · Jesse Squires》</a>

2022-07-25 <a href="https://www.jessesquires.com/blog/2022/07/25/my-website-disappeared-from-bing-and-duckduckgo-part-2/" rel="nofollow" style="color: #0c82ff;">《My website disappeared from Bing and DuckDuckGo, Part 2 · Jesse Squires》</a>

2022-06-16 <a href="https://lapcatsoftware.com/articles/bing.html" rel="nofollow" style="color: #0c82ff;">《Bing and DuckDuckGo removed my business web site - Jeff Johnson》</a>

2022-06-24 <a href="https://io.bikegremlin.com/28530/microsoft-bing-serp-gone-overnight/" rel="nofollow" style="color: #0c82ff;">《Microsoft Bing - site gone from SERP overnight! | BikeGremlin I/O》</a>
