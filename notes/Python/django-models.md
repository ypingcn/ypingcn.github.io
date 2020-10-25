---
layout: page
title:  Django 中的 models
update: 2017-07-16 22:01 +0800
---

## 概述

models 用来创建数据库表。创建后运行以下命令迁移数据方可使用

```python
python manage.py makemigrations
python manage.py migrate
```

```python
python manage.py dumpdata appname > appname.json
python manage.py loaddata appname.json
```

## 字段

一个 models 的结构大致如下

```python
from django.db import models
class test(models.Model):
    a1 = models.AutoField(primary_key=True)
    a2 = models.CharField(max_length=100)
```

其中的```AutoField``` ``` CharField ``` 就是字段，定义了数据库中存储数据的类型

django 有丰富的字段可供选择。

在 django 的文档中可以查询到更为具体的内容
[《Model field reference | Django documentation | Django》](https://docs.djangoproject.com/en/dev/ref/models/fields/#model-field-types)

## 参数

上面例子中的```primary_key=True``` ``` max_length=100 ```  便是对字段进行限制的参数。

```
1.null=True 数据库中该字段可为空
2.blank=True django 的 admin 添加数据时可留空
3.YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
example = models.CharField(choice = YEAR_IN_SCHOOL_CHOICES) 选项
4.default = 0 默认值为0
5.primary_key = True 主键
6.unique = True 不允许重复
```

这些只是个例子，更多解释还是要看文档，filed options 部分 [《Models | Django documentation | Django》](https://docs.djangoproject.com/en/dev/topics/db/models/#field-options)

## 表间关系

数据表之间可以有以下几个关系

```
一对多:models.ForeignKey(其他表)
多对多:models.ManyToManyField(其他表)
一对一:models.ManyToManyField(其他表)
```

创建上跟之前的没有多大的区别，举个例子：

````python
class people(models.Model):
    name = models.CharField(max_length=100)
    age = models.models.IntegerField()
    
class boy(models.Model):
    n = models.ForeignKey(people)
````

## 数据操作

```python
from <appname>.models import *
#增
people.objects.get_or_create(name="1")
#删
people.objects.all().delete()
#改
people.objects.filter(name="1").update(name="2")
#查
people.objects.get(name="1") #单条数据
people.objects.filter(name="1") #特定数据，不一定是一条（例子不是很好）
#数据个数
a = people.objects.filter(name="1")
len(a)
people.objects.filter(name="1").count()
#范围
people.objects.filter(age__range=[0,100])
#包含
people.objects.filter(name__contains="1")
#排序
people.objects.all().order_by('-age') #从大到小排序，要从小到大排则去掉负号
#其他
startswith istartswith endswith iendswith
```

## 管理

在相应文件夹中的 ```admin.py``` 编辑好内容，就可以在管理界面中管理数据

```python
from django.contrib import admin

# Register your models here.

from <appname> import models

admin.site.register(models.people)
```

如果显示的是 xxx objects，可以这样弄使得数据更容易理解

```python
class test(models.Model):
    #python2
    def __unicode__(self):
        return self.name
    #python3
    def __str__(self):
        return self.name
```

## 总结

django 的文档挺齐全的，上面也只是对我自己学习上的一个整理。

参考：

[Django documentation | Django documentation | Django](https://docs.djangoproject.com/)

[Django中的页面管理后台](https://www.cnblogs.com/zknublx/p/5944779.html)
