---
layout: page
title:  C++基础知识
update: 2022-07-06 00:00 +0800
---

[toc]

# 基本概念

## 左值、右值

左值 lvalue 是有标识符、可以取地址的表达式，如
 - 变量、函数或数据成员的名字
 - 返回左值引用的表达式，如 ++x、x = 1、cout << ' '
 - 字符串字面量如 "hello world"

纯右值 prvalue 是没有标识符、不可以取地址的表达式，一般也称之为“临时对象”。最常见的情况有：
 - 返回非引用类型的表达式，如 x++、x + 1、make_shared<int>(42)
 - 除字符串字面量之外的字面量，如 42、true

生命周期按使用范围先进后出
特殊规则：如果一个 prvalue 被绑定到一个引用上，它的生命周期则会延长到跟这个引用变量一样长。（只对 prvalue 有效，而对 xvalue 无效。如果由于某种原因，prvalue 在绑定到引用以前已经变成了 xvalue，那生命期就不会延长。）

# 关键字与函数实现

## static

 - 隐藏【不同文件不能看到其他文件的 static 变量和 函数】
 - 持久 【整个程序生命周期】

## define const

| const | define |
| ----- | ------ |
| 预处理展开 | 编译运行使用 |
| 类型检查  | 不检查    |

## typedef const 

> const

阻止变量被修改

参数不能在函数内部被修改

类的成员函数如果是 const 常函数，表示不能修改类内部数值

返回值定义为 const 使得其不能为左值，== 错误打成 = 可以检查出来

> typedef 

类型的别名

结构体

定义平台无关的类型

复杂的声明定义 

```
int *(*a[5])(int, char*);
typedef int *(*pFun)(int, char*);pFun a[5]; 
```

## const 指针

const int * a

const * int b

不能靠解引用改变它指向的对象的值，但是本身的值可以改

int * const a

常量指针，能靠解引用改变它指向的对象的值，本身的值不能改。

## 指针引用区别

★相同点：

●都是地址的概念；

指针指向一块内存，它的内容是所指内存的地址；而引用则是某块内存的别名。

★不同点：

●指针是一个实体，而引用仅是个别名；

●引用只能在定义时被初始化一次，之后不可变；指针可变；引用“从一而终”，指针可以“见异思迁”；

●引用没有const，指针有const，const的指针不可变；

●引用不能为空，指针可以为空；

●“sizeof 引用”得到的是所指向的变量(对象)的大小，而“sizeof 指针”得到的是指针本身的大小；

●指针和引用的自增(++)运算意义不一样；

●引用是类型安全的，而指针不是 (引用比指针多了类型检查

## strlen()

```c++
int strlen(const char * src)
{
    assert(src != NULL);
    int len = 0 ;
    while(*len != '\0')
        len++;
    return len;
}
```

## strcpy()

```c++
char * strcpy(char * dest,const char *src)
{

    assert((dest != NULL) && (src != NULL));
    char * ans = dest;
    while((*dest++ = *src++) != '\0');
    return ans;
}
```
## memset()

```
void * memset(void * s,int c,size_t n)
{
	const unsigned char newc = c;
	unsigned char * tmp = s;
	while(n--)
	{
      *tmp = newc;
      tmp++;
	}
	return s;
}
```

## memcpy()

```
void * memcpy(void * dst,const void * src,size_t size)
{
  assert((dst!=NULL)&&(src!=NULL));
  char * dst1;
  char * src1;
  if(src < dst && (char*)src + size > dst)
  {
    src1 = (char *)src + size - 1;
    dst1 = (char *)dst + size - 1;
    while(size --)
    {
      *dst1-- = *src1--;
    }
  }
  else
  {
    src1 = (char*)src;
    dst1 = (char*)dst;
    while(size --)
    {
      *dst1 ++ = *src1++;
    }
  }
  return dst;
}
```

## 可变参数

```c++
#include<stdarg.h>

char * f(const char * first,...)
{
  size_t len;
  char * buff;
  va_list argp;
  char * tmp;

  if(first == NULL)
    return NULL;

  len = strlen(first);
  va_start(argp,first);
  while( ( tmp = va_arg(argp,char *) ) != NULL)
    len += strlen(tmp);
  va_end(argp);

  buff = (char *)malloc(len+1);
  if(buff == NULL)
    return NULL;

  
  int buf_len = 0;
  strcat(buff+buf_len,first);
  buf_len += strlen(first);
  va_start(argp,first);
  while( (tmp = va_arg(argp,char *) ) != NULL )
  {
    strcat(buff+buf_len,tmp);
    buf_len += strlen(tmp);
  }
  va_end(argp);

  return buff;

}
int main()
{
  cout<<f("hello","athena");
  // 输出 helloathena
  return 0;
}
```

## 获得结构体内成员的偏移量

```cpp
#define myoffsetof(type,member) ((size_t)&((type*)0)->member)
```

# C++ 部分

## C/C++ 

面向过程与面向对象（继承、多态、封装）

C++ 有异常处理，模版，重载，命名空间

## C++/Java 

| C++              | Java    |
| ---------------- | ------- |
| 类 结构 函数 外部变量 预处理 | 只有类     |
| 有指针              | 没       |
| 多继承              | 单继承     |
| 要声明              | 所有类都是虚类 |

## C++11


 - auto
 - nullptr
 - 基于范围的 for 循环 （for(int a : v)）
 - 继承中的 override + final
 - 智能指针( unique_prt - shared_ptr - weak_ptr )
 - lambda ( ```[]()->type{}``` )
 - 强类型枚举
```c++
enum class Options {None, One, All};
Options o = Options::All;
```

## 特殊成员函数

### 默认构造函数
```
A::A()
```
### 复制构造函数
```
A::A(A&)
A::A(const A&)
A::A(volatile A&)
A::A(const volatile&)
```
### 移动构造函数 (C++11 起)
```
A::A(A&&)
A::A(const A&&)
A::A(volatile A&&)
A::A(const volatile&&)
```
### 复制赋值运算符
```
A& operator=(A)
A& operator=(A&)
A& operator=(const A&)
A& operator=(volatile A&)
A& operator=(const volatile A&)
```
### 移动赋值运算符 (C++11 起)
```
A& operator=(A&&)
A& operator=(const A&&)
A& operator=(volatile A&&)
A& operator=(const volatile A&&)
```
### 析构函数
```
~A::A()
virtual ~A::A()
```
## C++11 default


## C++11/14/17

https://github.com/changkun/modern-cpp-tutorial

### std::optional

管理一个可选的容纳值，即可以存在也可以不存在的值。
能用 std::nullopt 创建任何（空的） std::optional
```cpp
std::optional<string> o;
std::optional<string> o1 = std::nullopt;
```

### std::variant
类型安全的联合体，实例在任意时刻要么保有其一个可选类型之一的值，要么在错误情况下无值。
```cpp
 std::variant<int,float> v;
 v = 42;
 int value = std::get<int>(v);
```

### std::any
描述用于任何类型的单个值的类型安全容器

```cpp
std::any a = 1;
std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
a = 3.14;
std::cout << a.type().name() << ": " << std::any_cast<double>(a) << '\n';
a = true;
std::cout << a.type().name() << ": " << std::any_cast<bool>(a) << '\n';
if (a.has_value())
{
    std::cout << a.type().name() << '\n';
}

// 重置
a.reset();
if (!a.has_value())
{
    std::cout << "no value\n";
}

i: 1
d: 3.14
b: true
i
no value
```

### C++20

> 更多资料 【C++20：四巨头 | 类库大魔王的挖井日记 | https://minidump.info/blog/2020/02/the-big-four-of-cpp20/】

#### concept

模板编程在编译期就进行参数检查，限制模板参数

```cpp
template<typename T>
concept bool Stringable = requires(T a){
    {a.to_string()} -> string;
};

template<typename T>
concept bool HasStringFunc = requires(T a){
    { to_string(a) } -> string;
};

void print(Stringable a){
    std::cout << a.to_string() << std::endl;
}

void print(HasStringFunc a){
    std::cout << to_string(a) << std::endl;
}

int main() {
    Person p(57, 170.0);

    print(p); // uses concept Stringable
    print(3); // uses concept HasStringFunc
}
```
一个 gcd 的实现

```cpp
template<typename T>
concept bool Integral(){
    return std::is_integral<T>::value;
}

Integral auto gcd(Integral auto a,
                  Integral auto b){
    if( b == 0 ) return a; 
    else return gcd(b, a % b);
}

// 等效
template<typename T>
requires Integral<T>()
T gcd(T a, T b){
    if( b == 0 ) return a; 
    else return gcd(b, a % b);
}
```

> https://zh.cppreference.com/w/cpp/concepts

#### range/view/range

range：有 begin() end() 的东西
view：减少拷贝的视图，概念指定拥有常数时间复制、移动及赋值
range adaptor：range适配器，就是将一个range转换为一个view的东西


> https://github.com/ericniebler/range-v3

> https://zh.cppreference.com/w/cpp/ranges


```cpp
std::vector<int> ints{0,1,2,3,4,5};
    auto even = [](int i){ return 0 == i % 2; };
    auto square = [](int i) { return i * i; };
 
    for (int i : ints | std::views::filter(even) | std::views::transform(square)) {
        std::cout << i << ' ';
    }
```

#### coroutines

> https://zh.cppreference.com/w/cpp/language/coroutines

co_await 暂停执行直至恢复
co_yield 暂停并返回一个值
co_return 完成执行并返回一个值

```cpp
task<> tcp_echo_server() {
  char data[1024];
  for (;;) {
    std::size_t n = co_await socket.async_read_some(buffer(data));
    co_await async_write(socket, buffer(data, n));
  }
}

generator<int> iota(int n = 0) {
  while(true)
    co_yield n++;
}

lazy<int> f() {
  co_return 7;
}
```

#### module

> https://zh.cppreference.com/w/cpp/language/modules

## 多态性

编译时多态（静态）、运行时多态（动态）
静态：函数模版体现多态性
动态：虚函数，有继承关系的子类和父类之间，虚函数允许子类重写父类的成员函数，定义一个父类的指针，指向子类的对象，而且调用的又是虚函数，运行时就会动态绑定到父类指针的子类对象，查找子类的虚函数表，找到虚函数的地址。纯虚函数基类没有定义，其派生类必须实现。
virtual void f() = 0

## 动态绑定和静态绑定

对象的静态类型是声明时采用的类型，编译期确定。
对象的动态类型是运行时决定的。
```cpp
class B
{
}
class C : public B
{
}
class D : public B
{
}
D* pD = new D();//pD的静态类型是它声明的类型D*，动态类型也是D*
B* pB = pD;//pB的静态类型是它声明的类型B*，动态类型是pB所指向的对象pD的类型D*
C* pC = new C();
pB = pC;//pB的动态类型是可以更改的，现在它的动态类型是C*
```

静态绑定是绑定对象的静态类型，动态绑定是绑定对象的动态类型。

非虚函数是静态绑定的。虚函数是动态绑定的。指针和引用同样适用。

默认参数是静态绑定的。

## 虚函数

编译器必需要保证虚函数表的指针存在于对象实例中最前面的位置

多继承虚函数表有多项内容

参见 http://blog.csdn.net/wanghaobo920/article/details/7674631

https://coolshell.cn/articles/12165.html

## 构造函数类型

无参数构造函数

一般构造函数（也称重载构造函数）

拷贝构造函数

等号赋值运算符

## 拷贝构造函数调用时机

拷贝构造函数将会被调用。以下情况都会调用拷贝构造函数：

（1）一个对象以值传递的方式传入函数体 

（2）一个对象以值传递的方式从函数返回 

（3）一个对象需要通过另外一个对象进行初始化。

## 构造函数的初始化成员列表

初始化成员列表少了一次调用默认构造函数的过程 

## 必须使用“初始化列表”初始化数据成员

> 初始化列表在构造函数执行前执行
> https://blog.csdn.net/sinat_20265495/article/details/53670644

1.需要初始化的数据成员是对象的情况(这里包含了继承情况下，通过显示调用父类的构造函数对父类数据成员进行初始化)； 

2.需要初始化const修饰的类成员或初始化引用成员数据；

3.子类初始化父类的私有成员；

## 类的成员换了顺序后有什么影响

类成员的声明顺序决定初始化顺序；
构造函数初始化列表不影响初始化顺序；

https://blog.csdn.net/cy_cai/article/details/52980355

## 构造函数的虚函数

如果在构造函数或析构函数中调用虚函数，则运行的是为构造函数或析构函数自身定义的版本

构造函数里头，调用虚函数，派生类对象还没有创建出来，所以调用的是父类的函数

## 析构函数的虚函数

如果在构造函数或析构函数中调用虚函数，则运行的是为构造函数或析构函数自身定义的版本

析构函数里头，同理，派生类的对象已经析构，就只能调用到父类的函数

http://www.cnblogs.com/lixiaohui-ambition/archive/2012/07/13/2589716.html
在实现多态时，当用基类操作派生类，在析构时防止只析构基类而不析构派生类的状况发生。

## 不能继承的类

```
构造函数或析构函数为私有函数，所以该类是无法被继承的，
```
## 只能在堆上定义对象

```
将析构函数定义为private，在栈上不能自动调用析构函数，只能手动调用。
```

## 只能在栈上定义对象

将函数 operator new 和 operator delete 定义为private，这样使用 new 操作符创建对象时候，无法调用operator new，delete销毁对象也无法调用operator delete。

## 函数重载与函数重写

> 函数重载 

须在同一个类中进行 
类无法重载父类的函数，父类同名函数将被名称覆盖 
重载是在编译期间根据参数类型和个数决定函数调用

> 函数重写 

 须发生于父类与子类之间 
 且父类与子类中的函数必须有完全相同的原型 
 用 virtual 声明之后能够产生多态(如果不使用 virtual，那叫重定义)

## 类型转换

const_cast<T>(expression) // 去除常量类型
reinterpret_cast<T>(expression) // 低级转型，复制比特位，为了映射一个完全不同的类型
dynamic_cast<T>(expression) // 安全向下转型。基类指针/引用 -> 派生类指针/引用
static_cast<T>(expression)  // 强迫类型转换

在同一继承体系中:
upcast(向上转换即子类转成父类):没有问题.因为父类的行为都包含在子类中;
downcast(向下转换):有可能会出现问题,编译时可能不会发现.

>    const_cast 一般用于强制消除对象的常量性。它是唯一能做到这一点的 C++ 风格的强制转型。

>    dynamic_cast 主要用于执行“安全的向下转型（safe downcasting）”，也就是说，要确定一个对象是否是一个继承体系中的一个特定类型。它是唯一不能用旧风格语法执行的强制转型。也是唯一可能有重大运行时代价的强制转型。（过一会儿我再提供细节。）

>    reinterpret_cast 是特意用于底层的强制转型，导致实现依赖（implementation-dependent）（就是说，不可移植）的结果，例如，将一个指针转型为一个整数。这样的强制转型在底层代码以外应该极为罕见。在本书中我只用了一次，而且还仅仅是在讨论你应该如何为裸内存（raw memory）写一个调谐分配者（debugging allocator）的时候（参见 Item 50）。

>    static_cast 可以被用于强制隐型转换（例如，non-const 对象转型为 const 对象（就像 Item 3 中的），int 转型为 double，等等）。它还可以用于很多这样的转换的反向转换（例如，void* 指针转型为有类型指针，基类指针转型为派生类指针），但是它不能将一个 const 对象转型为 non-const 对象。（只有 const_cast 能做到。）

> 旧风格的强制转型依然合法( (int)i 这种写法 )，但是新的形式更可取。首先，在代码中它们>更容易识别（无论是人还是像 grep 这样的工具都是如此），这样就简化了在代码中寻找类型系统被破坏的地方的过程。第二，更精确地指定每一个强制转型的目的，使得编译器诊断使用错误成为可能。例如，如果你试图使用一个 const_cast 以外的新风格强制转型来消除常量性，你的代码将无法编译。
## 运算符重载

除了类属关系运算符"."、成员指针运算符"->"、作用域运算符"::"、sizeof运算符和三目运算符"?:"以外，C++中的所有运算符都可以重载。

赋值= 下标[] 调用() 必须为定义为类成员操作符

## 友元函数

类的友元函数是定义在类外部，但有权访问类的所有私有（private）成员和保护（protected）成员。尽管友元函数的原型有在类的定义中出现过，但是友元函数并不是成员函数。

因为友元函数没有this指针，则参数要有三种情况： 

要访问非static成员时，需要对象做参数；

要访问static成员或全局变量时，则不需要对象做参数；

如果做参数的对象是全局对象，则不需要对象做参数.

可以直接调用友元函数，不需要通过对象或指针

# 内存相关

## 编译过程

词法分析-> 语法分析 -> 代码优化 -> 代码生成

##　sizeof

C语言 sizeof函数详解 https://blog.csdn.net/wzy198852/article/details/7246836

链接：<https://www.nowcoder.com/discuss/55353>

class A {};: sizeof(A) = 1;

class A { virtual Fun(){} };: sizeof(A) = 4(32位机器)/8(64位机器);

class A { static int a; };: sizeof(A) = 1;

class A { int a; };: sizeof(A) = 4;

class A { static int a; int b; };: sizeof(A) = 4;

## sizeof 的结构体对齐

32位系统

 - 一个char（占用1-byte）变量以1-byte对齐。
 - 一个short（占用2-byte）变量以2-byte对齐。
 - 一个int（占用4-byte）变量以4-byte对齐。
 - 一个long（占用4-byte）变量以4-byte对齐。
 - 一个float（占用4-byte）变量以4-byte对齐。
 - 一个double（占用8-byte）变量以8-byte对齐。
 - 一个long double（占用12-byte）变量以4-byte对齐。
 - 任何pointer（占用4-byte）变量以4-byte对齐。

而在64位系统下，与上面规则对比有如下不同：

 - 一个long（占用8-byte）变量以8-byte对齐。

 - 一个long double（占用16-byte）变量以16-byte对齐。

 - 任何pointer（占用8-byte）变量以8-byte对齐。


```#pragma pack(2)```的作用是定义了结构体的对齐方式，在这里指定了是按规2字节对齐

成员对齐有一个重要的条件,即每个成员按自己的方式对齐.其对齐的规则是,每个成员按其类型的对齐参数(通常是这个类型的大小)和指定对齐参数(这里默认是8字节)中较小的一个对齐.并且结构的长度必须为所用过的所有对齐参数的整数倍,不够就补空字节

https://blog.csdn.net/ablenavy/article/details/2849577

## new-delete malloc-free

- malloc/free 是C语言的标准库函数，new/delete 是C++的运算符。 

1) malloc与free是C++/C语言的标准库函数，new/delete是C++的运算符。它们都可用于申请动态内存和释放内存。

2) 对于非内部数据类型的对象而言，光用maloc/free无法满足动态对象的要求。对象在创建的同时要自动执行构造函数，对象在消亡之前要自动执行析构函数。由于malloc/free是库函数而不是运算符，不在编译器控制权限之内，不能够把执行构造函数和析构函数的任务强加于malloc/free。

[《new 和 malloc 的区别》](http://blog.jobbole.com/109234)

[《实现和调试 Malloc、Free、Calloc 和 Realloc 的快速教程》 ](http://blog.jobbole.com/82511/)

- new是类型安全的，malloc不是。

int a=new float[2]是通不过编译的，new 内置了sizeof、类型转换和类型安全检查功能。而malloc的返回类型是void*，malloc只负责申请空间。

- 对于非内部数据类型的对象而言，new 在创建动态对象的同时完成了初始化工作，malloc则没有，calloc初始化，内存为0。对于内部数据类型需要加圆括号new才执行初始化工作。string属于非内部数据类型。```int arr=new int[10];```没有初始化，```int arr=new int[10]()```;初始化为0。

new由两步构成：1.operator new    2.调用构造函数

第一步相当于malloc的功能，但是operator new可以重载，可以自定义内存分配策略，甚至不做内存分配，甚至分配到非内存设备上，malloc则无能为力。

new由malloc分配内存空间，然后判断是否分配，并发出bad_alloc的异常消息.


## STL 空间配置器 alloc

在 SGI 中，如果用了一级配置器，便是直接使用了malloc() 和 free() 函数，而如果使用了二级适配器，则如果所申请的内存区域大于 128b,直接使用一级适配器，否则，使用二级适配器。

http://blog.jobbole.com/103759

一级配置器：__malloc_alloc_template

上面说过， SGI STL 中， 如果申请的内存区域大于 128B 的时候，就会调用一级适配器，而一级适配器的调用也是非常简单的， 直接用 malloc 申请内存，用 free 释放内存。

二级配置器：__default_alloc_template

内存池

```c++
union _Obj {
        union _Obj* _M_free_list_link;
        char _M_client_data[1];    /* The client sees this.        */
  };
static _Obj*  _S_free_list[]; //我就是这样用的
```

分配 allocate  释放 deallocate

## 深拷贝 浅拷贝

在某些状况下，类内成员变量需要动态开辟堆内存，如果实行位拷贝，也就是把对象里的值完全复制给另一个对象，如A=B。这时，如果B中有一个成员变量指针已经申请了内存，那A中的那个成员变量也指向同一块内存。这就出现了问题：当B把内存释放了（如：析构），这时A内的指针就是野指针了，出现运行错误。

深拷贝和浅拷贝可以简单理解为：如果一个类拥有资源，当这个类的对象发生复制过程的时候，资源重新分配，这个过程就是深拷贝，反之，没有重新分配资源，就是浅拷贝。下面举个深拷贝的例子。

## 零拷贝

https://www.jianshu.com/p/fad3339e3448

mmap sendfile splice

## 内存空间分布

> cat /proc/[pid]/maps

从低地址到高地址分布为：text 代码区，初始化的数据区，未初始化的数据区，堆，栈，命令行参数和环境变量。看 https://blog.csdn.net/oyw5201314ck/article/details/79397676 的图。

- 栈区（stack）—   由编译器自动分配释放   ，存放函数的参数值，局部变量的值等。其操作方式类似于数据结构中的栈。

- 堆区（heap）   —   一般由程序员分配释放，若程序员不释放，程序结束时可能由OS回收。注意它与数据结构中的堆是两回事，分配方式倒是类似于链表，呵呵。 

- 全局区（静态区）（static）—，全局变量和静态变量的存储是放在一块的，初始化的全局变量和静态变量在一块区域，未初始化的全局变量和未初始化的静态变量在相邻的另一块区域。   -   程序结束后由系统释放。

- 文字常量区   —常量字符串就是放在这里的。程序结束后由系统释放

- 程序代码区—存放函数体的二进制代码。

>   BSS段：BSS段（bss segment）通常是指用来存放程序中未初始化的全局变量的一块内存区域。BSS是英文Block Started by Symbol的简称。BSS段属于静态内存分配。
>   ELF ： ELF (Executable and Linkable Format)是Unix及类Unix系统下可执行文件、共享库等二进制文件标准格式。
>   

```cpp
int a = 0;   //全局初始化区   
char *p1;   //全局未初始化区   
int main()   
{   
  int b;   //栈   
  char s[]   =   "abc";   //栈   
  char *p2;   //栈   
  char *p3   =   "123456";   // 123456/0在常量区，p3在栈上。   
  static int c =0；   //全局（静态）初始化区   
  p1 = (char *)malloc(10);   
  p2 = (char *)malloc(20);   
  // 分配得来得10和20字节的区域就在堆区。   
  strcpy(p1, "123456");
  // 123456/0放在常量区，编译器可能会将它与p3所指向的"123456" 优化成一个地方。 
  return 0;
}    
```


# STL

## unordered_map 和 map 的区别

不同的是 unordered_map 不会根据 key 的大小进行排序，

存储时是根据 key 的 hash 值判断元素是否相同，即 unordered_map 内部元素是无序的，而 map中的元素是按照二叉搜索树存储，进行中序遍历会得到有序遍历。

## 智能指针

https://blog.csdn.net/weizhengbo/article/details/68957993

### auto_ptr
指向 new 出来的内存，资源独占，自动释放
不能指向数组（delete 而非delete[]） 不能作为容器对象（不支持拷贝构造与赋值）

### unique_ptr
同auto_ptr 但是直接赋值会编译出错

```cpp
template<classT>
class unique_ptr //前身是scoped_pt，实现粗暴—>禁止转移-->独占资源（只允许一个指针管理资源）
                //（禁止调拷贝构造和赋值运算符）,它只能管理单个对象
{
public:
    unique_ptr (T*p =NULL) :ptr(p)
    {}
    T* operator*()
    {
        return*ptr;
    }
    T* operator->()
    {
        returnptr;
    }
    voidget_ptr()
    {
        returnptr;
    }
    ~unique_ptr ()
    {
        if(ptr)

        {
            delete ptr;
            ptr= NULL;
        }
    }
private:
    unique_ptr (unique_ptr <T>&ap);//禁止拷贝构造
    unique_ptr <T>&operator=( unique_ptr <T>&ap1);//禁止赋值
    T*ptr;
};
```
### share_ptr
随意赋值 引用为0才析构 可能有环状引用

### weak_ptr
指向一个由shared_ptr管理的对象而不影响所指对象的生命周期，也就是说，它只引用，不计数。

## priority_queue

priority_queue调用 STL里面的 make_heap(), pop_heap(), push_heap() 算法实现，也算是堆的另外一种形式。

priority_queue默认为大顶堆，即堆顶元素为堆中最大元素。如果我们想要用小顶堆的话需要增加使用两个参数：

```cpp
priority_queue<int, vector<int>, greater<int> > q;  // 小顶堆
priority_queue<int, vector<int>, less<int> > q;     // 大顶堆
```

## vector 使用的注意点

vector 的下标只能用于已经初始化的对象

```c++
// 错误的例子
vector<int> a;
for(int i=0;i<10;i++)
    a[i]=i;
```

## STL容器的线程安全问题

http://www.cnblogs.com/ztteng/p/3411738.html

多个读取者是安全的。

对不同容器的多个写入者是安全的

以下列方式同步基本上可以做到线程安全的容器(就是在有写操作的情况下仍能保证安全)。

> 1.每次调用容器的成员函数的期间需要锁定。
>
> 2.每个容器容器返回迭代器的生存期需要锁定。
>
> 3.每个容器在调用算法的执行期需要锁定。

## STL sort()

https://blog.csdn.net/ouyangjinbin/article/details/51094300

只接受RandomAccessIterators（随机存取迭代器）

STL的sort()算法，数据量大时采用Quick Sort，分段递归排序。一旦分段后的数据量小于某个阈值，为避免Quick Sort的递归调用带来过大的额外开销，就改用Insertion Sort（插入排序）。如果递归层次过深，还会改用Heap Sort。

## STL partial_sort()

paitical_sort的原理是 **堆排序**

## STL std::list.sort()

http://www.cnblogs.com/avota/p/5388865.html
归并排序

## 迭代器失效的问题

《STL之容器：抉择时机，剔除元素，迭代器失效._caiaw_新浪博客》
[http://blog.sina.com.cn/s/blog_69883c580100sdmo.html](http://blog.sina.com.cn/s/blog_69883c580100sdmo.html)

vector 插入（push_back）数据后 end 失效

vector 插入（push_back）数据后 引起调整，全部失效

vector 删除（erase pop_back）删除点以及之后的全失效

deque 增加元素全部迭代器失效

deque 删除中间元素使得全部迭代器失效

deque 删除头尾元素使得指向该元素的迭代器失效

list 增加任何元素都不会使迭代器失效

list 删除元素使该迭代器失效

set 删除元素使该迭代器失效，增加、删除其他元素无影响

map 删除元素使该迭代器失效，增加、删除其他元素无影响

## 迭代器的 it++ 和 ++it

```++it``` 返回引用，```it++``` 返回一个临时对象

# 面向对象

## 三特征五原则

封装、继承、多态

- 单一职责
- 开放封闭（一个模块在扩展性方面应该是开放的而在更改性方面应该是封闭的）
- 替换原则（子类应当可以替换父类并出现在父类能够出现的任何地方）
- 依赖原则（具体依赖抽象，上层依赖下层）
- 接口分离原则

## 单例

```
class Log
{
public:
    static Log& instance()
    {
        static Log theLog;
        return theLog;
    }
    virtual void write(char const * logline);
    virtual void save(char const * filename);
private:
	Log();
	Log& operator=(Log const &);
	Log(Log const &);
	
	static std::list<std::string> m_data;
}
```
## 线程安全的单例

```c++
class singleton{
public:
  static singleton * getInstance()
  {
    if(instance == NULL)
    {
      pthread_metux_lock(&lock);
      if(instance == NULL)
        instance = new singleton;
      pthread_metux_unlock(&lock);
    }
    return instance;
  }
private:
  static singleton * instance;
  static pthread_metux_t lock;
}
pthread_mutex_t singleton::lock = PTHREAD_MUTEX_INITIALIZER;
singleton singleton::instance = NULL;
```
## 对象复用

对象池可以显著提高性能，如果一个对象的创建非常耗时或非常昂贵，频繁去创建的话会非常低效。对象池通过对象复用的方式来避免重复创建对象，它会事先创建一定数量的对象放到池中，当用户需要创建对象的时候，直接从对象池中获取即可，用完对象之后再放回到对象池中，以便复用。这种方式避免了重复创建耗时或耗资源的大对象，大幅提高了程序性能。本文将探讨对象池的技术特性以及源码实现。

unique_ptr

https://www.cnblogs.com/virusolf/p/5008517.html

## 大小端转换
```cpp
#define BigLittleSwap32(A) ((((uint32)(A) & 0xff000000) >> 24) | \
                    (((uint32)(A) & 0x00ff0000) >> 8) | \
                    (((uint32)(A) & 0x0000ff00) << 8) | \
                    (((uint32)(A) & 0x000000ff) << 24))
```
## 设计模式

以 Java 的例子为主，仅供参考的链接

https://www.runoob.com/design-pattern/design-pattern-tutorial.html

### 单例
### 订阅发布模式
### 工厂模式

对上层的使用者隔离对象创建的过程，
