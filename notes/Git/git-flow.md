---
layout: page
title:  Git-flow 个人理解
date: 2017-07-16 15:00 +0800
update: 2017-07-16 15:00 +0800
---

[Image URL](/img/post/git-flow-main.png)

这图很好地表现出了 git-flow 的整个流程。

## 概要

如图所示，git flow 用了这几个分支：

- master

个人将其理解为正式版的分支，不能在该分支修改只能从其他分支合并而来。

- develop

日常开发用的分支，feature 分支由该分支而来。

- hotfixes

修复正式版代码中的不足之处，修改完成后合并进master 和 develop 分支里。

- feature

新功能/特性分支，修改完成后只能合并进 develop 分支里。

值得一提的是，该分支合并时添加参数 ``` --no-ff``` ，能保留原有分支提交历史。 

- release

新版本的发布分支，完成所有工作后，合并到 master 和 develop 分支里。


