---
layout: page
title:  进程相关(threading)
update: 2018-01-31 20:28 +0800
---

这里是自己写下关于 Python 跟进程相关的 threading 模块的一点笔记，跟有些跟 Linux 调用挺像的，有共通之处。

### Thread

https://docs.python.org/3/library/threading.html?highlight=threading#thread-objects

直接传入

```python
def test(arg):
  print("test " , arg)

t = threading.Thread(target=test,args=(1,))
t.start()
```
继承 Thread 重写 run 方法

```python3
class MyThread(threading.Thread):
  def __init__(self,arg):
    super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
    self.arg=arg
  def run(self):#定义每个线程要运行的函数
    time.sleep(1)
    print("the arg is:%s\r" , self.arg )

```

threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

group 线程组，未实现

start() 线程就绪
join([timeout]) 阻塞其他线程，直到调用这方法的进程结束或时间到达

RuntimeError: cannot join thread before it is started

get/setName(name) 获取/设置线程名。
isAlive() 返回线程是否在运行。
is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

The entire Python program exits when no alive non-daemon threads are left.
没有非后台进程运行，Python 就退出。
主线程执行完毕后，后台线程不管是成功与否，主线程均停止

t.start()
t.join()
start() 后 join() 会顺序执行，失去线程意义

### Lock Rlock（锁）

https://docs.python.org/3/library/threading.html?#lock-objects

Lock属于全局，Rlock属于线程（R的意思是可重入，线程用Lock的话会死锁，来看例子）

```python
import threading 
lock = threading.Lock() #Lock对象 
lock.acquire() 
lock.acquire() #产生了死琐。 
lock.release() 

lock.release() 


import threading 
rLock = threading.RLock() #RLock对象 
rLock.acquire() 
rLock.acquire() #在同一线程内，程序不会堵塞。 
rLock.release() 
rLock.release() 

```

acquire(blocking=True, timeout=-1) 申请锁，返回申请的结果
release() 释放锁，没返回结果

```python
import threading
import time

gl_num = 0

lock = threading.RLock()

## 只会输出一次
# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def F():
  r = False
  if lock.acquire(timeout=1):
    r = True
    print("name" , threading.currentThread().getName())
    global gl_num
    gl_num += 1
    time.sleep(2)
  print(gl_num)
  if r:
	  print("release " , lock.release())


for i in range(10):
  t = threading.Thread(target=F,name=str(i))
  t.start()

```

### Condition （ 条件变量 ）

https://docs.python.org/3/library/threading.html#condition-objects

可以在构造时传入rlock lock实例，不然自己生成一个。

acquire([timeout])/release(): 与lock rlock 相同
wait([timeout]): 调用这个方法将使线程进入等待池，并释放锁。调用方法前线程必须已获得锁定，否则将抛出异常。 
notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。调用方法前线程必须已获得锁定，否则将抛出异常。 
notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

```python
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()


# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print('produce...')
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print('consume...')
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
```

### Semaphore（信号量 ）

threading.Semaphore(value=1)

https://docs.python.org/3/library/threading.html#semaphore-objects

acquire(blocking=True, timeout=None)
资源数大于0，减一并返回，等于0时等待，blocking为False不阻塞进程
返回值是申请结果
release()
资源数加1

```python
import threading
import time

s = threading.Semaphore(value=1)

def p():
    global s
    time.sleep(1)
    print(s.acquire(blocking=False))
    print("p end")

def c():
    global s
    print(s.acquire())
    time.sleep(2)
    print("c end")
    s.release()

t1 = threading.Thread(target=p)
t2 = threading.Thread(target=c)
t2.start()
t1.start()
```

### Event（事件）

https://docs.python.org/3/library/threading.html#event-objects

事件内置了一个初始为False的标志

is_set() 返回内置标志的状态
set() 设为True
clear() 设为False
wait(timeout=None) 阻塞线程并等待，为真时返回。返回值只会在等待超时时为False，其他情况为True

### Timer（定时器）

https://docs.python.org/3/library/threading.html#timer-objects

threading.Timer(interval, function, args=None, kwargs=None)

第一个参数是时间间隔，单位是秒，整数或者浮点数，负数不会报错直接执行不等待
可以用cancel() 取消

### Barrier

https://docs.python.org/3/library/threading.html#barrier-objects

threading.Barrier(parties, action=None, timeout=None)

调用的进程数目达到第一个设置的参数就唤醒全部进程

wait(timeout=None)
reset() 重置，等待中的进程收到``` BrokenBarrierError ```错误

> 来自个人 [ Python 文集 ](http://www.jianshu.com/nb/15212493)
