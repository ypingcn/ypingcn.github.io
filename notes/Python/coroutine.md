---
layout: page
title:  协程的魅力
date: 2018-01-22 20:00 +0800
update: 2021-11-23 22:03 +0800
---

协程类似于进程，在IO或者其他需要较长等待时间的操作执行结束前执行其他操作，但是因为不用进程切换，所以效率高。也可以用多进程加协程充分利用CPU

## 用作协程的生成器

```python
from inspect import getgeneratorstate

def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
a = average()
next(a)
print(a.send(1))
print(a.send(3))
a.close()
```

预激生成器
```python
def coroutine(function):
    @wraps(function)
    def call_it(*args,**kwargs):
        gen = function(*args,**kwargs)
        next(gen)
        return gen
    return call_it
@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count
a = average()
print(a.send(1))
print(a.send(3))
a.close()
```
处理异常
```python
from functools import wraps
def coroutine(function):
    @wraps(function)
    def call_it(*args,**kwargs):
        gen = function(*args,**kwargs)
        next(gen)
        return gen
    return call_it
class Demo(Exception):
    pass
@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        try:
            term = yield average
            total += term
        except Exception:
            print("wrong value")
        else:
            count += 1
            average = total / count
a = average()
print(a.send(1))
print(a.send(3))
print(a.throw(Demo)) # 不会改变平均值
print(a.send("1")) # 不会改变平均值
a.close()
```
协程返回值
```python
from functools import wraps
def coroutine(function):
    @wraps(function)
    def call_it(*args,**kwargs):
        gen = function(*args,**kwargs)
        next(gen)
        return gen
    return call_it
class Demo(Exception):
    pass
@coroutine
def average():
    total = 0.0
    count = 0
    average = None
    while True:
        try:
            term = yield
            if term is None:
                break
            total += term
        except Exception:
            print("wrong value")
        else:
            count += 1
            average = total / count
    return average
a = average()
a.send(1)
a.send(3)
try:
    a.send(None)
except StopIteration as e:
    print(e.value)
a.close()
```
### asyncio 库

可以借助 asyncio 库里的函数将一个普通函数改成协程

官方文档：https://docs.python.org/3/library/asyncio.html

例子一

```python
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())

task = []
for i in range(10):
    task.append(hello())
loop2.run_until_complete(asyncio.wait(task))
loop.close()
loop2.close()
```
例子二
```python
@asyncio.coroutine
def smart_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.2)
		yield from asyncio.sleep(sleep_secs)
		print('Smart one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1
 
@asyncio.coroutine
def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.4)
		yield from asyncio.sleep(sleep_secs)
		print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1
 
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [
		asyncio.async(smart_fib(10)),
		asyncio.async(stupid_fib(10)),
	]
	loop.run_until_complete(asyncio.wait(tasks))
	print('All fib finished.')
	loop.close()
```

### async 和 await 关键字

这两个字是在 Python 3.5 引入的，async 类似与 @asyncio.coroutine ，await 类似于 yield from

改写上文的例子。

```python
async def smart_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.2)
		await asyncio.sleep(sleep_secs)
		print('Smart one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1
 
async def stupid_fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		sleep_secs = random.uniform(0, 0.4)
		await asyncio.sleep(sleep_secs)
		print('Stupid one think {} secs to get {}'.format(sleep_secs, b))
		a, b = b, a + b
		index += 1
 
if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	tasks = [
		asyncio.ensure_future(smart_fib(10)),
		asyncio.ensure_future(stupid_fib(10)),
	]
	loop.run_until_complete(asyncio.wait(tasks))
	print('All fib finished.')
	loop.close()
```
