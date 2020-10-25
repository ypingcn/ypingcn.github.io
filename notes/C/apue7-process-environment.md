---
layout: page
title:  第七章 进程环境
update: 2017-09-25 20:18 +0800
---

```cpp
//八种方式使进程终止（正常终止和异常终止）
#include <stdlib.h> // ISO C
void exit(int __status) // 有清理工作
void _Exit(int __status)　// 直接返回内核
#include <unistd.h> // POSIX
void _exit(int __status)　// 直接返回内核
int atexit(void (*__func)()) // 注册以便在　main 函数结束后调用，调用顺序和注册顺序相反。
//exit()和atexit()_nobadyelse_新浪博客
//http://blog.sina.com.cn/s/blog_5cec5bad0100b0x2.html


#include <stdlib.h>
void * malloc(size_t __size)
void * calloc(size_t __nmemb, size_t __size)
void * realloc(void *__ptr, size_t __size)
void free(void *__ptr)

#include <stdlib.h>
char * getenv(const char *__name);
//P168
int putenv(char *__string)
int setenv(const char *__name, const char *__value, int __replace) // //__replace 为非0 则删除原有定义再重新设置，为0 则不修改
int unsetenv(const char *__name)

//setjmp longjmp 在函数之间跳转
//gettrlimit settrlimit 资源限制　p175
```