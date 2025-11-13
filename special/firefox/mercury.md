---
layout: page
title: Mercury 浏览器资源汇总（2025年）
description: 号称比原版 Firefox 浏览器性能优化 8%-20% 的 Mercury 浏览器，新一代高效安全的浏览器选择
date: 2025-08-17 15:00 +0800
update: 2025-08-18 09:00 +0800
---

根据官网说明，Mercury 浏览器【<a href="https://thorium.rocks/mercury" rel="nofollow" >官网</a>】是一款着重编译优化的 Firefox 火狐浏览器分支，并且集成了来自 LibreWolf、Waterfox 等多款优秀浏览器的隐私/安全性特性改动。

## 亮点

 - Compiler optimizations include AVX, AES, LTO and PGO.
 - 编译器优化包括 AVX、AES、LTO 和 PGO。
 - Disable all telemetry and reporting.
 - 禁用所有遥测和报告。
 - Remove all debugging constructs and enable hardening by default.
 - 移除所有调试结构，并默认启用加固功能。
 - Enable backspace to go back, and GPU acceleration by default.
 - 默认启用退格键回退功能和 GPU 加速。
 - Enable Do Not Track and Global Privacy Control.
 - 启用“勿追踪”和“全球隐私控制”。
 - Disable Pocket, highlights, and suggested content on the new tab page.
 - 禁用新标签页中的 Pocket、高亮和建议内容。
 - Restore top bar to ~ESR78 state with home button and developer button.
 - 恢复顶部栏至 ESR78 状态，包含主页按钮和开发者按钮。
 - Allow installing unsigned extensions.
 - 允许安装未签名的扩展。
 - Branding changes  品牌更改
 - Enable JPEG XL by default
 - 默认启用 JPEG XL
 - Implemented performance tweaks from BetterFox.
 - 实施了 BetterFox 提供的一些性能优化。
 - Disabled "Normandy", a component that allows Mozilla to alter extension configurations at will remotely. (bleh wtf is that)
 - 禁用了“Normandy”，这是一个允许 Mozilla 远程随意更改扩展配置的组件。（真是烦人，这是什么）

Mercury 浏览器着重于改进易用性和增强隐私/安全性的补丁。基于原生 Firefox，在性能、安全性和易用性方面做进一步的优化，其中许多来自于 LibreWolf、Waterfox、FireDragon、PlasmaFox、Ghostery 和 GNU IceCat。

Mercury 浏览器在基准测试和不同操作系统上相比原生 Firefox 可提高 8%-20%的性能。

## 编译器优化方式对比

1. AVX（Advanced Vector Extensions）：向量指令集优化
2. AES（Advanced Encryption Standard）：加密指令集优化
3. LTO（Link-Time Optimization）：链接时全局优化
4. PGO（Profile-Guided Optimization）：Profile引导的动态优化

| 优化类型	 |         核心目标	          |           依赖条件            |       	适用场景        |
| ---------- | -------------------------- | ---------------------------- | ---------------------- |
| AVX        | 	利用向量指令提升数据并行性能 | 	CPU支持AVX指令集	             | 科学计算、多媒体处理     |
| AES	     | 利用硬件指令加速加密解密	  | CPU支持AES指令集              | 加密库、安全协议         |
| LTO	     | 跨文件全局优化	              | 编译器支持LTO                 | 大型项目、跨文件调用频繁  |
| PGO        | 	基于运行时反馈的动态优化	  | 可收集真实运行场景的profile	 | 服务器应用、桌面程序     |

## 下载方式

访问【<a href="https://thorium.rocks/mercury" rel="nofollow" >官网</a>】，找到【Releases (Linux & Windows) 】的下载入口，根据 Windows 、MacOS 或 Linux 等操作系统选择下载~

## 提醒

个人开发者因精力有限，所开发浏览器往往更新频率低，甚至存在断更风险，其功能迭代、bug修复及安全补丁无法及时跟进，可能影响使用稳定性与安全性，建议谨慎将 Mercury 浏览器作为主力浏览器使用。

截止 2025 年 08 月 18 日，作者 Alex313031 最近一次更新 Mercury 浏览器时间已经是 2024 年 09 月 17 日，间隔时间接近一年。
---

**更多阅读**

<div class="row">
    <div class="col-lg-8 col-lg-offset-2
    col-md-10 col-md-offset-1
    post-container">
        <ul class="pager">
            <li class="previous">
                <a href="/special/firefox/doh/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Firefox 火狐浏览器设置安全 DNS （DoH）》">
                    下一篇<br>
                    <span>《Firefox 火狐浏览器设置安全 DNS （DoH）》</span>
                </a>
            </li>
            <li class="next">
                <a href="/special/firefox/version/" target="_blank" data-toggle="tooltip" data-placement="top"
                    title="《Firefox 火狐浏览器版本差异》">
                    下一篇<br>
                    <span>《Firefox 火狐浏览器版本差异》</span>
                </a>
            </li>
        </ul>
    </div>
</div>
