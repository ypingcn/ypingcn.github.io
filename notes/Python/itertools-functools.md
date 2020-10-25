---
layout: page
title:  itertools 和 functools 
update: 2018-01-22 20:00 +0800
---


## itertools

| 函数                                       | 解释                                       |
| ---------------------------------------- | ---------------------------------------- |
| itertools.dropwhile(predicate,it)        | 处理的是it，跳过predicate为真时的值，然后在第一个不为真的时候不再检查输出剩余内容 |
| filter(predicate,it)                     | 当predicate为真时输出相应的it，如果predicate为None时只输出真值内容。 |
| itertools.filterfalse(predicate,it)      | 与filter相反的效果                             |
| itertools.compress(it,selector_it)       | 当selector_it 为真时，输出相应的it（两个都是迭代器）        |
| itertools.islice(it,start,stop,step=1)   | 惰性操作的切片                                  |
| itertools.islice(it,stop)                | 惰性操作的切片                                  |
| itertools.accumulate(it[,func])          | 前两个元素计算结果后与接下来的一个求和，以此类推得出结果。            |
| itertools.starmap(func,it)               | it 的每个元素 itt 是可迭代的，每个元素以func(*it) 形式调用。例如 ``` list(itertools.starmap(lambda a,b:a+b , enumerate(itertools.accumulate(range(3)),1))) ``` --> ```[1,3,6] ``` |
| enumerate(it,start=0)                    | 输出 (index,item) 元组组成的列表                  |
| map(func,it[,it2,...itn])                | 将参数的it传给func,有多个it则需要func支持n个参数，一个it结束则计算结束。例如```list(map(lambda a,b:(a,b) , range(100) , [1,2,3] ))```  --> ``` [(0, 1), (1, 2), (2, 3)] ``` |
| itertools.chain(it1,...itn)              | 将参数里的所有元素连接起来                            |
| itertools.chain.from_iterable(it)        | 将参数里的所有元素连接起来 ```list ( itertools.chain.from_iterable(enumerate('XYZ',1)) ) ``` --> ``` [1, 'X', 2, 'Y', 3, 'Z'] ``` |
| itertools.product(it1,...itn,repeat=1)   | 计算笛卡尔积，repeat表示重复处理次数 , ``` list ( itertools.product([1,2],repeat=2) ) ``` --> ``` [(1, 1), (1, 2), (2, 1), (2, 2)]``` , ``` list ( itertools.product([1,2],[3,4],repeat=1) ) ``` --> ``` [(1, 3), (1, 4), (2, 3), (2, 4)]``` |
| zip(it1,it2,...itn)                      | 输出n个元素组成的元组，其中一个it 结束，全部计算结束             |
| itertools..zip_longest(it1,it2,...itn,fillvalue=None) | 类似zip ，但是遇到一个it 结束则补充fillvalue继续运算，直到所有 it 都结束 |
| itertools.combinations(it,len)           | **(不包含相同元素) **在it所有的元素中选len个，输出所有的组合可能性 ``` list( itertools.combinations([1,2,3,3],2) ) ``` --》 ``` [(1, 2), (1, 3), (1, 3), (2, 3), (2, 3), (3, 3)] ``` |
| itertools.combinations_with_replacement(it,len) | **(包含相同元素)** 同itertools.combinations(it,len) |
| itertools.permutations(it,len=None)      | 输出排列，len 默认为len(it)                      |
| itertools.conut(start,step)              | 计数                                       |
| itertools.cycle(it)                      | 循环输出it里的元素，到了最后一个元素则下一次输出第一个             |
| itertools.repeat(item[,time])            | 重复输出元素 item ，除非指定次数                      |
| itertools.groupby(it,key=None)           | 输出(k,g) 形式的元组，key 为分组标准，g 为相应的生成器 . ``` for len,group initertools.groupby(['a','aa','aaa'],len): print(len,list(group)) ``` --> ``` 1 ['a']  2 ['aa']  3 ['aaa'] ``` |
| itertools.tee(it,n=2)                    | 产出由 n 个生成器组成的元组，每个生成器用于单独输出序列。 ``` list( zip( *itertools.tee('XYZ',3) ) ) ``` -- > ``` [('X', 'X', 'X'), ('Y', 'Y', 'Y'), ('Z', 'Z', 'Z')] ``` |
| reversed(seq)                            | seq需要是序列或者是实现了``` __reversed__ `` 的对象    |

## functools

| 函数                                       | 解释                                       |
| ---------------------------------------- | ---------------------------------------- |
| ```functools.partial(func, *args, **keywords)``` | 偏函数，冻结位置函数或关键字参数                         |
| functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES) | 将  `__module__`, `__name__`, `__qualname__`, `__annotations__`and `__doc__` 同步到新的函数，参数是包装的函数、被包装的函数 |
| functools.warps(function)                | 等于  partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated) |
| functools.reduce(function, iterable[, initializer]) | 相当于 reduce()                             |
| functools.cmp_to_key(function)           | 用于 sorted() python3 sorted() 没有cmp 参数，sorted(iterable, key=cmp_to_key(locale.strcoll)) |
| functools.total_ordering                 | 某个类如果定义了__lt__、**le**、**gt**、__ge__这些方法中的至少一个，使用该装饰器，则会自动的把其他几个比较函数也实现在该类中，用在类上 |
| functools.lru_cache(maxsize=128, typed=False) | 将运行结果缓存下来，maxsize 为缓存大小，2 的幂,typed 为真则分类型存储。 |

### functools 示例

#### 基本装饰器的例子

```python
def w(function):
    def call_it(*args,**kwargs):
        print("before")
        function()
        print("after")
    return call_it

@w
def hello():
    print("hello")

hello()
```

#### functools.partial

```python
urlunquote = functools.partial(urlunquote, encoding='latin1')
# urlunquote(args, *kargs)
# 相当于 urlunquote(args, *kargs, encoding='latin1')
```

#### functools.update_wrapper

```python
from functools import update_wrapper

def w(function):
    def call_it(*args,**kwargs):
        print("before")
        function(*args,**kwargs)
    return update_wrapper(call_it,function)

@w
def hello():
    print("hello")

hello()
print(hello.__name__)
```

#### functools.wrap

```python

from functools import wraps

def w(function):
    @wraps(function)
    def call_it(*args,**kwargs):
        print("before")
        function(*args,**kwargs)
    return call_it

@w
def hello():
    print("hello")

hello()
print(hello.__name__)
```

#### functools.reduce

```python
from functools import reduce

print( reduce(lambda x,y: x+y,[1,2,3,4]) )
# 10
print( reduce(lambda x,y: x+y,[1,2,3,4],10))
# 20
```

#### functools.total_ordering

````python
@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
print dir(Student)
````
