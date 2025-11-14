---
layout: page
title:  Git 基础命令 与 Git 飞行规则
date: 2017-07-16 15:00 +0800
update: 2021-10-30 17:06 +0800
---


## Git 基础命令

参考资料

Git - Book <a href="https://git-scm.com/book/en/v2"  target="_blank" rel="noopener nofollow">#英文版链接</a> <a href="https://git-scm.com/book/zh/v2"  target="_blank" rel="noopener nofollow">#中文版链接</a>

### 初始化

```
git init
git init [proj-name]
git clone [url]
```

### 配置

```
git config --list
git config -e [--global]
git config [--global] user.name "[name]"
git config [--global] user.email "[email address]"
```

### 增删文件

```
git add [file1][file2]
git add [dir]
git add . //添加当前目录的所有文件
git rm [file1] //删除文件并记录此次删除
git rm --cache [file] //停止追踪指定文件，保留文件在工作区
git mv [name1][name2] //改名，记录此次改名
```

### 提交

```
git commit -m "message"
git commit [file1][file2] -m "message"
git commit -a
git commit -v //提交时显示所有diff信息
git commit --amend [file1][file2] //重写上一次的更新
git push origin local_branch:remote_branch
```

### 分支

```
git branch //本地
git branch -r  //远程
git branch -a  //本地和远程
git branch [name] // 新建分支
git checkout -b [name] //新建分支并切换
git checkout [name] //切换分支，更新工作区
git branch [branch][commit] //新建分支并指向指定分支
git branch --track [branch][remo-branch] //新建分支并于远程分支建立关系
git branch --set-upstream [branch][remo-branch] //与远程分支建立追踪关系
git merge [branch] //合并分支到当前分支
git cherry-pick [commit] //选择一个commit合并进当前分支
git branch -d [branch] //删除本地分支
git push origin --delete [branch] //删除远程分支
```

## 远程分支

```
git remote set-url origin <new url> // 修改origin
git remote add origin <url> // 空仓库时设置 origin,配合使用更佳 git push -u origin master 默认选择origin
```

## Git 飞行规则

这里有常见问题的记录汇总，以及对应的处理方法。

https://github.com/k88hudson/git-flight-rules/blob/master/README_zh-CN.md
